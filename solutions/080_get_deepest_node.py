#!/usr/bin/python


"""
This problem was asked by Google.

Given the root of a binary tree, return a deepest node. For example, in the following tree, return d.

    a
   / \
  b   c
 /
d
"""

class Node():
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

    def __repr__(self):
        return "{}: ({}, {})".format(self.val,self.left,self.right)

def helper(node,depth):
    if not node.left and not node.right:
        return (node,depth)

    left_node,left_depth=(node,depth) if not node.left else helper(node.left,depth+1) 
    right_node,right_depth=(node,depth) if not node.right else helper(node.right,depth+1) 

    return (left_node,left_depth) if left_depth>=right_depth else (right_node,right_depth)

def get_deepest_node(node):
    return helper(node,0)[0]

a=Node('a')
b=Node('b')
c=Node('c')
d=Node('d')
e=Node('e')
f=Node('f')
g=Node('g')

a.left=b
a.right=c
b.left=d

assert get_deepest_node(a)==d

c.right=e
e.right=f
assert get_deepest_node(a)==f

