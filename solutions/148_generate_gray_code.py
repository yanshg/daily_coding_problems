#!/usr/bin/python

"""
This problem was asked by Apple.

Gray code is a binary code where each successive value differ in only one bit, as well as when wrapping around. Gray code is common in hardware so that we don't see temporary spurious values during transitions.

Given a number of bits n, generate a possible gray code for it.

For example, for n = 2, one gray code would be [00, 01, 11, 10].

"""

def get_gray_codes(n):
    if not n:
        return ['']

    gcs=get_gray_codes(n-1)
    return [ '0'+ c for c in gcs ] + [ '1'+c for c in reversed(gcs) ]

assert get_gray_codes(1)==['0','1']
assert get_gray_codes(2)==['00','01','11','10']
assert get_gray_codes(3) == ['000', '001', '011',
                             '010', '110', '111', '101', '100']
assert get_gray_codes(4) == ['0000', '0001', '0011', '0010', '0110', '0111',
                             '0101', '0100', '1100', '1101', '1111', '1110', '1010', '1011', '1001', '1000']
