#!/usr/bin/python

"""
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""


def decode_ways(string):
    if not string:
        return 0

    mapping=dict()
    for i in range(1,26):
        mapping[str(i)]=chr(ord('a')+i-1)

    for char in string:
        if char not in mapping:
            return 0

    return helper(string,mapping)

def helper(string,mapping):
    if not string or len(string)==1:
        return 1

    ways=helper(string[1:],mapping);
    if (string[0:2] in mapping):
        ways+=helper(string[2:],mapping)

    return ways

assert decode_ways('81') == 1
assert decode_ways('11') == 2
assert decode_ways('111') == 3
assert decode_ways('1111') == 5
assert decode_ways('1311') == 4
assert decode_ways('001')==0
assert decode_ways('') == 0

