#!/usr/bin/python

"""
This problem was asked by Microsoft.

Implement 3 stacks using a single list:

class Stack:
    def __init__(self):
        self.list = []

    def pop(self, stack_number):
        pass

    def push(self, item, stack_number):
        pass
"""

# Need discuss with interviewer about how to organize the list

# Good solution: http://codercareer.blogspot.com/2013/02/no-39-stacks-sharing-array.html
#
# Idea:
# 1. Have another array with same size to record this item's previous one's position, just like blockchain.
# 2. Have pointer for the top position for the 3 stack and free stack.
# 3. Initialize the additional array as 1, 2, ..., -1

class Stack:
    def __init__(self, capacity, stack_count=3):
        self.list=['']*capacity
        self.pointer_chain=[1]*capacity
        for i in range(capacity-1):
            self.pointer_chain[i]=i+1
        self.pointer_chain[capacity-1]=-1

        self.stack_count=stack_count
        self.stack_pointer=[-1]*stack_count
        self.free_pointer=0

    def __repr__(self):
        return "list: " + str(self.list) + " pointer_chain:" + str(self.pointer_chain)

    def validate_if_full(self):
        if self.free_pointer==-1:
            raise IndexError("Stack full")

    def validate_stack_id(self, stack_id):
        if stack_id<0 or stack_id > self.stack_count-1:
            raise IndexError("Stack id out of index")

    def validate_if_empty_stack(self, stack_id):
        if self.stack_pointer[stack_id]==-1:
            raise IndexError("Stack is empty")

    def push(self, item, stack_id):
        self.validate_if_full()
        self.validate_stack_id(stack_id)

        stack_p=self.stack_pointer[stack_id]

        # push in free position
        free_p=self.free_pointer
        self.list[free_p]=item
        self.stack_pointer[stack_id]=free_p

        # Update free pointer and stack chain
        self.free_pointer=self.pointer_chain[free_p]
        self.pointer_chain[free_p]=stack_p

    def pop(self, stack_id):
        self.validate_stack_id(stack_id)
        self.validate_if_empty_stack(stack_id)

        stack_p=self.stack_pointer[stack_id]

        # put back to free chain
        free_p=self.free_pointer
        self.free_pointer=stack_p
        self.pointer_chain[stack_p]=free_p

        # Update stack chain
        self.stack_pointer[stack_id]=self.pointer_chain[stack_p]

        return self.list[stack_p]

s=Stack(20,3)

s.push('a',0)
s.push('b',1)
s.push('c',2)

print(s)

assert s.pop(1)=='b'

print(s)

s.push('d',0)
s.push('e',0)

print(s)
assert s.pop(0)=='e'

print(s)
