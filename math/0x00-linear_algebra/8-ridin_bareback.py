#!/usr/bin/env python3

"""Module Ridin’ Bareback : Performs matrix multiplication"""


def mat_mul(mat1, mat2):
    """Performs matrix multiplication"""

    new_matrix = []

    if (len(mat1[0]) != len(mat2)):
        return None

    for i in range(len(mat1)):
        inner_list = []
        for k in range(len(mat2[0])):
            inner_result = 0
            for j in range(len(mat1[0])):
                inner_result += mat1[i][j] * mat2[j][k]
            inner_list.append(inner_result)
        new_matrix.append(inner_list)
    return new_matrix
