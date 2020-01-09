#!/usr/bin/python

"""

This problem was asked by Apple.

Given a tree, find the largest tree/subtree that is a BST.

Given a tree, return the size of the largest tree/subtree that is a BST.

"""

# Idea: To identify if it is a BST tree, we need the following information:
#       1. if left tree is BST,
#       2. left tree's value range (left_minval, left_maxval)
#       3. if right tree is BST,
#       4. right tree's value range (right_minval, right_maxval)
#
#       The helper sub check above information to determine if the whole tree is a BST

class Node():
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

    def __repr__(self):
        return "{}=>({}, {})".format(self.val,self.left,self.right)

def get_largest_bst_tree(node):
    if not node:
        return True,node,0,float('inf'),float('-inf')

    if not node.left and not node.right:
        return True,node,1,node.val,node.val

    left_is_bst,left_bst,left_nodes,left_minval,left_maxval=get_largest_bst_tree(node.left)
    right_is_bst,right_bst,right_nodes,right_minval,right_maxval=get_largest_bst_tree(node.right)

    if left_is_bst and right_is_bst:
        if node.left and node.right:
            if left_maxval <= node.val <= right_minval:
                return (True, node, left_nodes + right_nodes + 1, left_minval, right_maxval)
        elif node.left and node.val >= left_maxval:
            return (True, node, left_nodes + 1, left_minval, node.val)
        elif node.right and node.val <= right_minval:
            return (True, node, right_nodes + 1, node.val, right_maxval)

    if left_nodes > right_nodes:
        return (False, left_bst, left_nodes, left_minval, node.val)
    else:
        return (False, right_bst, right_nodes, node.val, right_maxval)

def get_largest_bst_tree_size(root):
    _,_,size,_,_=get_largest_bst_tree(root)
    return size

"""

Test Tree:

          500
         /   \
       50    150
      /  \
    25   75
   /
 15

"""
a=Node(500)
b=Node(50)
c=Node(150)
d=Node(25)
e=Node(75)
f=Node(15)

a.left=b
a.right=c
b.left=d
b.right=e
d.left=f

assert get_largest_bst_tree_size(a)==4

a.val=100
assert get_largest_bst_tree_size(a)==6
