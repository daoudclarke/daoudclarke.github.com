#!/usr/bin/env python3
"""
Generate Bluesky thread from blog post using Claude API.

Usage:
    python generate_thread.py <post-filename>

Example:
    python generate_thread.py 2026-02-20-thoughts-on-standardizing-languages.md
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime, UTC, timezone
from pathlib import Path

import yaml
from anthropic import Anthropic
from dotenv import load_dotenv


def parse_blog_post(filepath):
    """Parse Jekyll blog post and extract frontmatter and content."""
    if not filepath.exists():
        raise FileNotFoundError(f"Blog post not found: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract YAML frontmatter
    frontmatter_match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$', content, re.DOTALL)
    if not frontmatter_match:
        raise ValueError("Invalid blog post format: missing YAML frontmatter")
    
    frontmatter_text = frontmatter_match.group(1)
    body = frontmatter_match.group(2).strip()
    
    # Parse YAML
    frontmatter = yaml.safe_load(frontmatter_text)
    
    return {
        'frontmatter': frontmatter,
        'body': body,
        'filename': filepath.name
    }


def extract_image_from_post(frontmatter, body):
    """
    Extract primary image from blog post.
    
    Priority order:
    1. Frontmatter 'image' field
    2. First markdown image in body
    
    Returns:
        dict with 'path' and 'alt' keys, or None if no image found
    """
    # Priority 1: Frontmatter image field
    if 'image' in frontmatter:
        image_url = frontmatter['image']
        # Convert URL to local path
        # https://daoudclarke.net/img/file.jpg -> img/file.jpg
        if 'daoudclarke.net' in image_url:
            image_path = image_url.split('daoudclarke.net/')[-1]
        else:
            image_path = image_url.lstrip('/')
        
        # Use title as alt text if available
        alt_text = frontmatter.get('title', '')
        return {'path': image_path, 'alt': alt_text}
        
    # Priority 2: First markdown image in body
    pattern = r'!\[(.*?)\]\((.*?)\)'
    match = re.search(pattern, body)
    if match:
        alt_text = match.group(1)
        image_path = match.group(2)
        
        # Handle Jekyll liquid tags: {{"/img/file.jpg"}}
        liquid_match = re.search(r'\{\{["\'](.*?)["\']\}\}', image_path)
        if liquid_match:
            image_path = liquid_match.group(1)
        
        # Clean path
        image_path = image_path.lstrip('/')
        
        return {'path': image_path, 'alt': alt_text}
        
    return None  # No image found


def construct_blog_url(filename, base_url="https://daoudclarke.net"):
    """Construct blog post URL from filename using Jekyll permalink structure."""
    # Extract date and title from filename: YYYY-MM-DD-title.md
    match = re.match(r'^(\d{4})-(\d{2})-(\d{2})-(.+)\.md$', filename)
    if not match:
        raise ValueError(f"Invalid filename format: {filename}")
    
    year, month, day, title = match.groups()
    
    # Jekyll permalink format: /:categories/:year/:month/:day/:title
    # Since we don't have categories, use: /year/month/day/title
    url = f"{base_url}/{year}/{month}/{day}/{title}"
    
    return url


def generate_thread_with_claude(title, content, url, api_key):
    """Use Claude API to generate a 5-post Bluesky thread."""
    client = Anthropic(api_key=api_key)
    
    prompt = f"""Please split this blog post up into parts for posting as a thread on social media, each with a maximum of 280 chars.

Content: {content}
URL: {url}

Requirements:
- Use only the original text plus a thread number indicator at the end: e.g. 1/6
- Include any link URLs within the text as plain text
- Shorten sentences if necessary but DO NOT add any words
- Each post MUST be 280 characters or less
- The last post should include the text: "Original article at: " URL

Return ONLY a JSON array with exactly 5 strings, nothing else. Example format:
["Part 1 text here", "Part 2 text here", "Part 3 text here", "Part 4 text here", ..."]"""

    try:
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        response_text = message.content[0].text.strip()
        
        # Parse JSON response
        posts = json.loads(response_text)
        
        if not isinstance(posts, list) or len(posts) != 5:
            raise ValueError(f"Expected 5 posts, got {len(posts) if isinstance(posts, list) else 'invalid format'}")
        
        # Validate character limits
        for i, post in enumerate(posts, 1):
            if len(post) > 280:
                print(f"Warning: Post {i} exceeds 280 characters ({len(post)} chars). Attempting to regenerate...")
                # Try one more time with emphasis on character limit
                return generate_thread_with_claude_strict(title, content, url, api_key, posts)
        
        return posts
    
    except json.JSONDecodeError as e:
        print(f"Error: Failed to parse Claude response as JSON: {e}")
        print(f"Response was: {response_text}")
        sys.exit(1)
    except Exception as e:
        print(f"Error calling Claude API: {e}")
        sys.exit(1)


def generate_thread_with_claude_strict(title, content, url, api_key, previous_posts):
    """Retry generation with stricter character limit enforcement."""
    client = Anthropic(api_key=api_key)
    
    prompt = f"""The previous thread generation had posts that were too long. Please regenerate with STRICT character limits.

Title: {title}
Content: {content}
URL: {url}

Previous attempt (some posts too long):
{json.dumps(previous_posts, indent=2)}

Requirements:
- Post 1 (Hook): Engaging opening - MAXIMUM 280 characters
- Posts 2-4 (Key Points): 3 key takeaways - MAXIMUM 280 characters EACH
- Post 5 (Link): Call-to-action with URL - MAXIMUM 280 characters

CRITICAL: Every single post must be 280 characters or less. Count carefully!

Return ONLY a JSON array with exactly 5 strings."""

    try:
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        response_text = message.content[0].text.strip()
        posts = json.loads(response_text)
        
        # Final validation
        for i, post in enumerate(posts, 1):
            if len(post) > 280:
                print(f"Error: Post {i} still exceeds 280 characters ({len(post)} chars) after retry.")
                print(f"Post content: {post}")
                print("\nPlease manually edit the generated thread file to fix character limits.")
        
        return posts
    
    except Exception as e:
        print(f"Error in retry: {e}")
        return previous_posts  # Return original even if too long, user can edit


def create_thread_markdown(posts, metadata):
    """Format thread as markdown with metadata."""
    lines = [
        "---",
        f"source_post: {metadata['source_post']}",
        f"blog_url: {metadata['blog_url']}",
        f"generated_at: {metadata['generated_at']}",
        f"status: draft",
    ]
    
    # Add image metadata if present
    if 'image_path' in metadata:
        lines.append(f"image_path: {metadata['image_path']}")
        lines.append(f"image_alt: {metadata['image_alt']}")
    
    lines.extend([
        "---",
        "",
        f"# Thread: {metadata['title']}",
        ""
    ])
    
    for i, post in enumerate(posts, 1):
        char_count = len(post)
        status = "✓" if char_count <= 280 else "⚠️ TOO LONG"
        
        if i == 1:
            lines.append(f"## Post {i} (Hook) [{char_count}/280 chars {status}]")
        elif i == 5:
            lines.append(f"## Post {i} (Link) [{char_count}/280 chars {status}]")
        else:
            lines.append(f"## Post {i} [{char_count}/280 chars {status}]")
        
        lines.append(post)
        lines.append("")
    
    return "\n".join(lines)


def save_thread(content, output_path):
    """Save thread markdown to file."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Thread generated successfully!")
    print(f"Saved to: {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate Bluesky thread from blog post using Claude API"
    )
    parser.add_argument(
        "post_filename",
        help="Blog post filename (e.g., 2026-02-20-thoughts-on-standardizing-languages.md)"
    )
    parser.add_argument(
        "--posts-dir",
        default=".",
        help="Directory containing blog posts (default: .)"
    )
    parser.add_argument(
        "--threads-dir",
        default="threads",
        help="Directory to save generated threads (default: threads)"
    )
    
    args = parser.parse_args()
    
    # Load environment variables
    load_dotenv()
    api_key = os.getenv("CLAUDE_API_KEY")
    
    if not api_key:
        print("Error: CLAUDE_API_KEY not found in environment variables")
        print("Please add it to your .env file")
        sys.exit(1)
    
    # Parse blog post
    print("Parsing blog post...")
    post_path = Path(args.posts_dir) / args.post_filename
    
    try:
        post_data = parse_blog_post(post_path)
    except Exception as e:
        print(f"Error parsing blog post: {e}")
        sys.exit(1)
    
    # Construct URL
    try:
        blog_url = construct_blog_url(args.post_filename)
    except Exception as e:
        print(f"Error constructing URL: {e}")
        sys.exit(1)
    
    # Get title from frontmatter
    title = post_data['frontmatter'].get('title', 'Untitled')
    
    print(f"Title: {title}")
    print(f"URL: {blog_url}")
    
    # Extract image if present
    image_data = extract_image_from_post(post_data['frontmatter'], post_data['body'])
    if image_data:
        print(f"Image found: {image_data['path']}")
    
    print("\nGenerating thread with Claude API...")
    
    # Generate thread
    posts = generate_thread_with_claude(
        title=title,
        content=post_data['body'],
        url=blog_url,
        api_key=api_key
    )
    
    # Create metadata
    metadata = {
        'source_post': args.post_filename,
        'blog_url': blog_url,
        'title': title,
        'generated_at': datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
    }
    
    # Add image metadata if present
    if image_data:
        metadata['image_path'] = image_data['path']
        metadata['image_alt'] = image_data['alt']
    
    # Format as markdown
    thread_markdown = create_thread_markdown(posts, metadata)
    
    # Save to file
    output_filename = args.post_filename  # Keep same filename
    output_path = Path(args.threads_dir) / output_filename
    save_thread(thread_markdown, output_path)
    
    print(f"\nReview and edit the thread, then post with:")
    print(f"python post_thread.py {output_path}")


if __name__ == "__main__":
    main()
