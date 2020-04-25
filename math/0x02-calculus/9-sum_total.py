#!/usr/bin/env python3
"""Summation done recursively"""


def summation_i_squared(n):
    """Summation done recursively"""

    result = 0
    if (type(n) is not int or n < 1):
        return None

    if (n == 1):
        return 1

    result += (summation_i_squared(n - 1) + n ** 2)
    return int(result)
