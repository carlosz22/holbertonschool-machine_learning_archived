#!/usr/bin/env python3

"""Module Gettin’ Cozy : Concatenates two matrices along a specific axis"""


def cat_matrices2D(mat1, mat2, axis=0):
    """Concatenates two matrices along a specific axis"""

    new_matrix = [sublist[:] for sublist in mat1]

    if (axis == 0):
        for i in mat2:
            new_matrix.append(i)
    elif (axis == 1):
        for i in range(len(mat2)):
            new_matrix[i].extend(mat2[i])
    else:
        return None

    return new_matrix
