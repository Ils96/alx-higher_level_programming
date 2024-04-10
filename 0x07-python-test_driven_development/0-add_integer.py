#!/usr/bin/python3
"""Defines integer add func."""


def add_integer(a, b=98):
    """Return the integer.

    Float arguments are typecasted to ints bef add is performed.

    Raises:
        TypeError: If either a or b is  non-integer and non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
