#!/usr/bin/python3
def complex_delete(a_dictionary, val):
    del_key = []
    for i in a_dictionary:
        if a_dictionary[i] == val:
            del_key.append(i)
    for j in del_key:
        del a_dictionary[j]
    return a_dictionary
