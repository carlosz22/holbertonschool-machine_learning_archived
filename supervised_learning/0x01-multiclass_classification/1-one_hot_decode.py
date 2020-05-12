#!/usr/bin/env python3

"""Performs one-hot decoding"""
import numpy as np


def one_hot_decode(one_hot):
    """Performs one-hot decoding"""
    if type(one_hot) is not np.ndarray or one_hot.ndim != 2:
        return None

    decoded_matrix = one_hot.argmax(axis=0)
    return decoded_matrix
