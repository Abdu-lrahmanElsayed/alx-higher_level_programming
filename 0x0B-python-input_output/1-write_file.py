#!/usr/bin/python3
""" function that writes a string to a text file
    andreturns the number of characters written"""


def write_file(filename="", text=""):
    """the function"""
    with open(filename, 'w', encoding="UTF8") as f:
        return f.write(text)
