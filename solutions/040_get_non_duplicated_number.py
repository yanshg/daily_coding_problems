#!/usr/bin/python

"""
This problem was asked by Google.

Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.

"""

# Article:  https://stackoverflow.com/questions/14100169/find-the-element-that-appears-once
            https://www.quora.com/Given-an-integer-array-such-that-every-element-occurs-3-times-except-one-element-which-occurs-only-once-how-do-I-find-that-single-element-in-O-1-space-and-O-n-time-complexity

# Idea:
#     Bits in 'ones' are set to 1, when that particular bit occurs for the first time.
#     Bits in 'twos' are set to 1, when that particular bit occurs for the second time.
#     If a bit is occurring for more than 2 times, we throw it away and start couting again.

# ones = ones ^ x:                 If it exists in ones, remove it, otherwise, add it.
#
# ones = (ones ^ x) & ~twos:       If appear once, add it to ones,
#                                  If appear twice (exists in ones), remove it from ones,
#                                  If appear third (not exists in ones), throw it away and do not add it in ones.

# twos = (ones & x) | twos:        If exists in ones, add it to twos
#
# twos = (ones & x) | (twos & ~x): If appear once, remove it from twos
#                                  If appear twice (exists in ones), add it to twos
#                                  If appear third (not exists in ones), throw it away and remove it from twos
#

def get_non_duplicated_number(numbers):
    ones, twos = 0, 0
    for x in numbers:
        ones, twos = (ones ^ x) & ~twos, (ones & x) | (twos & ~x)
    assert twos == 0
    return ones


assert get_non_duplicated_number([6, 1, 3, 3, 3, 6, 6]) == 1
assert get_non_duplicated_number([13, 19, 13, 13]) == 19
