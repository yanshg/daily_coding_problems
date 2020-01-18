#!/usr/bin/python

"""
This problem was asked by Amazon.

Given a string, determine whether any permutation of it is a palindrome.

For example, carrace should return true, since it can be rearranged to form racecar, which is a palindrome. daily should return false, since there's no rearrangement that can form a palindrome.

"""

# Idea: A set of characters can form a palindrome
#       if at most one character occurs odd number of times
#       and all characters occur even number of times.

def check_permutation_palindrome(string):
    chars = set()
    for c in string:
        if c not in chars:
            chars.add(c)
        else:
            chars.remove(c)

    return len(chars) < 2

assert check_permutation_palindrome('racecar')
assert not check_permutation_palindrome('daily')
