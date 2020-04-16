#!/usr/bin/env python3

"""Module Slice Like A Ninja:
    Slices a matrix along a specific axes"""


def np_slice(matrix, axes={}):
    """Slices a matrix along a specific axes"""

    max_key = max(axes.keys())
    new_matrix = matrix.copy()
    slice_list = []

    for i in range(max_key + 1):
        values = axes.get(i, None)
        if values is not None:
            slice_list.append(slice(*values))
        else:
            slice_list.append(slice(None))

    return new_matrix[slice_list]
