#!/usr/bin/python3
"""This module prints a text with 2 new lines after each of: ., ? and :"""


def text_indentation(text):
    """The function to print and check every thing is ok"""
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    chars = ".?:"
    lines = []
    txt = ""
    for c in text:
        txt += c
        if c in chars:
            lines.append(txt.strip())
            txt = ""
    for line in lines:
        print(line)
        print("")


if __name__ == "__main__":
    import doctest
    doctest.testmethod("tests/5-text_indentation.txt")
