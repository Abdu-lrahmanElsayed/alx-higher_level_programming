#!/usr/bin/python3
"""a module for append_after function"""


def append_after(filename="", search_string="", new_string=""):
    """a function that inserts a line of text to a file,
        after each line containing a specific string"""
    with open(filename, 'r', encoding="UTF8") as f:
        lines = f.readlines()
    with open(filename, 'w', encoding="UTF8") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
