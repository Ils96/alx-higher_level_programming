#!/usr/bin/python3

"""Defines a text file insert function."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string .
    Args:
        filename (str): The name file.
        search_string (str): The string to search for the file.
        new_string (str): The string to ins.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
