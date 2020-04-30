#!/usr/bin/env python3

"""Contains Poisson distribution as a class"""


class Poisson:
    """Class: Poisson distribution"""

    def __init__(self, data=None, lambtha=1.):
        """Constructor method"""
        if data is None:
            if lambtha < 0:
                raise ValueError('lambtha must be a positive value')
            else:
                self.lambtha = float(lambtha)
        else:
            if type(data) is not list:
                raise TypeError('data must be a list')
            elif len(data) < 2:
                raise ValueError('data must contain multiple values')
            else:
                self.lambtha = float(sum(data) / len(data))
