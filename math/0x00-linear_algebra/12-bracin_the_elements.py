#!/usr/bin/env python3

"""Module Bracing The Elements:
    Performs element-wise addition, substraction,
     multiplication and division"""


def np_elementwise(mat1, mat2):
    """Performs element-wise calculations"""

    result_tuple = (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2, )
    return result_tuple
