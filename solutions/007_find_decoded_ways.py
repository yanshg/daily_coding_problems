#!/usr/bin/python

"""
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be encoded.

For example, the message '111' would give 3, since it could be encoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""


# Idea: need memorize.
#

def encode_ways_dp(s):
    if not s:
        return 1

    if s.startswith('0'):
        return 0

    if len(s)==1:
        return 1
    
    total=encode_ways_dp(s[1:])
    if int(s[:2])<26:
        total+=encode_ways_dp(s[2:])

    return total

assert encode_ways('81') == 1
assert encode_ways('11') == 2
assert encode_ways('111') == 3
assert encode_ways('1111') == 5
assert encode_ways('1311') == 4
assert encode_ways('001')==0

