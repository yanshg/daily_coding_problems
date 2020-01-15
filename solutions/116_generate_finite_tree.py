#!/usr/bin/python

"""
This problem was asked by Jane Street.

Generate a finite, but an arbitrarily large binary tree quickly in O(1).

That is, generate() should return a tree whose size is unbounded but finite.
"""

import random

class Node:
    def __init__(self,val=1,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
        self.is_left_evaluated=False
        self.is_right_evaluated=False

    def __repr__(self):
        return "{}=>({},{})".format(self.val,self.left,self.right)

    def generate_left(self):
        if not self.is_left_evaluated:
            if random.random() < 0.5:
                self.left=Node()
            self.is_left_evaluated=True
        return self.left

    def generate_right(self):
        if not self.is_right_evaluated:
            if random.random() > 0.5:
                self.right=Node()
            self.is_right_evaluated=True
        return self.right

def traverse(node):
    if node==None:
        return None

    traverse(node.generate_left())
    traverse(node.generate_right())
    return node

def generate():
    return traverse(Node())

print(generate())
print(generate())
print(generate())
