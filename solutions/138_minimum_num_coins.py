#!/usr/bin/python

"""
This problem was asked by Google.

Find the minimum number of coins required to make n cents.

You can use standard American denominations, that is, 1c, 5c, 10c, and 25c.

For example, given n = 16, return 3 since we can make it with a 10c, a 5c, and a 1c.
"""

# Recursion problem issue:
# 1. Find out the transforming pattern,
# 2. Then use memo or DP table.
#
# Transform pattern:  f(n) = min(1+f(n-1), 1+f(n-5), 1+f(n-10), 1+f(n-25))
#                or:  f(n) = 1 + min(f(n-1), f(n-5), f(n-10), f(n-25))
#
#        Base cases:  f(-n) = float('inf')
#                     f(0) = 0


# Idea 1: use memo from top to bottom

def get_min_coins(n, memo=dict()):
    if n<0:
        return float('inf')
    elif n==0:
        return 0

    if n in memo:
        return memo[n]

    memo[n] = 1 + min([ get_min_coins(n-cents) for cents in [1,5,10,25] ])
    return memo[n]

assert get_min_coins(16)==3

# Idea 2: use DP table from bottom to top

#             DP[i]:  means the minimum coins required to take i cents.
#
# Transform pattern:  DP[i] = 1 + min(DP[i-1], DP[i-5], DP[i-10], DP[i-25])
#
#        Base cases:  DP[0] = 0
#
#            Return:  DP[n]

def get_min_coins_dp(n):
    DP = [0] * (n+1)
    for i in range(1,n+1):
        DP[i] = 1 + min([ DP[i-cents] for cents in [1,5,10,25] if i>=cents ])
    return DP[n]

assert get_min_coins(16)==3
assert get_min_coins_dp(16)==3
