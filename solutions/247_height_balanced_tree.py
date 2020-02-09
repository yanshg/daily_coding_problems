#!/usr/bin/python

"""

This problem was asked by PayPal.

Given a binary tree, determine whether or not it is height-balanced. A height-balanced binary tree can be defined as one in which the heights of the two subtrees of any node never differ by more than one.

"""

class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

    def __repr__(self):
        return "{}->({},{})".format(self.val,self.left,self.right)


def helper(root,height=0):
    if not root:
        return height,True

    if not root.left and not root.right:
        return height,True

    left_height,is_left_balanced=helper(root.left,height+1)
    right_height,is_right_balanced=helper(root.right,height+1)

    larger,smaller=(left_height,right_height) if left_height>right_height else (right_height,left_height)

    if is_left_balanced and is_right_balanced and larger-smaller<=1:
        return larger,True

    return larger,False


def is_height_balanced(root):
    _,is_height_balanced=helper(root,0)
    return is_height_balanced

"""
         1
       /   \
      2     3
    /   \    
   4     5   

"""

n1=Node(1)
n2=Node(2)
n3=Node(3)
n4=Node(4)
n5=Node(5)
n1.left=n2
n1.right=n3
n2.left=n4
n2.right=n5

assert is_height_balanced(n1)

n6=Node(6)
n4.right=n6
assert not is_height_balanced(n1)
