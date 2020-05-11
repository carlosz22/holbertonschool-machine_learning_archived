#!/usr/bin/env python3

"""Defines a Neuron for binary classification"""
import numpy as np
import matplotlib.pyplot as plt


class Neuron:
    """Class Neuron"""

    def __init__(self, nx):
        """Constructor method"""

        if type(nx) is not int:
            raise TypeError('nx must be an integer')
        if nx < 1:
            raise ValueError('nx must be a positive integer')

        self.__W = np.random.randn(*(1, nx))
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """W getter"""
        return self.__W

    @property
    def b(self):
        """b getter"""
        return self.__b

    @property
    def A(self):
        """A getter"""
        return self.__A

    def forward_prop(self, X):
        """Calulates the forward propagation"""
        Z = np.matmul(self.__W, X) + self.__b
        self.__A = 1/(1 + np.exp(-Z))
        return self.__A

    def cost(self, Y, A):
        """Calculates the cost"""
        m = Y.shape[1]
        cost = -1/m * np.sum(np.multiply(
            Y, np.log(A)) + np.multiply((1 - Y), np.log(1.0000001 - A)))
        return cost

    def evaluate(self, X, Y):
        """Performs binary classification
        Outputs prediction matrix and cost"""
        self.forward_prop(X)
        cost = self.cost(Y, self.__A)
        y_hat = self.__A.round().astype(int)
        return y_hat, cost

    def gradient_descent(self, X, Y, A, alpha=0.05):
        """Performs gradient descent"""
        m = Y.shape[1]
        dZ = A - Y
        db = 1/m * np.sum(dZ)
        dW = 1/m * np.matmul(X, dZ.T)
        self.__b = self.__b - alpha * db
        self.__W = self.__W - alpha * dW.T

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
            self.gradient_descent(X, Y, self.__A, alpha)
            y_hat, cost = self.evaluate(X, Y)
            if (i % step == 0 or i == iterations):
                cost_data.append(cost)
                step_data.append(i)
                if verbose is True:
                    print("Cost after {} iterations: {}".format(i, cost))

        if graph is True:
            plt.plot(step_data, cost_data, 'b-')
            plt.title('Training Cost')
            plt.xlabel('iteration')
            plt.ylabel('cost')
            plt.show()

        return y_hat, cost
