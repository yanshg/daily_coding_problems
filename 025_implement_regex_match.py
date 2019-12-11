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
#                   3. first char is match, check remaining chars
#                   4. if first char in regex is '*', replace '*' with some numbers of '.'

def first_match(regex,string):
    return regex[0]==string[0] or (regex[0]=='.' and bool(string))

def is_match(regex,string):
    if not regex:
        return not string

    if not string:
        if regex == '*' * len(regex):
            return True
        return False

    # len(regex)>0 and len(string)>0
    if first_match(regex,string):
        return is_match(regex[1:],string[1:])

    # first char is not match, check '*' cases to replace '*' with multiple '.'
    if regex[0]=='*':
        # remove * in regex to get how many '.' need be used.
        # can use "re.sub(r'\*',r'',string)" to remove '*' in the string.
        regex_without_star=''.join([ e for e in regex if e!='*' ])
        lr,ls=len(regex_without_star),len(string)
        if (lr>ls):
            return False

        for num_dots in range(ls-lr+1):
            new_regex='.'*num_dots + regex[1:]
            if is_match(new_regex,string):
                return True

    return False

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

