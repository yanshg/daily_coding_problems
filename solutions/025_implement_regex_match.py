#!/usr/bin/python

"""

This problem was asked by Facebook.

Implement regular expression matching with the following special characters:

    . (period) which matches any single character
    * (asterisk) which matches zero or more of the preceding element

That is, implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.

For example, given the regular expression "ra." and the string "ray", your function should return true. The same regular expression on the string "raymond" should return false.

Given the regular expression ".*at" and the string "chat", your function should return true. The same regular expression on the string "chats" should return false.

"""

# Idea: Use danymic programming,
#       Base cases: 1. zero length of regex
#                   2. zero length of string
#                   3. if first char in regex is '*', recursionly match * with zero or first 1 character in string.
#                   4. first char is match, check remaining chars

def is_match(regex,string):
    if not regex:
        return not string

    if not string:
        return True if regex=='*'*len(regex) else False

    if regex[0] == '*':
        # regex[0] consumes no characters or
        # regex[0] consumes one character
        return is_match(regex[1:], string) or is_match(regex,string[1:])

    first_match = regex[0] in {string[0], '.'}
    return first_match and is_match(regex[1:], string[1:])

assert is_match(r'ra.', 'ray')
assert not is_match(r'ra.', 'raymond')
assert is_match(r'*at', 'chat')
assert is_match(r'*chat', 'chat')
assert is_match(r'.*at', 'chat')
assert is_match(r'c*hat', 'chat')
assert is_match(r'.*hat', 'chat')
assert is_match(r'*', 'chat')
assert is_match(r'**', 'chat')
assert is_match(r'ch*a*t', 'chat')
assert is_match(r'c*a*t', 'chat')
assert not is_match(r'ch*a*ts', 'chat')
assert not is_match(r'.*at', 'chats')

