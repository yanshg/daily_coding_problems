#!/usr/bin/python

"""
This problem was asked by Google.

Given a stack of N elements, interleave the first half of the stack with the second half reversed using only one other queue. This should be done in-place.

Recall that you can only push or pop from a stack, and enqueue or dequeue from a queue.

For example, if the stack is [1, 2, 3, 4, 5], it should become [1, 5, 2, 4, 3]. If the stack is [1, 2, 3, 4], it should become [1, 4, 2, 3].

Hint: Try working backwards from the end state.

"""

from collections import deque

def interleave_stack(s,dq,index=1):
    l=len(s)
    if index==l:
        return s

    for i in range(l-index):
        dq.append(s.pop())

    while dq:
        s.append(dq.popleft())

    return interleave_stack(s,dq,index+1)

dq=deque()

assert interleave_stack([1, 2, 3, 4, 5, 6, 7, 8, 9],dq,1) == [1, 9, 2, 8, 3, 7, 4, 6, 5 ]
assert interleave_stack([1, 2, 3, 4, 5],dq,1) == [1, 5, 2, 4, 3]
assert interleave_stack([1, 2, 3, 4],dq,1) == [1, 4, 2, 3]
