#!/usr/bin/env python3
"""
Post thread to Bluesky from markdown file.

Usage:
    python post_thread.py <thread-filename>

Example:
    python post_thread.py threads/2026-02-20-thoughts-on-standardizing-languages.md
"""

import argparse
import os
import re
import sys
from pathlib import Path

from atproto import Client
from dotenv import load_dotenv


def parse_thread_markdown(filepath):
    """Parse thread markdown file and extract posts and metadata."""
    if not filepath.exists():
        raise FileNotFoundError(f"Thread file not found: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract YAML frontmatter
    frontmatter_match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$', content, re.DOTALL)
    if not frontmatter_match:
        raise ValueError("Invalid thread format: missing YAML frontmatter")
    
    frontmatter_text = frontmatter_match.group(1)
    body = frontmatter_match.group(2).strip()
    
    # Parse frontmatter manually (simple key: value format)
    metadata = {}
    for line in frontmatter_text.split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            metadata[key.strip()] = value.strip()
    
    # Extract posts from body
    posts = []
    post_pattern = r'## Post \d+.*?\n(.*?)(?=\n## Post|\n*$)'
    matches = re.findall(post_pattern, body, re.DOTALL)
    
    for match in matches:
        post_text = match.strip()
        if post_text:
            posts.append(post_text)
    
    return {
        'metadata': metadata,
        'posts': posts
    }


def validate_thread(posts):
    """Validate thread format and character limits."""
    issues = []
    
    for i, post in enumerate(posts, 1):
        char_count = len(post)
        if char_count > 300:  # Bluesky's actual limit
            issues.append(f"Post {i} exceeds 300 characters ({char_count} chars)")
        elif char_count > 280:  # Our target limit
            issues.append(f"Post {i} exceeds recommended 280 characters ({char_count} chars)")
    
    return issues


def extract_url_facets(text):
    """Extract URLs from text and create facets for clickable links."""
    # URL regex pattern
    url_pattern = r'https?://[^\s<>"{}|\\^`\[\]]+'
    
    facets = []
    for match in re.finditer(url_pattern, text):
        url = match.group(0)
        start = match.start()
        end = match.end()
        
        # Convert character positions to byte positions (required by AT Protocol)
        byte_start = len(text[:start].encode('utf-8'))
        byte_end = len(text[:end].encode('utf-8'))
        
        facets.append({
            "index": {
                "byteStart": byte_start,
                "byteEnd": byte_end
            },
            "features": [{
                "$type": "app.bsky.richtext.facet#link",
                "uri": url
            }]
        })
    
    return facets if facets else None


def upload_image_to_bluesky(client, image_path, alt_text=""):
    """
    Upload image to Bluesky and return embed object.
    
    Args:
        client: Authenticated Bluesky client
        image_path: Path to image file
        alt_text: Alt text for accessibility
    
    Returns:
        dict: Embed object for use in post
    """
    with open(image_path, 'rb') as f:
        image_data = f.read()
    
    # Upload blob
    blob = client.upload_blob(image_data)
    
    # Create embed object
    embed = {
        "$type": "app.bsky.embed.images",
        "images": [{
            "alt": alt_text,
            "image": blob.blob
        }]
    }
    
    return embed


def post_thread_to_bluesky(client, posts, metadata):
    """Post thread to Bluesky with proper reply chains, clickable links, and image on first post."""
    print(f"Posting thread ({len(posts)} posts)...")
    
    # Check for image metadata and upload if present
    image_embed = None
    if 'image_path' in metadata:
        try:
            print(f"  Uploading image: {metadata['image_path']}")
            image_embed = upload_image_to_bluesky(
                client,
                metadata['image_path'],
                metadata.get('image_alt', '')
            )
            print(f"  ✓ Image uploaded successfully")
        except Exception as e:
            print(f"  ⚠️  Warning: Failed to upload image: {e}")
            print(f"  Continuing without image...")
    
    posted_refs = []
    
    for i, post_text in enumerate(posts, 1):
        try:
            # Extract URL facets for clickable links
            facets = extract_url_facets(post_text)
            
            if i == 1:
                # First post - add image if available
                response = client.send_post(
                    text=post_text,
                    facets=facets,
                    embed=image_embed  # Only on first post
                )
            else:
                # Reply to previous post
                parent_ref = {
                    'uri': posted_refs[-1]['uri'],
                    'cid': posted_refs[-1]['cid']
                }
                
                # Root is always the first post
                root_ref = {
                    'uri': posted_refs[0]['uri'],
                    'cid': posted_refs[0]['cid']
                }
                
                response = client.send_post(
                    text=post_text,
                    facets=facets,
                    reply_to={
                        'root': root_ref,
                        'parent': parent_ref
                    }
                )
            
            # Store reference for next post
            posted_refs.append({
                'uri': response.uri,
                'cid': response.cid
            })
            
            print(f"  ✓ Post {i}/{len(posts)} posted")
        
        except Exception as e:
            print(f"  ✗ Error posting post {i}: {e}")
            raise
    
    return posted_refs[0]  # Return first post reference


def update_thread_status(filepath, status='posted'):
    """Update thread file status to indicate it has been posted."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update status in frontmatter
    updated_content = re.sub(
        r'(status:\s*)\w+',
        f'\\1{status}',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(updated_content)


def extract_post_id_from_uri(uri):
    """Extract post ID from AT Protocol URI."""
    # URI format: at://did:plc:xxx/app.bsky.feed.post/xxxxx
    match = re.search(r'/app\.bsky\.feed\.post/([^/]+)$', uri)
    if match:
        return match.group(1)
    return None


def main():
    parser = argparse.ArgumentParser(
        description="Post thread to Bluesky from markdown file"
    )
    parser.add_argument(
        "thread_file",
        help="Thread markdown file (e.g., threads/2026-02-20-thoughts-on-standardizing-languages.md)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate thread without posting"
    )
    
    args = parser.parse_args()
    
    # Load environment variables
    load_dotenv()
    handle = os.getenv("BLUESKY_HANDLE")
    password = os.getenv("BLUESKY_APP_PASSWORD")
    
    if not handle or not password:
        print("Error: BLUESKY_HANDLE and BLUESKY_APP_PASSWORD must be set in .env file")
        sys.exit(1)
    
    # Parse thread file
    print("Reading thread file...")
    thread_path = Path(args.thread_file)
    
    try:
        thread_data = parse_thread_markdown(thread_path)
    except Exception as e:
        print(f"Error parsing thread file: {e}")
        sys.exit(1)
    
    posts = thread_data['posts']
    metadata = thread_data['metadata']
    
    print(f"Thread: {metadata.get('blog_url', 'Unknown')}")
    print(f"Posts: {len(posts)}")
    
    # Validate thread
    print("\nValidating thread format...")
    issues = validate_thread(posts)
    
    if issues:
        print("⚠️  Validation warnings:")
        for issue in issues:
            print(f"  - {issue}")
        
        if any("exceeds 300" in issue for issue in issues):
            print("\nError: Some posts exceed Bluesky's 300 character limit.")
            print("Please edit the thread file to shorten these posts.")
            sys.exit(1)
        
        if not args.dry_run:
            response = input("\nContinue anyway? (y/N): ")
            if response.lower() != 'y':
                print("Aborted.")
                sys.exit(0)
    else:
        print("✓ All posts within character limits")
    
    if args.dry_run:
        print("\n✓ Dry run complete - thread is valid")
        print("\nThread preview:")
        for i, post in enumerate(posts, 1):
            print(f"\n--- Post {i} ({len(post)} chars) ---")
            print(post)
        sys.exit(0)
    
    # Check if already posted
    if metadata.get('status') == 'posted':
        response = input("\n⚠️  This thread appears to have been posted already. Post again? (y/N): ")
        if response.lower() != 'y':
            print("Aborted.")
            sys.exit(0)
    
    # Authenticate with Bluesky
    print("\nAuthenticating with Bluesky...")
    try:
        client = Client()
        client.login(handle, password)
        print(f"✓ Authenticated as @{handle}")
    except Exception as e:
        print(f"Error authenticating: {e}")
        sys.exit(1)
    
    # Post thread
    try:
        first_post = post_thread_to_bluesky(client, posts, metadata)
        
        # Update thread file status
        update_thread_status(thread_path, 'posted')
        
        # Construct thread URL
        post_id = extract_post_id_from_uri(first_post['uri'])
        if post_id:
            # Extract handle without @ if present
            clean_handle = handle.lstrip('@')
            thread_url = f"https://bsky.app/profile/{clean_handle}/post/{post_id}"
            print(f"\n✓ Thread posted successfully!")
            print(f"View at: {thread_url}")
        else:
            print(f"\n✓ Thread posted successfully!")
            print(f"URI: {first_post['uri']}")
    
    except Exception as e:
        print(f"\n✗ Error posting thread: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
