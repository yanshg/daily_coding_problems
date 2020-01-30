#!/usr/bin/python

"""

This problem was asked by Amazon.

Given a complete binary tree, count the number of nodes in faster than O(n) time. Recall that a complete binary tree has every level filled except the last, and the nodes in the last level are filled starting from the left.

"""

class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

    def __repr__(self):
        return "{}->({}, {})".format(self.val,self.left,self.right)

def count_nodes(root):
    if not root:
        return 0

    return 1 + count_nodes(root.left) + count_nodes(root.right) 

def get_left_height(root):
    height=0
    while root:
        root=root.left
        height+=1
    return height

def get_right_height(root):
    height=0
    while root:
        root=root.right
        height+=1
    return height

def count_bst_nodes(root):
    if not root:
        return 0

    lh=get_left_height(root)
    rh=get_right_height(root)
    if lh==rh:
        return (1<<lh)-1

    return 1+count_bst_nodes(root.left)+count_bst_nodes(root.right)



"""
           1
         /   \
       2       3
     /   \   /   \
    4    5  6     7
   /
  8

"""

n1=Node(1)
n2=Node(2)
n3=Node(3)
n4=Node(4)
n5=Node(5)
n6=Node(6)
n7=Node(7)
n8=Node(8)

n1.left=n2
n1.right=n3
n2.left=n4
n2.right=n5
n3.left=n6
n3.right=n7
n4.left=n8

assert count_nodes(n1)==8
assert count_bst_nodes(n1)==8

