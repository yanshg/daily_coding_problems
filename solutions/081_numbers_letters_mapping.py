#!/usr/bin/python

"""
This problem was asked by Yelp.

Given a mapping of digits to letters (as in a phone number), and a digit string, return all possible letters the number could represent. You can assume each valid number in the mapping is a single digit.

For example if {"2": ["a", "b", "c"], 3: ["d", "e", "f"], ...} then "23" should return ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""

digit_mapping={
    '2': ['a', 'b', 'c' ],
    '3': ['d', 'e', 'f' ],
    '4': ['g', 'h', 'i' ],
}

def get_letter_strings(nums):
    if not nums:
        return []

    letters=digit_mapping[nums[0]] if nums[0] in digit_mapping else [];
    if len(nums)==1:
        return letters

    return [ letter+other for letter in letters for other in get_letter_strings(nums[1:]) ]

assert get_letter_strings('') == [] 
assert get_letter_strings('3') == ['d', 'e', 'f']
assert get_letter_strings('23') == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
