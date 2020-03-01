#!/usr/bin/python

"""

This problem was asked by Salesforce.

Write a program to merge two binary trees. Each node in the new tree should hold a value equal to the sum of the values of the corresponding nodes of the input trees.

If only one input tree has a node in a given position, the corresponding node in the new tree should match that input node.

"""

class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

    def __repr__(self):
        return "{}->({},{})".format(self.val,self.left,self.right)

def merge_tree(tree1,tree2):
    if not tree1 and not tree2:
        return None

    val=0
    left1,right1=None,None
    left2,right2=None,None
    if tree1:
        val+=tree1.val
        left1,right1=tree1.left,tree1.right
    if tree2:
        val+=tree2.val
        left2,right2=tree2.left,tree2.right

    return Node(val, merge_tree(left1,left2), merge_tree(right1,right2))


"""

    2            4             6
   / \     +      \     =     / \
  1   3            5         1   8

"""

n1=Node(2)
n2=Node(1)
n3=Node(3)
n1.left=n2
n1.right=n3

n4=Node(4)
n5=Node(5)
n4.right=n5

new_tree=merge_tree(n1,n4)
assert new_tree.val==6
assert new_tree.left.val==1
assert new_tree.right.val==8


