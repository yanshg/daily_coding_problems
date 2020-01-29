#!/usr/bin/python

"""

This problem was asked by Facebook.

Given a string of parentheses, find the balanced string that can be produced from it using the minimum number of insertions and deletions. If there are multiple solutions, return any of them.

For example, given "(()", you could return "(())". Given "))()(", you could return "()()()()".

"""

# Idea:  Use dynamic and recursion programming
#
#        Intermediate state: first character + remaining string
#
#        Base case: 1. the string become empty
#                   2. the first char is '('
#                   3. the first char is ')'

def helper(s, stack=[], balanced=''):
    if not s:
        return balanced + (')' * len(stack))

    c,remain=s[0],s[1:]

    # first char is ')'
    if c==')':
        if stack and stack[-1]=='(':
            stack.pop()
            return helper(remain,stack.copy(),balanced+c)
        else:
            return helper(remain,stack.copy(),balanced+'()')

    # first char is '('
    stack.append(c)
    return helper(remain,stack.copy(),balanced+c)

def balance_parentheses(s):
    return helper(s,[],'')

assert balance_parentheses("(()")=="(())"
assert balance_parentheses("))()(")=="()()()()"
