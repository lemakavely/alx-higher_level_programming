#!/usr/bin/python3
def simple_delete(a_dictionary, i=""):
    if i in a_dictionary:
        del a_dictionary[i]
    return a_dictionary
