#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{0:d}".format(value))
        return True
    except Exception:
        return False
