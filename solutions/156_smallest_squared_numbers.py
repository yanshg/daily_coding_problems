#!/usr/bin/python

"""

This problem was asked by Facebook.

Given a positive integer n, find the smallest number of squared integers which sum to n.

For example, given n = 13, return 2 since 13 = 3**2 + 2**2 = 9 + 4.

Given n = 27, return 3 since 27 = 3**2 + 3**2 + 3**2 = 9 + 9 + 9.

"""

# Recursion with memory from top to bottom
def get_smallest_squared_integers(n,memo=dict()):
    if n<=3:
        return n
    if n not in memo:
        res = n
        i = 1
        while i*i <= n:
            res = min(res, 1 + get_smallest_squared_integers(n-i*i, memo))
            i += 1
        memo[n] = res
    return memo[n]

# Also can use DP table from bottom to top.
#
# DP[i]: means smallest squared integers for target i
# results: DP[n]

assert get_smallest_squared_integers(13)==2
assert get_smallest_squared_integers(27)==3
