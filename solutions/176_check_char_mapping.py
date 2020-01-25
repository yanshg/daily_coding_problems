#!/usr/bin/python

"""
This problem was asked by Bloomberg.

Determine whether there exists a one-to-one character mapping from one string s1 to another s2.

For example, given s1 = abc and s2 = bcd, return true since we can map a to b, b to c, and c to d.

Given s1 = foo and s2 = bar, return false since the o cannot map to two characters.

"""

# Idea 1: Use dynamic programming

def helper(s1,s2,hashmap={}):
    if not s1 or not s2:
        return not s1 and not s2

    c1,c2=s1[0],s2[0]
    if c1 not in hashmap:
        hashmap[c1]=c2
    elif hashmap[c1]!=c2:
        return False

    return helper(s1[1:],s2[1:],hashmap)

def check_char_mapping1(s1,s2):
    return helper(s1,s2,{})


# Idea 2:  Do not use dynamic programming
#
#          use zip() to get the character pair

def check_char_mapping2(s1,s2):
    if len(s1) != len(s2):
        return False

    hashmap=dict()
    for c1,c2 in zip(s1,s2):
        if c1 not in hashmap:
            hashmap[c1]=c2
        elif hashmap[c1]!=c2:
            return False

    return True

assert check_char_mapping1('abc','bcd')
assert not check_char_mapping1('foo','bar')

assert check_char_mapping2('abc','bcd')
assert not check_char_mapping2('foo','bar')
