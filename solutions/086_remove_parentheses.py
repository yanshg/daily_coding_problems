#!/usr/bin/python

"""

This problem was asked by Google.

Given a string of parentheses, write a function to compute the minimum number of parentheses to be removed to make the string valid (i.e. each open parenthesis is eventually closed).

For example, given the string "()())()", you should return 1. Given the string ")(", you should return 2, since we must remove all of them.

"""

def remove_parenthesis(string):
    stack=list()
    for char in string:
        if char=='(':
            stack.append(char)
        elif char==')':
            if stack and stack[-1]=='(':
                stack.pop()
            else:
                stack.append(char)
    return len(stack)

assert remove_parenthesis("()())()")==1
assert remove_parenthesis(")(")==2
assert remove_parenthesis(")((")==3
assert remove_parenthesis("))((")==4
assert remove_parenthesis("))()(")==3
assert remove_parenthesis("())()(")==2
    

