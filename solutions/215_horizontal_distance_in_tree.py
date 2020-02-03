#!/usr/bin/python

"""

This problem was asked by Yelp.

The horizontal distance of a binary tree node describes how far left or right the node will be when the tree is printed out.

More rigorously, we can define it as follows:

    The horizontal distance of the root is 0.
    The horizontal distance of a left child is hd(parent) - 1.
    The horizontal distance of a right child is hd(parent) + 1.

For example, for the following tree, hd(1) = -2, and hd(6) = 0.

             5
          /     \
        3         7
      /  \      /   \
    1     4    6     9
   /                /
  0                8

The bottom view of a tree, then, consists of the lowest node at each horizontal distance. If there are two nodes at the same depth and horizontal distance, either is acceptable.

For this tree, for example, the bottom view could be [0, 1, 3, 6, 8, 9].

Given the root to a binary tree, return its bottom view.

"""

class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
        self.depth=None

    def __repr__(self):
        return "{}->({},{})".format(self.val,self.left,self.right)

def get_horizontal_distance(root,distances=dict()):
    
def bottom_view_of_tree(root):
    pass

n1=Node(5)
n2=Node(3)
n3=Node(7)
n4=Node(1)
n5=Node(4)
n6=Node(6)
n7=Node(9)
n8=Node(0)
n9=Node(8)


n1.left=n2
n1.right=n3
