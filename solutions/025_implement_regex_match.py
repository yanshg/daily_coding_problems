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

# Idea: Use recursion
#
#       Base cases: 1. zero length of regex
#                   2. zero length of string
#                   3. if first char in regex is '*', recursionly match * with zero or first 1 character in string.
#                   4. first char is match, check remaining chars

# O(2^n)
def is_match(regex,string):
    if not regex:
        return not string

    if not string:
        return bool(regex=='*'*len(regex))

    if regex[0] == '*':
        # regex[0] consumes no characters or
        # regex[0] consumes one character
        return is_match(regex[1:], string) or is_match(regex,string[1:])

    elif regex[0] in { string[0], '.' }:
        return is_match(regex[1:], string[1:])

    return False


# Idea: Use DP table

# DP[i][j]: True if match regex[:i+1] and string[:j+1] else False
#
# DP[i][j] = |- DP[i-1][j] or DP[i][j-1]  if regex[i] == '*'
#            |- DP[i-1[j-1]               if regex[i] in [ '.', string[j] ]
#
# r' = '' + r
# s' = '' + s
# match(r', s') = match(r, s)
#
#            |- True                      if i==0 and j==0
#            |- False                     if (i==0 and j>0) or (i>0 and j==0)
# DP[i][j] = |- DP[i-1][j] or DP[i][j-1]  if regex[i-1] == '*'
#            |- DP[i-1[j-1]               if regex[i-1] in [ '.', string[j-1] ]

# O(m*n)
def is_match_dp(regex, string):
    m = len(regex)
    n = len(string)
    DP = [ [ False for j in range(n+1) ] for i in range(m+1) ]

    # Handle base case that string is null
    for i in range(1,m+1):
        if regex[i-1] == '*':
            DP[i][0] = DP[i-1][0]

    for i in range(1,m+1):
        for j in range(1,n+1):
            if regex[i-1] == '*':
                DP[i][j] = DP[i-1][j] or DP[i][j-1]
            elif regex[i-1] in [ '.', string[j-1] ]:
                DP[i][j] = DP[i-1][j-1]

    return DP[-1][-1]

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

assert is_match_dp(r'ra.', 'ray')
assert not is_match_dp(r'ra.', 'raymond')
assert is_match_dp(r'*at', 'chat')
assert is_match_dp(r'*chat', 'chat')
assert is_match_dp(r'.*at', 'chat')
assert is_match_dp(r'c*hat', 'chat')
assert is_match_dp(r'.*hat', 'chat')
assert is_match_dp(r'*', 'chat')
assert is_match_dp(r'**', 'chat')
assert is_match_dp(r'ch*a*t', 'chat')
assert is_match_dp(r'c*a*t', 'chat')
assert not is_match_dp(r'ch*a*ts', 'chat')
