#!/usr/bin/python3
"""a function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """the function"""
    with open(filename, 'r', encoding="UTF8") as f:
        for line in f:
            print(line, end="")
