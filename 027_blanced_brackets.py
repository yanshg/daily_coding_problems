#!/usr/bin/python

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
