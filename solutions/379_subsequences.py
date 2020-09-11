#!/usr/bin/python

"""

This problem was asked by Microsoft.

Given a string, generate all possible subsequences of the string.

For example, given the string xyz, return an array or set with the following strings:


x
y
z
xy
xz
yz
xyz

Note that zx is not a valid subsequence since it is not in the order of the given string.

"""

# Idea: Recursion
#
#         subseqs(S, i) = { S[i] } | { a+S[i] for a in subseqs(S,i-1) } | subseqs(S, i-1)
#         subseqs(S, 0) = { S[0] }
#
# Result: subseqs(S, len(S)-1)

def helper(S, i):
    if i == 0: return { S[0] }

    subs = helper(S,i-1)
    return subs | { S[i] } | { a+S[i] for a in subs }

def subseqs(S):
    return helper(S, len(S)-1)

assert subseqs('xyz') == { 'x', 'y', 'z', 'xy', 'xz', 'yz', 'xyz' }

