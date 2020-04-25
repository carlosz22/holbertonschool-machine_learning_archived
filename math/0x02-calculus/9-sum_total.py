#!/usr/bin/env python3
"""Summation done recursively"""


def summation_i_squared(n):
    """Summation done recursively"""

    if (type(n) is not int or n < 1):
        return None

    result = (n * (n + 1)) * (2 * n + 1) / 6
    return int(result)
