#!/usr/bin/python

"""

This problem was asked by Microsoft.

Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '−', '*', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

     *
   /   \
  +     +
 / \   / \
3   2 4   5

You should return 45, as it is (3 + 2) * (4 + 5).

"""

class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

    def __repr__(self):
        return "{}->({},{})".format(self.val,self.left,self.right)

def evaluate_tree(root):
    if not root:
        return 0

    if root.val=='+':
        return evaluate_tree(root.left) + evaluate_tree(root.right)
    elif root.val=='-':
        return evaluate_tree(root.left) - evaluate_tree(root.right)
    elif root.val=='*':
        return evaluate_tree(root.left) * evaluate_tree(root.right)
    elif root.val=='/':
        return evaluate_tree(root.left) / evaluate_tree(root.right)

    return int(root.val)


node1=Node('*')
node2=Node('+')
node3=Node('+')
node4=Node('3')
node5=Node('2')
node6=Node('4')
node7=Node('5')

node1.left=node2
node1.right=node3

node2.left=node4
node2.right=node5

node3.left=node6
node3.right=node7

assert evaluate_tree(node1)==45
