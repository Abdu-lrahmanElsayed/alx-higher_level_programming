#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as exc:
        print("Exception: {:}".format(exc), file=sys.stderr)
        return False
