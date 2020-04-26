#!/usr/bin/env python3
"""Integrates a polynomial"""


def poly_integral(poly, C=0):
    """Integrates a polynomial"""

    if (type(poly) is not list or len(poly) < 1
            or type(C) is not int):
        return None

    if poly == [0]:
        return [C]

    integrate_coef = [poly[i] / (i + 1) for i in range(len(poly))]
    integrate_coef.insert(0, C)
    integrate_coef_fixed = [int(i) if i % 1 == 0 else i
                            for i in integrate_coef]

    return integrate_coef_fixed
