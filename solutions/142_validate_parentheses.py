#!/usr/bin/python

"""
This problem was asked by Google.

You're given a string consisting solely of (, ), and *. * can represent either a (, ), or an empty string. Determine whether the parentheses are balanced.

For example, (()* and (*) are balanced. )*( is not balanced.
"""

# Idea:  put checked string in stack(), handle '*' case in remaining.
#        Handle only one character in each DP sub calling

def validate_parentheses(string,stack=list()):
    if not string and not stack:
        return True
    elif not string:
        return False

    ch=string[0]
    remain=string[1:]
    s=stack.copy();

    if ch=='*':
        return validate_parentheses('('+remain,s) or \
               validate_parentheses(')'+remain,s) or \
               validate_parentheses(remain,s)

    if ch==')' and not s:
        return False
    elif ch==')' and s[-1]=='(':
        s.pop()
    else:
        s.append(ch)

    return validate_parentheses(remain,s)

assert validate_parentheses("(()*")
assert validate_parentheses("(())")
assert validate_parentheses("((*)")
assert validate_parentheses("((**")
assert validate_parentheses("(*)")
assert not validate_parentheses(")*(")

