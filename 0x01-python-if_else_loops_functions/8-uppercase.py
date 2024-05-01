#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if 'a' <= i <= 'z':
            print("{:s}".format(chr(ord(i) - 32)), end='')
        else:
            print("{:s}".format(i), end='')
    print()
