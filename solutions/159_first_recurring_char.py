#!/usr/bin/python

"""
This problem was asked by Google.

Given a string, return the first recurring character in it, or null if there is no recurring character.

For example, given the string "acbbac", return "b". Given the string "abcdef", return null.

"""

def get_recurring_char(string):
    exists=set()
    for ch in string:
        if ch in exists:
            return ch
        exists.add(ch)
    return None

# a integer has 4 bytes, totally 32 bits.
def get_recurring_char1(string):
    checker=0
    for i,c in enumerate(string):
        bit=ord(c) - ord('a')
        if checker&(1<<bit):
            return c
        checker |= (1<<bit)
    return None

assert get_recurring_char('acbbac')=='b'
assert get_recurring_char1('acbbac')=='b'
assert not get_recurring_char('abcdef')

