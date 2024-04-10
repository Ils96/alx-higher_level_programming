#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    Prevent user from instan new LockedClass attribute
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
