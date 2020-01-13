#!/usr/bin/python

"""
This problem was asked by Cisco.

Given an unsigned 8-bit integer, swap its even and odd bits. The 1st and 2nd bit should be swapped, the 3rd and 4th bit should be swapped, and so on.

For example, 10101010 should be 01010101. 11100010 should be 11010001.

Bonus: Can you do this in one line?

"""

# 85 is the odd-bit filter '01010101'
def swap_bits(num):
    return ((num & 85) << 1) | ((num & (85 << 1)) >> 1)

# 170 is the even-bit filter '10101010'
def swap_bits_another(num):
    return ((num & 170) >> 1) | ((num & (170 >> 1)) << 1)


assert swap_bits(0) == 0
assert swap_bits(255) == 255
assert swap_bits(210) == 225
assert swap_bits(170) == 85
assert swap_bits(226) == 209

assert swap_bits_another(0) == 0
assert swap_bits_another(255) == 255
assert swap_bits_another(210) == 225
assert swap_bits_another(170) == 85
assert swap_bits_another(226) == 209
