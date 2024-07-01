#!/usr/bin/python3
def weight_average(my_list=[]):
    total_score = 0
    total_weight = 0
    if my_list is None or my_list == []:
        return 0
    else:
        for s, w in my_list:
            total_score += s * w
            total_weight += w
        return total_score / total_weight
