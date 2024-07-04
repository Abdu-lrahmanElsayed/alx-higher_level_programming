#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    my_list_len = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            my_list_len += 1
    except IndexError:
        pass
    finally:
        print()
        return my_list_len
