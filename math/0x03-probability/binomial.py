#!/usr/bin/env python3

"""Contains Binomial distribution as a class"""


class Binomial:
    """Class: Binomial distribution"""

    def __init__(self, data=None, n=1, p=0.5):
        """Constructor method"""
        if data is None:
            if n <= 0:
                raise ValueError('n must be a positive value')
            elif p <= 0 or p >= 1:
                raise ValueError('p must be greater than 0 and less than 1')
            else:
                self.n = int(n)
                self.p = float(p)
        else:
            if type(data) is not list:
                raise TypeError('data must be a list')
            elif len(data) < 2:
                raise ValueError('data must contain multiple values')
            else:
                mean = float(sum(data) / len(data))
                var = sum([((x - mean)) ** 2 for x in data])/len(data)
                variance = float(var)
                self.p = - (variance / mean) + 1
                self.n = round(mean / self.p)
                self.p = mean / self.n

    def pmf(self, k):
        """Calculates the value of the PMF for a given number of successes"""

        if type(k) is not int:
            int(k)

        if k < 0:
            return 0

        factorial_n = 1
        for i in range(1, self.n + 1):
            factorial_n *= i

        factorial_k = 1
        for i in range(1, k + 1):
            factorial_k *= i

        factorial_n_k = 1
        for i in range(1, (self.n - k) + 1):
            factorial_n_k *= i

        factorial_term = (factorial_n / (factorial_k * factorial_n_k))
        pmf = factorial_term * (self.p ** k) * ((1 - self.p) ** (self.n - k))
        return pmf
