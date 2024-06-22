#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    i = tuple_a[:2] + (0, 0)
    j = tuple_b[:2] + (0, 0)
    tuple_c = (i[0] + j[0], i[1] + j[1])
    return tuple_c
