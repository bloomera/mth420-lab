# matplotlib_intro.py
"""Python Essentials: Intro to Matplotlib.
Adrian Bloomer
MTH 420
April 28
"""

import numpy as np
from matplotlib import pyplot as plt

# Problem 1
def var_of_means(n):
    """ Create an (n x n) array of values randomly sampled from the standard
    normal distribution. Compute the mean of each row of the array. Return the
    variance of these means.

    Parameters:
        n (int): The number of rows and columns in the matrix.

    Returns:
        (float) The variance of the means of each row.
    """
    x = np.random.normal(size=(n,n))
    x = np.mean(x, axis=1)
    return np.var(x)

def prob1():
    """ Create an array of the results of var_of_means() with inputs
    n = 100, 200, ..., 1000. Plot and show the resulting array.
    """
    x = np.arange(100, 1001, 100)
    y = [var_of_means(n) for n in x]
    plt.plot(x,y)
    plt.show()

#prob1()

# Problem 2
def prob2():
    """ Plot the functions sin(x), cos(x), and arctan(x) on the domain
    [-2pi, 2pi]. Make sure the domain is refined enough to produce a figure
    with good resolution.
    """
    x = np.arange(-2*np.pi, 2*np.pi, 0.1)
    plt.plot(x, np.sin(x))
    plt.plot(x, np.cos(x))
    plt.plot(x, np.arctan(x))
    plt.show()
    
#prob2()


# Problem 3
def prob3():
    """ Plot the curve f(x) = 1/(x-1) on the domain [-2,6].
        1. Split the domain so that the curve looks discontinuous.
        2. Plot both curves with a thick, dashed magenta line.
        3. Set the range of the x-axis to [-2,6] and the range of the
           y-axis to [-6,6].
    """
    x1 = np.arange(-2, 1, 0.1)
    x2 = np.arange(1, 6, 0.1)
    for x in [x1, x2]:
        plt.plot(x, 1/(x-1), 'm--', linewidth=4)
    plt.xlim(-2, 6)
    plt.ylim(-6, 6)
    plt.show()

#prob3()
    

# Problem 4
def prob4():
    """ Plot the functions sin(x), sin(2x), 2sin(x), and 2sin(2x) on the
    domain [0, 2pi], each in a separate subplot of a single figure.
        1. Arrange the plots in a 2 x 2 grid of subplots.
        2. Set the limits of each subplot to [0, 2pi]x[-2, 2].
        3. Give each subplot an appropriate title.
        4. Give the overall figure a title.
        5. Use the following line colors and styles.
              sin(x): green solid line.
             sin(2x): red dashed line.
             2sin(x): blue dashed line.
            2sin(2x): magenta dotted line.
    """
    x = np.linspace(0, 2*np.pi, 100)
    plt.suptitle('sine functions')
    
    plt.subplot(221)
    plt.plot(x, np.sin(x), 'g-')
    plt.axis([0, 2*np.pi, -2, 2])
    plt.title('sin(x)')
    
    plt.subplot(222)
    plt.plot(x, np.sin(2*x), 'r--')
    plt.axis([0, 2*np.pi, -2, 2])
    plt.title('sin(2x)')
    
    plt.subplot(223)
    plt.plot(x, 2*np.sin(x), 'b--')
    plt.axis([0, 2*np.pi, -2, 2])
    plt.title('2sin(x)')
    
    plt.subplot(224)
    plt.plot(x, 2*np.sin(2*x), 'm:')
    plt.axis([0, 2*np.pi, -2, 2])
    plt.title('2sin(2x)')
    
    plt.show()

#prob4()

# Problem 5
def prob5():
    """ Visualize the data in FARS.npy. Use np.load() to load the data, then
    create a single figure with two subplots:
        1. A scatter plot of longitudes against latitudes. Because of the
            large number of data points, use black pixel markers (use "k,"
            as the third argument to plt.plot()). Label both axes.
        2. A histogram of the hours of the day, with one bin per hour.
            Label and set the limits of the x-axis.
    """
    raise NotImplementedError("Problem 5 Incomplete")


# Problem 6
def prob6():
    """ Plot the function g(x,y) = sin(x)sin(y)/xy on the domain
    [-2pi, 2pi]x[-2pi, 2pi].
        1. Create 2 subplots: one with a heat map of g, and one with a contour
            map of g. Choose an appropriate number of level curves, or specify
            the curves yourself.
        2. Set the limits of each subplot to [-2pi, 2pi]x[-2pi, 2pi].
        3. Choose a non-default color scheme.
        4. Include a color scale bar for each subplot.
    """
    x = np.linspace(-2*np.pi, 2*np.pi, 100)
    y = np.linspace(-2*np.pi, 2*np.pi, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(X) * np.sin(Y) / (X * Y)
    
    plt.subplot(121)
    plt.pcolormesh(X, Y, Z, cmap="viridis", shading="auto")
    plt.colorbar()
    plt.xlim(-2*np.pi, 2*np.pi)
    plt.ylim(-2*np.pi, 2*np.pi)
    
    plt.subplot(122)
    plt.contour(X, Y, Z, 15, cmap="coolwarm")
    plt.colorbar()
    plt.xlim(-2*np.pi, 2*np.pi)
    plt.ylim(-2*np.pi, 2*np.pi)
    
    plt.show()

#prob6()