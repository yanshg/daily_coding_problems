#!/usr/bin/python

"""
This problem was asked by Google.

Given the sequence of keys visited by a postorder traversal of a binary search tree, reconstruct the tree.

For example, given the sequence 2, 4, 3, 8, 7, 5, you should construct the following tree:

    5
   / \
  3   7
 / \   \
2   4   8

"""

class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

    def __repr__(self):
        return "{}->({},{})".format(self.val,self.left,self.right)

def get_tree(list):
    if not list:
        return None

    rootval=list[-1]

    i,l=0,len(list)
    while i<l-1 and list[i]<=rootval:
        i+=1

    return Node(rootval,get_tree(list[:i]),get_tree(list[i:-1]))

root=get_tree([2, 4, 3, 8, 7, 5])
print(root)
assert root.val==5
assert root.left.val==3
assert root.right.val==7
assert root.left.left.val==2
assert root.left.right.val==4
assert root.right.right.val==8
