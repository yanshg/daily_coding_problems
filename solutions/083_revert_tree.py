#!/usr/bin/python

"""
This problem was asked by Google.

Invert a binary tree.

For example, given the following tree:

    a
   / \
  b   c
 / \  /
d   e f

should become:

  a
 / \
 c  b
 \  / \
  f e  d

"""

class Node():
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

    def __repr__(self):
        return "{}=({},{})".format(self.val, self.left, self.right)

def revert_tree(root):
    if not root:
        return None

    reverted_left=revert_tree(root.left)
    reverted_right=revert_tree(root.right)
    root.left=reverted_right
    root.right=reverted_left
    return root

a=Node('a')
b=Node('b')
c=Node('c')
d=Node('d')
e=Node('e')
f=Node('f')

a.left=b
a.right=c
b.left=d
b.right=e
c.left=f

print "original tree: " + repr(a)

revert_tree(a)

print "reverted tree: " + repr(a)

assert a.left==c
assert a.right==b
assert b.left==e
assert b.right==d
assert c.right==f

