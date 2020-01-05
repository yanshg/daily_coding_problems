#!/usr/bin/python

"""
This question was asked by ContextLogic.

Implement division of two positive integers without using the division, multiplication, or modulus operators. Return the quotient as an integer, ignoring the remainder.

"""

def divide(dividend, divisor):
    if not divisor:
        return

    sum, quotient=0, 0
    while sum<=dividend:
        sum+=divisor
        quotient+=1
    return quotient-1

assert not divide(1,0)
assert divide(0,1)==0
assert divide(1,1)==1
assert divide(16,2)==8
assert divide(13,3)==4
