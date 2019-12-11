#!/usr/bin/python

"""

This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1

"""

# Notes: have same operation on each node

class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

    def __repr__(self):
        return "{}->({}, {})".format(self.val,self.left,self.right)

def is_unival_tree(node):
    if not node:
        return True

    if (node.left and node.val != node.left.val) or \
       (node.right and node.val != node.right.val):
        return False

    return is_unival_tree(node.left) and is_unival_tree(node.right)

def helper(node):
    if not node:
        return True, 0

    is_left_unival,left_num=helper(node.left)
    is_right_unival,right_num=helper(node.right)

    total=left_num+right_num

    if is_left_unival and is_right_unival:
        if (node.left and node.val != node.left.val) or \
           (node.right and node.val != node.right.val):
            return False, total
        return True, total+1

    return False, total

def get_unival_tree_num(node):
    _,num=helper(node)
    return num

node1=Node('a')
node2=Node('a')
node3=Node('b')
node4=Node('b')
node5=Node('b')
node6=Node('b')
node7=Node('b')

node1.left=node2
node1.right=node3
node3.left=node4
node3.right=node5
node5.left=node6
node5.right=node7

print(node1)

assert is_unival_tree(node2)
assert is_unival_tree(node3)
assert is_unival_tree(node5)
assert not is_unival_tree(node1)

assert get_unival_tree_num(node1)==6
