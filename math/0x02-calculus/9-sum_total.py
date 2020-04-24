#!/usr/bin/env python3
"""Summation done recursively"""

def summation_i_squared(n):
    """Summation done recursively"""

    if (n == 1):
        return 1
    return (summation_i_squared(n - 1) + n ** 2)
