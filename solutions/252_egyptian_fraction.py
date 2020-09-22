#!/usr/bin/python

"""

This problem was asked by Palantir.

The ancient Egyptians used to express fractions as a sum of several terms where each numerator is one. For example, 4 / 13 can be represented as 1 / 4 + 1 / 18 + 1 / 468.

Create an algorithm to turn an ordinary fraction a / b, where a < b, into an Egyptian fraction.

"""

import math

def get_egyptain_fraction(a, b, fractions=[]):
    if a == 0:
        return fractions
    elif a == 1:
        return fractions + [b]

    c = math.ceil(float(b)/a)
    fractions += [ c ]

    a,b = a*c-b, b*c
    return get_egyptain_fraction(a, b, fractions)

assert get_egyptain_fraction(4,13,[]) == [ 4, 18, 468 ]
