#!/usr/bin/python

"""

This problem was asked by Stripe.

Given an integer n, return the length of the longest consecutive run of 1s in its binary representation.

For example, given 156, you should return 3.

"""

# Idea:  perform (n &= n>>1) until n become 0
#
#     n=156      10011100     longest consecutive of 1 == 3
#              & 01001110               |
#            --------------             V
#              = 00001100               2

def get_longest_consecutive_ones(n):
    length=0
    while n:
        n&=n>>1
        length+=1
    return length

assert get_longest_consecutive_ones(156)==3



