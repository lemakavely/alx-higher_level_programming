#!/usr/bin/python3
def square_matrix_simple(mat=[]):
    return [list(map((lambda x: x * x), elm)) for elm in mat]
