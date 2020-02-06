#!/usr/bin/python

"""

This problem was asked by Yahoo.

Recall that a full binary tree is one in which each node is either a leaf node, or has two children. Given a binary tree, convert it to a full one by removing nodes with only one child.

For example, given the following tree:

         0
      /     \
    1         2
  /            \
3                4
  \            /   \
    5         6     7

You should convert it to:

     0
  /     \
5         4
        /   \
       6     7


"""

class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

    def __repr__(self):
        return "{}->({}, {})".format(self.val,self.left,self.right)

def purge_to_full_tree(root):
    if not root:
        return None
    elif not root.left and not root.right:
        return root
    elif root.left and root.right:
        root.left=purge_to_full_tree(root.left)
        root.right=purge_to_full_tree(root.right)
        return root
    elif root.left:
        return purge_to_full_tree(root.left)
    elif root.right:
        return purge_to_full_tree(root.right)

n0=Node(0)
n1=Node(1)
n2=Node(2)
n3=Node(3)
n4=Node(4)
n5=Node(5)
n6=Node(6)
n7=Node(7)

n0.left=n1
n0.right=n2
n1.left=n3
n3.right=n5
n2.right=n4
n4.left=n6
n4.right=n7

n0=purge_to_full_tree(n0)

assert n0.left.val==5
assert n0.right.val==4
assert n0.right.left.val==6
assert n0.right.right.val==7



