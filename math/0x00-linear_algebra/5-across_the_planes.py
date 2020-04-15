#!/usr/bin/env python3

"""Module Across The Planes: Returns the sum of two 2D matrices element-wise"""


def add_matrices2D(mat1, mat2):
    """Returns the sum of two 2D matrices element-wise"""

    added_matrix = []

    if (len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0])):
        return None

    for i in range(len(mat1)):
        inner_list = []
        for j in range(len(mat1[0])):
            sum = mat1[i][j] + mat2[i][j]
            inner_list.append(sum)
        added_matrix.append(inner_list)

    return added_matrix
