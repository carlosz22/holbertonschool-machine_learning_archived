#!/usr/bin/env python3

"""Defines a Neural Network for binary classification"""
import numpy as np
import matplotlib.pyplot as plt


class NeuralNetwork:
    """Class NeuralNetwork"""

    def __init__(self, nx, nodes):
        """Constructor method"""
        if type(nx) is not int:
            raise TypeError('nx must be an integer')
        elif nx < 1:
            raise ValueError('nx must be a positive integer')

        if type(nodes) is not int:
            raise TypeError('nodes must be an integer')
        elif nodes < 1:
            raise ValueError('nodes must be a positive integer')

        self.__W1 = np.random.randn(*(nodes, nx))
        self.__b1 = np.zeros((nodes, 1))
        self.__A1 = 0
        self.__W2 = np.random.randn(*(1, nodes))
        self.__b2 = 0
        self.__A2 = 0

    @property
    def W1(self):
        """W1 getter"""
        return self.__W1

    @property
    def b1(self):
        """b1 getter"""
        return self.__b1

    @property
    def A1(self):
        """A1 getter"""
        return self.__A1

    @property
    def W2(self):
        """W2 getter"""
        return self.__W2

    @property
    def b2(self):
        """b2 getter"""
        return self.__b2

    @property
    def A2(self):
        """A2 getter"""
        return self.__A2

    def forward_prop(self, X):
        """Calulates the forward propagation"""
        Z1 = np.matmul(self.__W1, X) + self.__b1
        self.__A1 = 1/(1 + np.exp(-Z1))
        Z2 = np.matmul(self.__W2, self.__A1) + self.__b2
        self.__A2 = 1/(1 + np.exp(-Z2))
        return self.__A1, self.__A2

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
        cost = self.cost(Y, self.__A2)
        y_hat = self.__A2.round().astype(int)
        return y_hat, cost

    def gradient_descent(self, X, Y, A1, A2, alpha=0.05):
        """Performs gradient descent"""
        m = Y.shape[1]
        dZ2 = A2 - Y
        db2 = 1/m * np.sum(dZ2, axis=1, keepdims=True)
        dW2 = 1/m * np.matmul(dZ2, A1.T)
        dZ1 = np.matmul(self.__W2.T, dZ2) * (A1 * (1 - A1))
        db1 = 1/m * np.sum(dZ1, axis=1, keepdims=True)
        dW1 = 1/m * np.matmul(dZ1, X.T)
        self.__b2 = self.__b2 - alpha * db2
        self.__W2 = self.__W2 - alpha * dW2
        self.__b1 = self.__b1 - alpha * db1
        self.__W1 = self.__W1 - alpha * dW1

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
            self.gradient_descent(X, Y, self.__A1, self.__A2, alpha)
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
