#!/usr/bin/python3
def uniq_add(list_to_add=[]):
    to_add = 0
    for j in set(list_to_add):
        to_add += j
    return to_add
