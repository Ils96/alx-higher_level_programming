#!/usr/bin/python3
"""Module for add_ints meth."""


def add_integer(a, b=98):
    """Adds 2  integers.

    Args:
        a: the first integer.
        b: the second integer, default 98.

    Raises:
        TypeError: if a, b are not int, float.

    Returns:
        The sum of two ints.
    """

    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
