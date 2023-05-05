# lstsq_eigs.py
"""Volume 1: Least Squares and Computing Eigenvalues.
Adrian Bloomer
MTH 420
May 5
"""

# (Optional) Import functions from your QR Decomposition lab.
# import sys
# sys.path.insert(1, "../QR_Decomposition")
# from qr_decomposition import qr_gram_schmidt, qr_householder, hessenberg

import numpy as np
from matplotlib import pyplot as plt
from scipy import linalg as la

# Problem 1
def least_squares(A, b):
    """Calculate the least squares solutions to Ax = b by using the QR
    decomposition.

    Parameters:
        A ((m,n) ndarray): A matrix of rank n <= m.
        b ((m, ) ndarray): A vector of length m.

    Returns:
        x ((n, ) ndarray): The solution to the normal equations.
    """
    q, r = la.qr(A, mode="economic")
    return la.solve_triangular(r, q.T @ b)

# Problem 2
def line_fit():
    """Find the least squares line that relates the year to the housing price
    index for the data in housing.npy. Plot both the data points and the least
    squares line.
    """
    data = np.load("housing.npy")
    years = 2000 + data[:,0]
    a = np.column_stack((years, np.ones(len(years))))
    b = data[:,1]
    x1, x2 = least_squares(a,b)
    plt.scatter(years, b)
    plt.plot(years, x1 * years + x2)
    plt.show()

# Problem 3
def polynomial_fit():
    """Find the least squares polynomials of degree 3, 6, 9, and 12 that relate
    the year to the housing price index for the data in housing.npy. Plot both
    the data points and the least squares polynomials in individual subplots.
    """
    data = np.load("housing.npy")
    years = data[:,0]
    b = data[:,1]
    for i, degree in enumerate([3, 6, 9, 12]):
        plt.subplot(220 + i + 1)
        plt.scatter(2000 + years, b, color='#454545')
        v = np.vander(years, degree + 1)
        coeffs = la.lstsq(v, b)[0]
        poly = np.poly1d(coeffs)
        plt.plot(2000 + years, poly(years), color='#FF6000')
    plt.show()


def plot_ellipse(a, b, c, d, e):
    """Plot an ellipse of the form ax^2 + bx + cxy + dy + ey^2 = 1."""
    theta = np.linspace(0, 2*np.pi, 200)
    cos_t, sin_t = np.cos(theta), np.sin(theta)
    A = a*(cos_t**2) + c*cos_t*sin_t + e*(sin_t**2)
    B = b*cos_t + d*sin_t
    r = (-B + np.sqrt(B**2 + 4*A)) / (2*A)

    plt.plot(r*cos_t, r*sin_t)
    plt.gca().set_aspect("equal", "datalim")

# Problem 4
def ellipse_fit():
    """Calculate the parameters for the ellipse that best fits the data in
    ellipse.npy. Plot the original data points and the ellipse together, using
    plot_ellipse() to plot the ellipse.
    """
    raise NotImplementedError("Problem 4 Incomplete")


# Problem 5
def power_method(A, N=20, tol=1e-12):
    """Compute the dominant eigenvalue of A and a corresponding eigenvector
    via the power method.

    Parameters:
        A ((n,n) ndarray): A square matrix.
        N (int): The maximum number of iterations.
        tol (float): The stopping tolerance.

    Returns:
        (float): The dominant eigenvalue of A.
        ((n,) ndarray): An eigenvector corresponding to the dominant
            eigenvalue of A.
    """
    raise NotImplementedError("Problem 5 Incomplete")


# Problem 6
def qr_algorithm(A, N=50, tol=1e-12):
    """Compute the eigenvalues of A via the QR algorithm.

    Parameters:
        A ((n,n) ndarray): A square matrix.
        N (int): The number of iterations to run the QR algorithm.
        tol (float): The threshold value for determining if a diagonal S_i
            block is 1x1 or 2x2.

    Returns:
        ((n,) ndarray): The eigenvalues of A.
    """
    raise NotImplementedError("Problem 6 Incomplete")
