#!/usr/bin/python

"""
This problem was asked by Microsoft.

Print the nodes in a binary tree level-wise. For example, the following should print 1, 2, 3, 4, 5.

  1
 / \
2   3
   / \
  4   5

"""

from collections import deque

class Node():
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

    def __repr__(self):
        return "{}->({},{})".format(self.val,self.left,self.right)


def print_tree_with_level(root):
    dq=deque([root])
    while dq:
        node=dq.popleft()
        print(node.val)
        if node.left:
            dq.append(node.left)
        if node.right:
            dq.append(node.right)


node1=Node(1)
node2=Node(2)
node3=Node(3)
node4=Node(4)
node5=Node(5)

node1.left=node2
node1.right=node3
node3.left=node4
node3.right=node5

print(node1)
print_tree_with_level(node1)
