#!/usr/bin/env python3

"""Module Howdy Partner: Concatenates two arrays"""


def cat_arrays(arr1, arr2):
    """Concatenates two arrays"""

    new_array = arr1[:]
    new_array.extend(arr2)
    return new_array
