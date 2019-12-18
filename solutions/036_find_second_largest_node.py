#!/usr/bin/python

"""
This problem was asked by Dropbox.

Given the root to a binary search tree, find the second largest node in the tree.
"""

class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

    def __repr__(self):
        return "{}->({},{}".format(self.val,self.left,self.right)

def helper(root):
    if not root:
        return None,None

    if not root.left and not root.right:
        return None,root

    if root.right:
        right_second,right_largest=helper(root.right)
        if not right_second:
            right_second=root
        return right_second,right_largest
    elif root.left:
        left_second,left_largest=helper(root.left)
        return left_largest,root

def find_second_largest_node(root):
    second,largest=helper(root)
    return second

node1=Node(1)
node2=Node(2)
node3=Node(3)
node4=Node(4)
node5=Node(5)
node6=Node(6)
node7=Node(7)
node8=Node(8)
node9=Node(9)

node5.left=node4
node5.right=node8

node4.left=node2

node2.left=node1
node2.right=node3

node8.left=node6
node8.right=node9

node6.right=node7

print(node5)

"""
       5
      / \
     4   8
    /   / \
   2   6   9
  / \   \
 1   3   7

"""

assert find_second_largest_node(node8)==node8
