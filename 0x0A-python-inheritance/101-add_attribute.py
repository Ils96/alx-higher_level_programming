#!/usr/bin/python3

"""Defines function that add attribute to obj."""

def add_attribute(obj, att, value):
    """Add n attribute to an objt if possible.
    Args:
        obj (any): The object to add an attribute to.
        att (str): The name of attribute to add to obj.
        value (any): The value of att.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
