#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_score = float('-inf')
    best_key = None
    for k, v in a_dictionary.items():
        if isinstance(v, int) and v > max_score:
            max_score = v
            best_key = k
    return best_key
