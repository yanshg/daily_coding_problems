#!/usr/bin/python

"""
This problem was asked by Amazon.

Implement a stack API using only a heap. A stack implements the following methods:

    push(item), which adds an element to the stack
    pop(), which removes and returns the most recently added element (or throws an error if there is nothing on the stack)

Recall that a heap has the following operations:

    push(item), which adds a new key to the heap
    pop(), which removes and returns the max value of the heap
"""

import sys, heapq

class HeapStack:
    def __init__(self):
        self.counter=sys.maxsize
        self.stack=[]

    def push(self,val):
        heapq.heappush(self.stack,(self.counter,val))
        self.counter-=1

    def pop(self):
        if not self.stack:
            return None

        self.counter,val=heapq.heappop(self.stack)
        return val

hs=HeapStack()
hs.push(1)
hs.push(4)
hs.push(3)

assert hs.pop()==3
assert hs.pop()==4

hs.push(3)
assert hs.pop()==3
assert hs.pop()==1

assert not hs.pop()
