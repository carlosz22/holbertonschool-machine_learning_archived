#!/usr/bin/env python3

"""Performs one-hot encoding"""
import numpy as np


def one_hot_encode(Y, classes):
    """Performs one-hot encoding"""
    if type(Y) is not np.ndarray or Y.size < 1:
        return None
    if type(classes) is not int or classes < 1:
        return None

    hot_encoded_matrix = np.zeros((classes, Y.size))
    hot_encoded_matrix[Y, np.arange(Y.size)] = 1
    print(hot_encoded_matrix.shape)
    return hot_encoded_matrix
