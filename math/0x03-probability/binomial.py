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
