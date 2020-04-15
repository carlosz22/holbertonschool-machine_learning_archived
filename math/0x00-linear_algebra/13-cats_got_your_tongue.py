#!/usr/bin/env python3

import numpy as np
"""Module Cat's Got Your Tongue:
    Concatenates two matrices along a specific axis"""


def np_cat(mat1, mat2, axis=0):
    """Concatenates two matrices along a specific axis"""

    return np.concatenate((mat1, mat2), axis=axis).copy()
