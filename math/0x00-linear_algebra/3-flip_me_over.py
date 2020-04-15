#!/usr/bin/env python3

"""Module Flip Me Over: Returns the transpose of a 2D matrix"""


def matrix_transpose(matrix):
    """Returns the transpose of a 2D matrix"""

    transpose = []
    for j in range(len(matrix[0])):
        inner_list = []
        for i in range(len(matrix)):
            inner_list.append(matrix[i][j])
        transpose.append(inner_list)
    return transpose
