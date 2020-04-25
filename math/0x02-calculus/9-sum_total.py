#!/usr/bin/env python3
"""Summation done recursively"""


def summation_i_squared(n):
    """Summation done recursively"""

    if (type(n) not in [int, float]):
        return None

    if (n == 1):
        return 1
    elif (n < 1):
        return int(summation_i_squared(n + 1) + n ** 2)

    return int(summation_i_squared(n - 1) + n ** 2)
