#!/usr/bin/python3
def square_matrix_map(mat=[]):
    return list(map((lambda row: list(map((lambda x: x * x), row))), mat))
