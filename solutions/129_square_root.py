#!/usr/bin/python

"""
Given a real number n, find the square root of n. For example, given n = 9, return 3.
"""

import math

def get_sqrt_with_math(n):
    return math.sqrt(n)

TOLERANCE=10**-6
def almost_equal(n1,n2):
    if -TOLERANCE<(n1-n2)<TOLERANCE:
        return True
    return False

def get_sqrt_helper(n,start,end):
    mid=float(start+end)/2
    sq=mid*mid

    if almost_equal(n, sq):
        return round(mid,2)

    if sq>n:
        return get_sqrt_helper(n,start,mid)
    else:
        return get_sqrt_helper(n,mid,end)

def get_sqrt(n):
    return get_sqrt_helper(n,0,n)

assert get_sqrt_with_math(9)==3
assert get_sqrt(9)==3
assert get_sqrt(100)==10
