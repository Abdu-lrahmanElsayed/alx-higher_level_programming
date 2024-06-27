#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mul_dict = {}
    for k, v in a_dictionary.items():
        mul_dict[k] = v * 2
    return mul_dict
