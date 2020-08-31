#!/usr/bin/python

"""
This problem was asked by Yelp.

Given a mapping of digits to letters (as in a phone number), and a digit string, return all possible letters the number could represent. You can assume each valid number in the mapping is a single digit.

For example if {"2": ["a", "b", "c"], 3: ["d", "e", "f"], ...} then "23" should return ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""

# For recursion problem, the key is to find out the transforming pattern
#
# 1. Already got results of f(nums[:i])
# 2. How to get f(nums[:i+1], like:
#    f(nums[:i+1]) = [ w+c for w in f(nums[:i]) for c in map[nums[i]] ]
#

mapping={
    '2': ['a', 'b', 'c' ],
    '3': ['d', 'e', 'f' ],
    '4': ['g', 'h', 'i' ],
}

def get_letter_strings(nums):
    results = [ '' ]
    for num in nums:
        results = [ w+c for w in results for c in mapping[num] ]
    return results

assert get_letter_strings('') == ['']
assert get_letter_strings('3') == ['d', 'e', 'f']
assert get_letter_strings('23') == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
