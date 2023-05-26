# cvxpy_intro.py
"""Volume 2: Intro to CVXPY.
Adrian Bloomer
MTH 420
May 26
"""

import cvxpy as cp
import numpy as np

def prob1():
    """Solve the following convex optimization problem:

    minimize        2x + y + 3z
    subject to      x  + 2y         <= 3
                         y   - 4z   <= 1
                    2x + 10y + 3z   >= 12
                    x               >= 0
                          y         >= 0
                                z   >= 0

    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    x = cp.Variable(3, nonneg = True)
    c = np.array([2, 1, 3])
    objective = cp.Minimize(c.T @ x)
    constraints = [
        1 * x[0] + 2 * x[1] + 0 * x[2] <= 3,
        0 * x[0] + 1 * x[1] + -4 * x[2] <= 1,
        2 * x[0] + 10 * x[1] + 3 * x[2] >= 12,
    ]
    problem = cp.Problem(objective, constraints)
    s = problem.solve()
    return x.value, s

print(prob1())

# Problem 2
def l1Min(A, b):
    """Calculate the solution to the optimization problem

        minimize    ||x||_1
        subject to  Ax = b

    Parameters:
        A ((m,n) ndarray)
        b ((m, ) ndarray)

    Returns:
        The optimizer x (ndarray)
        The optimal value (float)
    """
    n = A.shape[1]
    x = cp.Variable(n, nonneg = True)
    objective = cp.Minimize(cp.norm(x, 1))
    problem = cp.Problem(objective, [A @ x == b])
    s = problem.solve()
    return x.value, s

print(l1Min(np.array([[1,2,1,1],[0,3,-2,-1]]), np.array([7,4])))


# Problem 3
def prob3():
    """Solve the transportation problem by converting the last equality constraint
    into inequality constraints.

    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    x = cp.Variable(6, nonneg = True)
    c = np.array([4, 7, 6, 8, 8, 9])
    objective = cp.Minimize(c.T @ x)
    p1, p2, p3, p4, p5, p6 = x
    constraints = [
        p1 + p2 <= 7,
        p3 + p4 <= 2,
        p5 + p6 <= 4,
        p1 + p3 + p5 == 5,
        p2 + p4 + p6 == 8,
    ]
    problem = cp.Problem(objective, constraints)
    s = problem.solve()
    return x.value, s

print(prob3())


# Problem 4
def prob4():
    """Find the minimizer and minimum of

    g(x,y,z) = (3/2)x^2 + 2xy + xz + 2y^2 + 2yz + (3/2)z^2 + 3x + z

    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    x = cp.Variable(3, nonneg = False)
    Q = np.array([[3, 2, 1], [2, 4, 2], [1, 2, 3]])
    r = np.array([3, 0, 1])
    objective = cp.Minimize(.5 * cp.quad_form(x, Q) + r.T @ x)
    problem = cp.Problem(objective)
    s = problem.solve()
    return x.value, s

print(prob4())


# Problem 5
def prob5(A, b):
    """Calculate the solution to the optimization problem
        minimize    ||Ax - b||_2
        subject to  ||x||_1 == 1
                    x >= 0
    Parameters:
        A ((m,n), ndarray)
        b ((m,), ndarray)

    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    n = A.shape[1]
    x = cp.Variable(n, nonneg = True)
    objective = cp.Minimize(cp.norm(A @ x - b, 2))
    problem = cp.Problem(objective, [cp.sum(x) == 1])
    s = problem.solve()
    return x.value, s

print(prob5(np.array([[1,2,1,1],[0,3,-2,-1]]), np.array([7,4])))


# Problem 6
def prob6():
    """Solve the college student food problem. Read the data in the file
    food.npy to create a convex optimization problem. The first column is
    the price, second is the number of servings, and the rest contain
    nutritional information. Use cvxpy to find the minimizer and primal
    objective.

    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    raise NotImplementedError("Problem 6 Incomplete")