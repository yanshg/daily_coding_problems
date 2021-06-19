#!/usr/bin/python

"""

This problem was asked by Google.

A quack is a data structure combining properties of both stacks and queues. It can be viewed as a list of elements written left to right such that three operations are possible:
 - push(x): add a new item `x` to the left end of the list
 - pop(): remove and return the item on the left end of the list
 - pull(): remove the item on the right end of the list.

Implement a quack using three stacks and `O(1)` additional memory, so that the amortized time for any push, pop, or pull operation is `O(1)`.

"""

class Quack:
    def __init__(self):
        self.left=[]
        self.right=[]
        self.buffer=[]

    def push(self,x):
        self.left.append(x)

    def pop(self):
        return self.left.pop()

    def pull(self):
        return self.left.popleft()

q=Quack()
q.push(1)
q.push(2)
q.push(3)
q.push(4)
assert q.pop()==4
assert q.pull()==1
assert q.pop()==3
assert q.pull()==2

try:
    q.pop()
except IndexError as e:
    print(e)

try:
    q.pull()
except IndexError as e:
    print(e)
