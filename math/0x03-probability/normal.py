#!/usr/bin/env python3

"""Contains Normal distribution as a class"""


class Normal:
    """Class: Normal distribution"""

    def __init__(self, data=None, mean=0., stddev=1.):
        """Constructor method"""
        if data is None:
            if stddev <= 0:
                raise ValueError('stddev must be a positive value')
            else:
                self.mean = float(mean)
                self.stddev = float(stddev)
        else:
            if type(data) is not list:
                raise TypeError('data must be a list')
            elif len(data) < 2:
                raise ValueError('data must contain multiple values')
            else:
                self.mean = float(sum(data) / len(data))
                stddev = float(sum([((x - mean)) for x in data])/len(data))
                self.stddev = stddev
