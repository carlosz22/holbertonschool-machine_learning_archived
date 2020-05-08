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

        if type(layers) is not list or len(layers) < 1:
            raise TypeError('layers must be a list of positive integers')

        self.__L = len(layers)
        self.__cache = {}
        self.__weights = {}
        for i in range(self.__L):
            if type(layers[i]) is not int or layers[i] < 0:
                raise TypeError('layers must be a list of positive integers')
            W_key = "W" + str(i + 1)
            b_key = "b" + str(i + 1)
            if i == 0:
                self.__weights[W_key] = np.random.randn(
                    layers[i], nx) * np.sqrt(2/nx)
                self.__weights[b_key] = np.zeros((layers[i], 1))
            else:
                self.__weights[W_key] = np.random.randn(
                    layers[i], layers[i-1]) * np.sqrt(2/layers[i-1])
                self.__weights[b_key] = np.zeros((layers[i], 1))

    @property
    def L(self):
        """L getter"""
        return self.__L

    @property
    def cache(self):
        """cache getter"""
        return self.__cache

    @property
    def weights(self):
        """weights getter"""
        return self.__weights
