#!/usr/bin/env python3

"""Module Line Up: Returns the sum of two arrays element-wise"""


def add_arrays(arr1, arr2):
    """Returns the sum of two arrays element-wise"""

    added_array = []

    if (len(arr1) != len(arr2)):
        return None

    for i in range(len(arr1)):
        sum = arr1[i] + arr2[i]
        added_array.append(sum)

    return added_array
