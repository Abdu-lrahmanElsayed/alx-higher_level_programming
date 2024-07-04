#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    try:
        for i in range(list_length):
            try:
                idx1 = my_list_1[i]
                idx2 = my_list_2[i]
                if not isinstance(idx1, (int, float)) or
                not isinstance(idx2, (int, float)):
                    print("wrong type")
                    new_list.append(0)
                elif idx2 == 0:
                    print("division by 0")
                    new_list.append(0)
                else:
                    j = idx1 / idx2
                    new_list.append(j)
            except IndexError:
                print("out of range")
                new_list.append(0)
    finally:
        return new_list
