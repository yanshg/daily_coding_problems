#!/usr/bin/python

"""

This problem was asked by Apple.

Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) data structure with the following methods: enqueue, which inserts an element into the queue, and dequeue, which removes it.

"""

class Queue:
    def __init__(self):
        self.in_stack=[]
        self.out_stack=[]

    def enqueue(self, val):
        self.in_stack.append(val)

    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()

q=Queue()
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
assert q.dequeue()==2
assert q.dequeue()==3

q.enqueue(5)
q.enqueue(6)

assert q.dequeue()==4
assert q.dequeue()==5
assert q.dequeue()==6

try:
    q.dequeue()
except IndexError as e:
    print(e)
