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

assert get_recurring_char('acbbac')=='b'
assert not get_recurring_char('abcdef')

