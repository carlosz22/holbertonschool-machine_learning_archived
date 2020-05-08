#!/usr/bin/env python3

"""Defines a Deep Neural Network for binary classification"""
import numpy as np


class DeepNeuralNetwork:
    """Class DeepNeuralNetwork"""

    def __init__(self, nx, layers):
        """Constructor method"""
        if type(nx) is not int:
            raise TypeError('nx must be an integer')
        elif nx < 1:
            raise ValueError('nx must be a positive integer')

        if type(layers) is not list \
           and all(type(x) is not int or x < 0 for x in layers):
            raise TypeError('layers must be a list of positive integers')

        self.L = len(layers)
        self.cache = {}
        self.weights = {}
        for i in range(self.L):
            W_key = "W" + str(i + 1)
            b_key = "b" + str(i + 1)
            if i == 0:
                self.weights[W_key] = np.random.randn(
                    layers[i], nx) * np.sqrt(2/nx)
                self.weights[b_key] = np.zeros((layers[i], 1))
            else:
                self.weights[W_key] = np.random.randn(
                    layers[i], layers[i-1]) * np.sqrt(2/layers[i-1])
                self.weights[b_key] = np.zeros((layers[i], 1))
