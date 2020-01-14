#!/usr/bin/python

"""
This problem was asked by Google.

Find the minimum number of coins required to make n cents.

You can use standard American denominations, that is, 1c, 5c, 10c, and 25c.

For example, given n = 16, return 3 since we can make it with a 10c, a 5c, and a 1c.
"""

def get_min_coins(n):
    coins=0
    bases=[25,10,5,1]
    for base in bases:
        num=n//base
        n-=num*base
        coins+=num
    return coins

assert get_min_coins(16)==3

# Using Dynamic programming methods

def get_min_coins_dp(n,bases=[]):
    if not bases:
        return 0
    base=bases[0]
    coins=n//base
    remain=n-base*coins
    return coins+get_min_coins_dp(remain,bases[1:])

assert get_min_coins_dp(16,[25,10,5,1])==3
