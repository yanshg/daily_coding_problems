#!/usr/bin/python

"""
This problem was asked by Google.

Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.

For example, given the following preorder traversal:

[a, b, d, e, c, f, g]

And the following inorder traversal:

[d, b, e, a, f, c, g]

You should return the following tree:

    a
   / \
  b   c
 / \ / \
d  e f  g

"""

class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

    def __repr__(self):
        return "{}->({},{})".format(self.val,self.left,self.right)

def construct_tree(preorder,inorder):
    if not preorder and not inorder:
        return None

    val=preorder[0]
    root=Node(val)
    if len(preorder)==1:
        return root

    i=inorder.index(val)
    root.left=construct_tree(preorder[1:i+1],inorder[:i])
    root.right=construct_tree(preorder[i+1:],inorder[i+1:])
    return root

tree = construct_tree(preorder=['a', 'b', 'd', 'e', 'c', 'f', 'g'],
                      inorder=['d', 'b', 'e', 'a', 'f', 'c', 'g'])
assert tree.val == 'a'
assert tree.left.val == 'b'
assert tree.left.left.val == 'd'
assert tree.left.right.val == 'e'
assert tree.right.val == 'c'
assert tree.right.left.val == 'f'
assert tree.right.right.val == 'g'

tree = construct_tree(preorder=['a', 'b', 'd', 'e', 'c', 'g'],
                      inorder=['d', 'b', 'e', 'a', 'c', 'g'])
assert tree.val == 'a'
assert tree.left.val == 'b'
assert tree.left.left.val == 'd'
assert tree.left.right.val == 'e'
assert tree.right.val == 'c'
assert tree.right.right.val == 'g'
