#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        i = "{0:d}".format(value)
        print(i)
        return True
    except Exception:
        return False
