#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return my_list
    my_list.reverse()
    [print('{:d}'.format(i)) for i in my_list]
