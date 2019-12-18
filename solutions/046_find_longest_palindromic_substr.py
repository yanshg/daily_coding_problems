#!/usr/bin/python

"""

This problem was asked by Amazon.

Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum length, return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic substring of "bananas" is "anana".

"""

def is_palindrome(s):
    return s==s[::-1]

def get_longest_palindromic_substr(string):
    if not string or is_palindrome(string):
        return string

    return max([get_longest_palindromic_substr(string[1:]),
                get_longest_palindromic_substr(string[:-1])],
               key=len)

assert get_longest_palindromic_substr("aabcdcb")=="bcdcb"
assert get_longest_palindromic_substr("bananas")=="anana"
