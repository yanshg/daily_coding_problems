#!/usr/bin/python

"""
This problem was asked by MongoDB.

Given a list of elements, find the majority element, which appears more than half the time (> floor(len(lst) / 2.0)).

You can assume that such element exists.

For example, given [1, 2, 1, 1, 3, 4, 0], return 1.

"""

from collections import defaultdict

def get_majority_element(nums):
    min_appears=len(nums)//2
    appears=defaultdict(int)

    for num in nums:
        appears[num]+=1
        if appears[num]>=min_appears:
            return num

    return None

# Boyer-Moore Majorite Vote Algorithm
def get_majority_element1(nums):
    m = -1
    i = 0
    for num in nums:
        if i == 0:
            m = num
            i = 1
        elif m == num:
            i += 1
        else:
            i -= 1
    return m

assert get_majority_element([1, 2, 1, 1, 3, 4, 0])==1
assert get_majority_element1([1, 2, 1, 1, 3, 1, 1, 4, 0, 1])==1

