#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_list = set()
    add = 0
    for i in my_list:
        if i not in unique_list:
            add += i
            unique_list.add(i)
    return add
