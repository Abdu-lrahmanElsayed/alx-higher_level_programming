#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    my_list_len = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                my_list_len += 1
        print()
        return my_list_len
    except SyntaxError:
        pass
