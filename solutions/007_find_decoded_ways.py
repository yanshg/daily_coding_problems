#!/usr/bin/python

"""
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be encoded.

For example, the message '111' would give 3, since it could be encoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""


# Idea: need memorize.
#

def encode_ways(s):
    if s and s.startswith('0'):
        return 0

    if len(s)<=1:
        return 1
    
    ways=encode_ways(s[1:])
    if int(s[:2])<26:
        ways+=encode_ways(s[2:])

    return ways

# In above implementation, encode_ways(s[2:]) was called twice by encode_ways(s) and encode_ways(s[1:])
#
# Need memorize

from collections import defaultdict

def helper(s,n,index,cache):
    if index in cache:
        return cache[index]

    if index<n and s[index]=='0':
        return 0

    if index>=n-1:
        return 1

    ways=helper(s,n,index+1,cache)
    if int(s[index:index+2])<26:
        ways+=helper(s,n,index+2,cache)
    cache[index]=ways

    #print("index:",index, "cached ways:",ways)
    return ways

def encode_ways_cache(s):
    cache=defaultdict(int)
    n=len(s)
    return helper(s,n,0,cache)


assert encode_ways('81') == 1
assert encode_ways('11') == 2
assert encode_ways('111') == 3
assert encode_ways('1111') == 5
assert encode_ways('1311') == 4
assert encode_ways('001')==0

assert encode_ways_cache('81') == 1
assert encode_ways_cache('11') == 2
assert encode_ways_cache('111') == 3
assert encode_ways_cache('1111') == 5
assert encode_ways_cache('1311') == 4
assert encode_ways_cache('001')==0
