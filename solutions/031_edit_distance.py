#!/usr/bin/python

"""
This problem was asked by Google.

The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.
"""

def edit_distance(s, t, debt=0):
    if (not s or not t):
        return len(s)+len(t)+debt
    i=edit_distance(s[1:], t, debt+1)
    d=edit_distance(s, t[1:], debt+1)
    e=edit_distance(s[1:], t[1:], debt+(s[0] != t[0]))
    return min(i,d,e)

assert edit_distance('kitten', 'sitting')==3
assert edit_distance('black', 'white')==5
