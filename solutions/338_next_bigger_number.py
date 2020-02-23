#!/usr/bin/python

"""

This problem was asked by Facebook.

Given an integer n, find the next biggest integer with the same number of 1-bits on. For example, given the number 6 (0110 in binary), return 9 (1001).

"""

# Article:  https://www.geeksforgeeks.org/next-higher-number-with-same-number-of-set-bits/

def get_next_bigger_number(x): 
    next = 0
    if(x): 
        # right most set bit 
        right_one = x & -(x) 
          
        next_higher_one_bit = x + right_one 
          
        right_ones_pattern = x ^ next_higher_one_bit 
          
        # right adjust pattern 
        right_ones_pattern = right_ones_pattern / right_one
          
        # correction factor 
        right_ones_pattern = right_ones_pattern >> 2
          
        next = next_higher_one_bit | right_ones_pattern 

    return next

# example:                                    x = b'11011100'
#  with x&-x                          right_one = b'00000100'
#  x + right_one            next_higher_one_bit = b'11100000'
#  x^next_higher_one_bit     right_ones_pattern = b'00111100'
#  after / right_one,        right_ones_pattern = b'00001111'
#  after >> 2,               right_ones_pattern = b'00000011'
#                                          next = b'11100011'

assert get_next_bigger_number(6)==9
