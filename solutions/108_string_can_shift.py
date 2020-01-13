#!/usr/bin/python

"""
This problem was asked by Google.

Given two strings A and B, return whether or not A can be shifted some number of times to get B.

For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb, return false.
"""

def can_shift(str1,str2):
    return str1 and str2 and \
           len(str1)==len(str2) and \
           str2 in str1*2

assert can_shift("abcde","cdeab")
assert not can_shift("abc","acb")

