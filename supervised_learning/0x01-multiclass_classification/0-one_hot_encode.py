#!/usr/bin/env python3

"""Performs one-hot encoding"""
import numpy as np


def one_hot_encode(Y, classes):
    """Performs one-hot encoding"""
    if classes < 1:
        return None

    hot_encoded_matrix = np.zeros((Y.size, classes))
    hot_encoded_matrix[Y, np.arange(Y.size)] = 1
    return hot_encoded_matrix
