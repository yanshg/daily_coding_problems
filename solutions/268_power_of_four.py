#!/usr/bin/python

"""

This problem was asked by Indeed.

Given a 32-bit positive integer N, determine whether it is a power of four in faster than O(log N) time.

"""

# Idea:  https://stackoverflow.com/a/19611541/8650340

def is_power_of_four(n):
    return (n&(n-1)==0 and n%3==1)
    #return (n&(-n) & 0x55555554) == n

assert is_power_of_four(4)
assert not is_power_of_four(8)
assert is_power_of_four(16)
assert not is_power_of_four(17)
