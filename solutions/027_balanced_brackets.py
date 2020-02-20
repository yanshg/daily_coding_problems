#!/usr/bin/python

"""

This problem was asked by Facebook.

Gqiven a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.

"""

brackets='()[]{}'

brackets_map = {
  ')': '(',
  ']': '[',
  '}': '{',
}

def is_balanced(str):
    stack=list();
    for char in str:
        if not char in brackets:
           continue
        elif char in brackets_map and stack and stack[-1]==brackets_map[char]:
           stack.pop()
        else:
           stack.append(char)
    return not stack

assert is_balanced("([ab])[c]({d})")
assert is_balanced("(abcde)")
