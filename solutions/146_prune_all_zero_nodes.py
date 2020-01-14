#!/usr/bin/python

"""
This question was asked by BufferBox.

Given a binary tree where all nodes are either 0 or 1, prune the tree so that subtrees containing all 0s are removed.

For example, given the following tree:

   0
  / \
 1   0
    / \
   1   0
  / \
 0   0

should be pruned to:

   0
  / \
 1   0
    /
   1

We do not remove the tree at the root or its left child because it still has a 1 as a descendant.
"""

class Node:
    def __init__(self,val,left=None,right=None):
        self.val=1 if val else 0
        self.left=left
        self.right=right

    def __repr__(self):
        return "{}->({},{})".format(self.val,self.left,self.right)

def prune_nodes(root):
    if not root:
        return None

    if root.left:
        root.left=prune_nodes(root.left)

    if root.right:
        root.right=prune_nodes(root.right)

    if not root.left and not root.right and not root.val:
        return None

    return root

node1=Node(0)
node2=Node(1)
node3=Node(0)
node4=Node(1)
node5=Node(0)
node6=Node(0)
node7=Node(0)

node1.left=node2
node1.right=node3
node3.left=node4
node3.right=node5

node5.left=node6
node5.right=node7

print(node1)
print(prune_nodes(node1))
