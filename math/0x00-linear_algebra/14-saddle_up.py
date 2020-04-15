#!/usr/bin/env python3

"""Module Saddle Up:
    Performs matrix multiplication (dot product)"""

import numpy as np


def np_matmul(mat1, mat2):
    """Performs matrix multiplication"""

    return np.dot(mat1, mat2).copy()
