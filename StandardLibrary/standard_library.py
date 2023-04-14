# standard_library.py
"""Python Essentials: The Standard Library.
Adrian Bloomer
MTH 420
April 14
"""


# Problem 1
def prob1(L):
    """Return the minimum, maximum, and average of the entries of L
    (in that order, separated by a comma).
    """
    return min(L), max(L), sum(L)/len(L)

print(prob1([1, 2, 3]))


# Problem 2
def prob2():
    """Determine which Python objects are mutable and which are immutable.
    Test integers, strings, lists, tuples, and sets. Print your results.
    """
    v1 = 1
    v2 = v1
    v2 += 1
    print("int", "is mutable" if v1 == v2 else "is not mutable")
    
    v1 = "a"
    v2 = v1
    v2 += "b"
    print("string", "is mutable" if v1 == v2 else "is not mutable")
    
    v1 = ["a"]
    v2 = v1
    v2[0] = "b"
    print("list", "is mutable" if v1 == v2 else "is not mutable")
    
    v1 = ("a",)
    v2 = v1
    v2 += ("b",)
    print("tuple", "is mutable" if v1 == v2 else "is not mutable")
    
    v1 = {1, 2}
    v2 = v1
    v2.add(3)
    print("set", "is mutable" if v1 == v2 else "is not mutable")
    
prob2()

import calculator as calc

# Problem 3
def hypot(a, b):
    """Calculate and return the length of the hypotenuse of a right triangle.
    Do not use any functions other than sum(), product() and sqrt() that are
    imported from your 'calculator' module.

    Parameters:
        a: the length one of the sides of the triangle.
        b: the length the other non-hypotenuse side of the triangle.
    Returns:
        The length of the triangle's hypotenuse.
    """
    return calc.sqrt(calc.sum(calc.product(a, a), calc.product(b, b)))

print(hypot(3, 4))

import itertools

# Problem 4
def power_set(A):
    """Use itertools to compute the power set of A.

    Parameters:
        A (iterable): a str, list, set, tuple, or other iterable collection.

    Returns:
        (list(sets)): The power set of A as a list of sets.
    """
    return [set(x) for x in itertools.chain(
        *[itertools.combinations(A, n) for n in range(0, len(A)+1)]
    )]

print(power_set([1, 2, 3]))
print(power_set("abc"))


# Problem 5: Implement shut the box.
def shut_the_box(player, timelimit):
    """Play a single game of shut the box."""
    raise NotImplementedError("Problem 5 Incomplete")
