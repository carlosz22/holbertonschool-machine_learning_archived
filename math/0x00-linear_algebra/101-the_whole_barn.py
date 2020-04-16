#!/usr/bin/env python3

"""Module The Whole Barn: Adds two matrices recursively"""


def add_matrices(mat1, mat2):
    """Adds two matrices recursively"""

    new_matrix = []

    if (len(mat1) != len(mat2)):
        return None

    if (type(mat1) == list and type(mat1[0]) == list):
        for i in range(len(mat1)):
            value = add_matrices(mat1[i], mat2[i])
            if value is not None:
                new_matrix.append(value)
            else:
                return None
    else:
        for i in range(len(mat1)):
            new_matrix.append(mat1[i] + mat2[i])

    return new_matrix
