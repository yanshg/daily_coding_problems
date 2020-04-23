#!/usr/bin/python

"""

This problem was asked by Netflix.

A Cartesian tree with sequence S is a binary tree defined by the following two properties:

    It is heap-ordered, so that each parent value is strictly less than that of its children.
    An in-order traversal of the tree produces nodes with values that correspond exactly to S.

For example, given the sequence [3, 2, 6, 1, 9], the resulting Cartesian tree would be:

      1
    /   \
  2       9
 / \
3   6

Given a sequence S, construct the corresponding Cartesian tree.

"""

class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

    def __repr__(self):
        return "{}->({},{})".format(self.val,self.left,self.right)


def inorder_seq(root):
    if not root:
        return []
    return inorder_seq(root.left)+[root.val]+inorder_seq(root.right)

def construct_cartesian_tree(nums):
    if not nums:
        return None

    min_num=nums[0]
    min_index=0
    for i,num in enumerate(nums):
        if num<min_num:
            min_num=num
            min_index=i

    return Node(nums[min_index],
                construct_cartesian_tree(nums[:min_index]),
                construct_cartesian_tree(nums[min_index+1:]))

assert inorder_seq(construct_cartesian_tree([]))==[]
assert inorder_seq(construct_cartesian_tree([3, 2, 6, 1, 9]))==[3, 2, 6, 1, 9]
assert inorder_seq(construct_cartesian_tree([9, 3, 7, 1, 8, 12, 10, 20, 15, 18, 5]))==[9, 3, 7, 1, 8, 12, 10, 20, 15, 18,5]
