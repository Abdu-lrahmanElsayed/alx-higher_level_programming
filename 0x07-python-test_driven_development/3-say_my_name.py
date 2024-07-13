#!/usr/bin/python3
"""This module prints My name is <first name> <last name>"""


def say_my_name(first_name, last_name=""):
    """this is the function

        args: first_name, last_name with standard value no thing

        raises: TypeError: if the name in not string
        """
    if not isinstance(first_name, str) or first_name is None\
            or first_name == "":
        raise TypeError('first_name must be a string')
    elif not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print("My name is {:s} {:s}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testmethod("tests/3-say_my_name.txt")
