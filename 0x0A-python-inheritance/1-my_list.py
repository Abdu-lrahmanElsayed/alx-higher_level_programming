#!/usr/bin/python3
"""a class MyList that inherits from list"""


class MyList(list):
    """child class"""

    def print_sorted(self):
        """to create sorted list"""
        for i in self:
            if not isinstance(i, int):
                raise TypeError('The index must be integer')
        print(sorted(self))

if __name__ == "__main__":
    import doctest
    doctest.testmethod("tests/1-my_list.txt")
