#!/usr/bin/env python3

"""Contains Exponential distribution as a class"""


class Exponential:
    """Class: Exponential distribution"""

    def __init__(self, data=None, lambtha=1.):
        """Constructor method"""
        if data is None:
            if lambtha <= 0:
                raise ValueError('lambtha must be a positive value')
            else:
                self.lambtha = float(lambtha)
        else:
            if type(data) is not list:
                raise TypeError('data must be a list')
            elif len(data) < 2:
                raise ValueError('data must contain multiple values')
            else:
                self.lambtha = float(len(data) / sum(data))

    def pdf(self, x):
        """Calculates the probability of x happening"""

        if x < 0:
            return 0

        e_cons = 2.7182818285
        pdf = self.lambtha * e_cons ** (-(self.lambtha) * x)

        return pdf

    def cdf(self, x):
        """Calculates the cumulative distribution probability for x"""

        if x < 0:
            return 0

        e_cons = 2.7182818285
        cdf = 1 - (e_cons ** (-(self.lambtha) * x))

        return cdf
