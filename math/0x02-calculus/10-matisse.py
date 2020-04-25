#!/usr/bin/env python3
"""Differentiates a polynomial"""


def poly_derivative(poly):
    """Differentiates a polynomial"""

    if (type(poly) is not list and len(poly) < 1):
        return None

    derivative_coef = [poly[i] * i for i in range(len(poly))]

    return derivative_coef[1:]
