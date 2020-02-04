#!/usr/bin/python

"""

This problem was asked by Quora.

Given an absolute pathname that may have . or .. as part of it, return the shortest standardized path.

For example, given "/usr/bin/../bin/./scripts/../", return "/usr/bin/".

"""

def get_absolute_path(path):
    stack=[]
    for dir in path.split('/'):
        if dir=='..' and stack:
           stack.pop()
        elif dir=='.':
           continue
        else:
           stack.append(dir)
    return '/'.join(stack)

assert get_absolute_path("/usr/bin/../bin/./scripts/../")=="/usr/bin/"
