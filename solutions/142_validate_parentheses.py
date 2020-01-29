#!/usr/bin/python

"""

This problem was asked by Google.

You're given a string consisting solely of '(', ')', and '*'. * can represent either a (, ), or an empty string. Determine whether the parentheses are balanced.

For example, '(()*' and '(*)' are balanced. ')*(' is not balanced.

"""

# Idea:  put checked string in stack(), handle '*' case in remaining.
#        Handle only one character in each DP sub calling

def validate_parentheses_helper(string,stack=list()):
    if not string:
        return not stack

    ch,remain=string[0],string[1:]
    s=stack.copy();

    if ch=='*':
        return validate_parentheses_helper('('+remain,s) or \
               validate_parentheses_helper(')'+remain,s) or \
               validate_parentheses_helper(remain,s)

    if ch==')' and not s:
        return False
    elif ch==')' and s[-1]=='(':
        s.pop()
    else:
        s.append(ch)

    return validate_parentheses_helper(remain,s)

def validate_parentheses(string):
    return validate_parentheses_helper(string,[])

assert validate_parentheses("(()*")
assert validate_parentheses("(())")
assert validate_parentheses("((*)")
assert validate_parentheses("((**")
assert validate_parentheses("(*)")
assert not validate_parentheses(")*(")

