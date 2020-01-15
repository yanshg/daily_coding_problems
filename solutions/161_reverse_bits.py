#!/usr/bin/python

"""
This problem was asked by Facebook.

Given a 32-bit integer, return the number with its bits reversed.

For example, given the binary number 1111 0000 1111 0000 1111 0000 1111 0000, return 0000 1111 0000 1111 0000 1111 0000 1111.

"""

def reverse_bits(n) :
    result=0

    while(n>0):
        result<<=1
        if n&1==1:
            result^=1
        n>>=1

    return result

assert reverse_bits(11)==13
