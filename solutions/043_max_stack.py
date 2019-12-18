#!/usr/bin/python

"""

This problem was asked by Amazon.

Implement a stack that has the following methods:

    push(val), which pushes an element onto the stack
    pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
    max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.

Each method should run in constant time.

"""

# Idea: It will raise an exception if run pop() or get element of '-1' index on an empty list

class MaxStack:
    def __init__(self):
        self.stack=list()
        self.maxstack=list()

    def push(self,val):
        self.stack.append(val)
        self.maxstack.append(max(val,self.max()) if self.maxstack else val)

    def pop(self):
        self.maxstack.pop()
        return self.stack.pop()

    def max(self):
        return self.maxstack[-1]

maxstack=MaxStack()
maxstack.push(2)
maxstack.push(0)
maxstack.push(1)
assert maxstack.pop() == 1
assert maxstack.max() == 2
