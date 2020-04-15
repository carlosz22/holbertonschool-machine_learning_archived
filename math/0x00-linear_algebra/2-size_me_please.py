#!/usr/bin/env python3

"""Module Matrix Shape: Calculates the shape of a matrix recursively"""


def matrix_shape(matrix):
    """Calculates the shape of a matrix recursively"""

    shape_matrix = []
    if (type(matrix) == list):
        shape_matrix.append(len(matrix))
        shape_matrix.extend(matrix_shape(matrix[0]))

    return shape_matrix
