#!/usr/bin/python

"""
This problem was asked by Amazon.

Given a node in a binary search tree, return the next bigger element, also known as the inorder successor.

For example, the inorder successor of 22 is 30.

   10
  /  \
 5    30
     /  \
   22    35

You can assume each node has a parent pointer.

"""

import bisect

class Node:
    def __init__(self,val,left=None,right=None,parent=None):
        self.val=val
        self.left=left
        self.right=right
        self.parent=parent

    def __repr__(self):
        return "{}=>({},{})".format(self.val,self.left,self.right)

# Issues:
#  1. The nodes may have same value.
#  2. The parent node's value may greater or less than the children's value
#
# So it is NOT possible to search the binary tree and get the inorder successor.
#
# The solution:
#  1. Get the root node
#  2. Traverse the tree and get the list
#  3. use bisect to get the inorder successor

def get_root(node):
    while node.parent:
        node=node.parent
    return node

def get_list(root):
    if not root:
        return []

    return get_list(root.left) + [ root.val ] + get_list(root.right)

def get_successor(node,val):
    nums=get_list(get_root(node))
    i=bisect.bisect_right(nums,val)
    if i<len(nums):
        return nums[i]
    return None


node1=Node(5)
node2=Node(10)
node3=Node(22)
node4=Node(30)
node5=Node(35)

node1.parent=node2

node2.left=node1
node2.right=node4

node3.parent=node4

node4.left=node3
node4.right=node5
node4.parent=node2

node5.parent=node4
print(node2)

assert get_successor(node2, 3)==5
assert get_successor(node2, 5)==10
assert get_successor(node2, 7)==10
assert get_successor(node2, 10)==22
assert get_successor(node2, 11)==22
assert get_successor(node2, 22)==30
assert get_successor(node2, 35)==None

assert get_successor(node5, 3)==5
assert get_successor(node5, 5)==10
assert get_successor(node5, 7)==10
assert get_successor(node5, 10)==22
assert get_successor(node5, 11)==22
assert get_successor(node5, 22)==30
assert get_successor(node5, 35)==None

