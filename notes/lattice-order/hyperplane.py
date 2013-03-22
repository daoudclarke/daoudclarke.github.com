# Bismillahi-r-Rahmani-r-Rahim

# Hyperplane - find out what a hyperplane in kernel space
#              looks like in the original space


import numpy as np

def test():
    # Define a positive cone by these two vectors
    a = np.array([-1,-3])
    b = np.array([1,3])
    aa = np.kron(a,a)
    bb = np.kron(b,b)
    print a,b, aa, bb





if __name__ == "__main__":
    test()
