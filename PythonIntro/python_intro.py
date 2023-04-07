# python_intro.py
"""Python Essentials: Introduction to Python.
Adrian Bloomer
MTH 420
April 7
"""


# Problem 1 (write code below)
if __name__ == "__main__":
    print("Hello, world!")


# Problem 2
def sphere_volume(r):
    """ Return the volume of the sphere of radius 'r'.
    Use 3.14159 for pi in your computation.
    """
    return 4 / 3 * 3.14159 * r**3

if __name__ == "__main__":
    print(sphere_volume(1))


# Problem 3
def isolate(a, b, c, d, e):
    """ Print the arguments separated by spaces, but print 5 spaces on either
    side of b.
    """
    print(a, "   ", b, "   ", c, d, e)

if __name__ == "__main__":
    isolate(1, 2, 3, 4, 5)

# Problem 4
def first_half(my_string):
    """ Return the first half of the string 'my_string'. Exclude the
    middle character if there are an odd number of characters.

    Examples:
        >>> first_half("python")
        'pyt'
        >>> first_half("ipython")
        'ipy'
    """
    return my_string[:(len(my_string)//2)]

def backward(my_string):
    """ Return the reverse of the string 'my_string'.

    Examples:
        >>> backward("python")
        'nohtyp'
        >>> backward("ipython")
        'nohtypi'
    """
    return my_string[::-1]

if __name__ == "__main__":
    print(first_half("python"))
    print(first_half("ipython"))
    print(backward("python"))

# Problem 5
def list_ops():
    """ Define a list with the entries "bear", "ant", "cat", and "dog".
    Perform the following operations on the list:
        - Append "eagle".
        - Replace the entry at index 2 with "fox".
        - Remove (or pop) the entry at index 1.
        - Sort the list in reverse alphabetical order.
        - Replace "eagle" with "hawk".
        - Add the string "hunter" to the last entry in the list.
    Return the resulting list.

    Examples:
        >>> list_ops()
        ['fox', 'hawk', 'dog', 'bearhunter']
    """
    a = ["bear", "ant", "cat", "dog"]
    a.append("eagle")
    a[2] = "fox"
    a.pop(1)
    a.sort(reverse=True)
    a[a.index("eagle")] = "hawk"
    a[-1] += "hunter"
    return a

if __name__ == "__main__":
    print(list_ops())


# Problem 6
def pig_latin(word):
    """ Translate the string 'word' into Pig Latin, and return the new word.

    Examples:
        >>> pig_latin("apple")
        'applehay'
        >>> pig_latin("banana")
        'ananabay'
    """
    if word[0] in "aeiou":
        return word + "hay"
    else:
        return word[1:] + word[0] + "ay"

if __name__ == "__main__":
    print(pig_latin("apple"))
    print(pig_latin("banana"))

# Problem 7
def palindrome():
    """ Find and retun the largest panindromic number made from the product
    of two 3-digit numbers.
    """
    biggest_x = 0
    biggest_y = 0
    biggest_product = 0
    for x in range(100, 1000):
        for y in range(100, 1000):
            if x*y > biggest_product and str(x*y) == str(x*y)[::-1]:
                biggest_x = x
                biggest_y = y
                biggest_product = x*y
    print(biggest_x, "*", biggest_y, "=", biggest_product)
    return biggest_product

if __name__ == "__main__":
    palindrome()

# Problem 8
def alt_harmonic(n):
    """ Return the partial sum of the first n terms of the alternating
    harmonic series, which approximates ln(2).
    """
    return sum([(-1)**(k+1)/k for k in range(1, n+1)])


if __name__ == "__main__":
    print(alt_harmonic(500000))