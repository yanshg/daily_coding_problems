#!/usr/bin/python

"""

This problem was asked by Wayfair.

You are given a 2 x N board, and instructed to completely cover the board with the following shapes:

    Dominoes, or 2 x 1 rectangles.
    Trominoes, or L-shapes.

For example, if N = 4, here is one possible configuration, where A is a domino, and B and C are trominoes.

A B B C
A B C C

Given an integer N, determine in how many ways this task is possible.

"""

# Article:  https://cs.stackexchange.com/questions/66658/domino-and-tromino-combined-tiling?answertab=votes#tab-top
#
#
#         |- 0                                 if n==0
#         |- 1                                 if n==1
#  f(n) = |- 2                                 if n==2
#         |- 5                                 if n==3
#         |- f(n-1) + f(n-2) + 2*(sum([f(n-k) for k in range(3,n+1)]) if n>=4
#
#  =>
#
#  f(n) - f(n-1) = f(n-1) + f(n-3)
#
#  =>
#
#  f(n) = 2*f(n-1) + f(n-3)

def get_ways(n):
    if n==0 or n==1: return n
    if n==2: return 2
    if n==3: return 5

    return 2 * get_ways(n-1) + get_ways(n-3)

def get_ways_memo(n, memo=dict()):
    if n==0 or n==1: return n
    if n==2: return 2
    if n==3: return 5

    if n in memo:
        return memo[n]

    memo[n] = 2*get_ways_memo(n-1, memo) + get_ways_memo(n-3, memo)
    return memo[n]

# Use DP table
#
# DP[i]: means ways with i length
#
#          |- 0                         if i==0
#          |- 1                         if i==1
#  DP[i] = |- 2                         if i==2
#          |- 5                         if i==3
#          |- 2 * DP[i-1] + DP[i-3]     if i>=4
#
def get_ways_dp(n):
    DP = [0] * (n+1)
    DP[1] = 1
    DP[2] = 2
    DP[3] = 5

    for i in range(4,n+1):
        DP[i] = 2 * DP[i-1] + DP[i-3]

    return DP[-1]

assert get_ways(4) == 11
assert get_ways_memo(4,{}) == 11
assert get_ways_dp(3) == 5
assert get_ways_dp(4) == 11
