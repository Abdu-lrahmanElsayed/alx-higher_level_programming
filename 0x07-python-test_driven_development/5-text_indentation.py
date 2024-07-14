#!/usr/bin/python3
"""This module prints a text with 2 new lines after each of: ., ? and :"""


def text_indentation(text):
    """The function to print and check every thing is ok"""
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    txt = ""
    i = 0
    while i < len(text):
        txt += text[i]
        if text[i] in ".?:":
            txt += "\n\n"
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
    print(txt, end="")


if __name__ == "__main__":
    import doctest
    doctest.testmethod("tests/5-text_indentation.txt")
