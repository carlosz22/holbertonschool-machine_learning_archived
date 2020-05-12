#!/usr/bin/env python3

"""Performs one-hot encoding"""
import numpy as np


def one_hot_encode(Y, classes):
    """Performs one-hot encoding"""
    if type(Y) is not np.ndarray or len(Y) < 1:
        return None
    if (type(classes) is not int or classes < 1 or classes < np.amax(Y)):
        return None

    m = len(Y)
    hot_encoded_matrix = np.zeros((classes, m))
    hot_encoded_matrix[Y, np.arange(m)] = 1
    return hot_encoded_matrix
