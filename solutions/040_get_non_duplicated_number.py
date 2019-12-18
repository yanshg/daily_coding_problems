#!/usr/bin/python

"""
This problem was asked by Google.

Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.

"""


# Note: the code below fails for negative numbers, but you could shift the entire array by the minimum.
# Note 2: the implementation below makes it evident that the space complexity is O(log_2(n)) rather than O(1).
# This is always the case, unless a specific integer type or a maximum value are specified (they are not above).

import math

def get_non_duplicated_number(numbers):
    bits = [0] * int(math.ceil(math.log(max(numbers), 2)))  # low endian

    for number in numbers:
        index = 0
        while number > 0:
            bits[index] += number & 1
            number //= 2
            index += 1

    return sum((b % 3) * 2**i for i, b in enumerate(bits))


assert get_non_duplicated_number([6, 1, 3, 3, 3, 6, 6]) == 1
assert get_non_duplicated_number([13, 19, 13, 13]) == 19
