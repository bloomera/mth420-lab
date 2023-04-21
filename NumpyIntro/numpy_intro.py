# numpy_intro.py
"""Python Essentials: Intro to NumPy.
Adrian Bloomer
MTH 420
April 21
"""

import numpy as np

def prob1():
    """ Define the matrices A and B as arrays. Return the matrix product AB. """
    a = np.array([
        [3,-1,4],[1,5,-9]
    ])
    b = np.array([
        [2,6,-5,3],[5,-8,9,7],[9,-3,-2,-3]
    ])
    return a @ b

print(prob1())


def prob2():
    """ Define the matrix A as an array. Return the matrix -A^3 + 9A^2 - 15A. """
    a = np.array([
        [3,1,4],[1,5,9],[-5,3,1]
    ])
    return -a@a@a+9*a@a-15*a

print(prob2())


def prob3():
    """ Define the matrices A and B as arrays using the functions presented in
    this section of the manual (not np.array()). Calculate the matrix product ABA,
    change its data type to np.int64, and return it.
    """
    a = np.triu(np.ones((7,7)))
    print(a)
    b = np.full((7,7),-1) + 6*a - 6*np.eye(7)
    print(b)
    return (a@b@a).astype(np.int64)

print(prob3())


def prob4(A):
    """ Make a copy of 'A' and use fancy indexing to set all negative entries of
    the copy to 0. Return the resulting array.

    Example:
        >>> A = np.array([-3,-1,3])
        >>> prob4(A)
        array([0, 0, 3])
    """
    A = A.copy()
    A[A < 0] = 0
    return A

print(prob4(np.array([-3,-1,3])))


def prob5():
    """ Define the matrices A, B, and C as arrays. Use NumPy's stacking functions
    to create and return the block matrix:
                                | 0 A^T I |
                                | A  0  0 |
                                | B  0  C |
    where I is the 3x3 identity matrix and each 0 is a matrix of all zeros
    of the appropriate size.
    """
    a = np.array([
        [0,2,4],[1,3,5]
    ])
    b = np.array([
        [3,0,0],[3,3,0],[3,3,3]
    ])
    c = -2*np.eye(3)
    return np.hstack((
      np.vstack((np.zeros((3,3)),a,b)),
      np.vstack((a.T,np.zeros((5,2)))),
      np.vstack((np.eye(3),np.zeros((2,3)),c))
    ))

print(prob5())


def prob6(A):
    """ Divide each row of 'A' by the row sum and return the resulting array.
    Use array broadcasting and the axis argument instead of a loop.

    Example:
        >>> A = np.array([[1,1,0],[0,1,0],[1,1,1]])
        >>> prob6(A)
        array([[ 0.5       ,  0.5       ,  0.        ],
               [ 0.        ,  1.        ,  0.        ],
               [ 0.33333333,  0.33333333,  0.33333333]])
    """
    return (A.T / A.sum(axis=1)).T

print(prob6(np.array([[1,1,0],[0,1,0],[1,1,1]])))

def prob7():
    """ Given the array stored in grid.npy, return the greatest product of four
    adjacent numbers in the same direction (up, down, left, right, or
    diagonally) in the grid. Use slicing, as specified in the manual.
    """
    raise NotImplementedError("Problem 7 Incomplete")
