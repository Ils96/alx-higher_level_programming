#!/usr/bin/python3

"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Checks if an object is antance of a class.
    Args:
        obj : The object to check.
        a_class (type): The class to pe of obj to.
    Returns:
        If obj is an i inst of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
