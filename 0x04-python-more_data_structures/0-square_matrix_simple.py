#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    new_matrix = [[n**2 for n in new] for new in new_matrix]
    return new_matrix
