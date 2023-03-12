#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for col in matrix:
        for row in range(len(col)):
            print(
                "{:d}".format(col[row]),
                end="" if row == len(col) - 1 else " ")
        print("")
