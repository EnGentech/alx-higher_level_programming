#!/usr/bin/python3
"""A program to implement the test
valueable using doctest written by
EnGentech"""


def matrix_divided(matrix, div):
    """created a function for matrix with div"""
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    else:
        for val in matrix:
            for check in val:
                if type(check) is not int and type(check) is not float:
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    chk_val = 0
    val = len(matrix[0])
    for i in matrix:
        if len(i) != val:
            chk_val = 1

    if chk_val == 1:
        raise TypeError("Each row of the matrix must have the same size")

    if type (div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = matrix.copy()
    result = [[round(i/div, 2) for i in row] for row in new_matrix]
    return result
    #EnGentech signature
