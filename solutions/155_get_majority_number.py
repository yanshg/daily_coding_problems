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

assert get_majority_element([1, 2, 1, 1, 3, 4, 0])==1

