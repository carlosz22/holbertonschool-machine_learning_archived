#!/usr/bin/env python3

"""Defines a Deep Neural Network for multiclass classification"""
import numpy as np
import matplotlib.pyplot as plt
import pickle


class DeepNeuralNetwork:
    """Class DeepNeuralNetwork"""

    def __init__(self, nx, layers, activation='sig'):
        """Constructor method"""
        if type(nx) is not int:
            raise TypeError('nx must be an integer')
        elif nx < 1:
            raise ValueError('nx must be a positive integer')

        if type(layers) is not list or len(layers) < 1:
            raise TypeError('layers must be a list of positive integers')

        if (activation != 'sig' and activation != 'tanh'):
            raise ValueError("activation must be 'sig' or 'tanh'")

        self.__L = len(layers)
        self.__cache = {}
        self.__weights = {}
        self.__activation = activation
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

    def forward_prop(self, X):
        """Calculates forward propagation"""
        self.__cache['A0'] = X
        for i in range(self.__L):
            lay = str(i + 1)
            lay_min_1 = str(i)
            Zl = np.matmul(self.__weights['W' + lay],
                           self.__cache['A' + lay_min_1]) + \
                self.__weights['b' + lay]
            if i == self.__L - 1:
                t = np.exp(Zl)
                self.__cache['A' + lay] = t / np.sum(t, axis=0, keepdims=True)
            else:
                if self.__activation == 'sig':
                    self.__cache['A' + lay] = 1/(1 + np.exp(-Zl))
                elif self.__activation == 'tanh':
                    self.__cache['A' + lay] == (np.exp(Zl) - np.exp(-Zl)) / \
                        (np.exp(Zl) + np.exp(-Zl))

        return self.__cache['A' + str(self.__L)], self.__cache

    def cost(self, Y, A):
        """Calculates the cost"""
        m = Y.shape[1]
        cost = -1/m * np.sum(Y * np.log(A))
        return cost

    def evaluate(self, X, Y):
        """Performs binary classification
        Outputs prediction matrix and cost"""
        A, _ = self.forward_prop(X)
        cost = self.cost(Y, A)
        A_max = np.amax(A, axis=0)
        y_hat = np.where(A == A_max, 1, 0)
        return y_hat, cost

    def gradient_descent(self, Y, cache, alpha=0.05):
        """Performs gradient descent"""
        m = Y.shape[1]
        # dZ = cache['A' + str(self.__L)] - Y
        for i in reversed(range(self.__L)):
            lay = str(i + 1)
            lay_min_1 = str(i)
            if i == (self.__L - 1):
                dZ = cache['A' + str(self.__L)] - Y
            else:
                if self.__activation == 'sig':
                    dZ = dA * (cache['A' + lay]) * (1 - cache['A' + lay])
                elif self.__activation == 'tanh':
                    dZ = dA * (1 - np.tanh(cache['A' + lay]) ** 2)
            dW = 1/m * np.matmul(dZ, cache['A' + lay_min_1].T)
            db = 1/m * np.sum(dZ, axis=1, keepdims=True)
            dA = np.matmul(self.__weights['W' + lay].T, dZ)
            self.__weights['W' + lay] = self.__weights['W' + lay] - \
                (alpha * dW)
            self.__weights['b' + lay] = self.__weights['b' + lay] - \
                (alpha * db)

    def train(self, X, Y, iterations=5000,
              alpha=0.05, verbose=True, graph=True, step=100):
        """Performs the training for x iterations"""
        if type(iterations) is not int:
            raise TypeError('iterations must be an integer')
        elif iterations <= 0:
            raise ValueError('iterations must be a positive integer')

        if type(alpha) is not float:
            raise TypeError('alpha must be a float')
        elif alpha <= 0:
            raise ValueError('alpha must be positive')

        if (verbose is True or graph is True):
            if type(step) is not int:
                raise TypeError('step must be an integer')
            elif (step <= 0 or step > iterations):
                raise ValueError('step must be positive and <= iterations')

        cost_data = []
        step_data = []
        self.evaluate(X, Y)
        for i in range(iterations):
            self.gradient_descent(Y, self.__cache, alpha)
            y_hat, cost = self.evaluate(X, Y)
            if i % step == 0 or i == iterations:
                cost_data.append(cost)
                step_data.append(i)
                if verbose is True:
                    print("Cost after {} iterations: {}". format(i, cost))

        if graph is True:
            plt.plot(step_data, cost_data, 'b-')
            plt.title('Training Cost')
            plt.xlabel('iteration')
            plt.ylabel('cost')
            plt.show()

        return y_hat, cost

    def save(self, filename):
        """Save object using pickle dump"""
        if not filename.endswith('.pkl'):
            filename += '.pkl'

        with open(filename, 'wb') as file_object:
            pickle.dump(self, file_object)

    @staticmethod
    def load(filename):
        """Load pickle object to the program"""
        try:
            with open(filename, 'rb') as file_object:
                new_object = pickle.load(file_object)
        except IOError:
            return None
        else:
            return new_object
