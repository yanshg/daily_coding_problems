#!/usr/bin/python

"""

This problem was asked by Etsy.

Given a sorted array, convert it into a height-balanced binary search tree.

"""

class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

    def __repr__(self):
        return "{}->({},{})".format(self.val,self.left,self.right)


# Base cases: 1. 0 number
#             2. 1 number  (could be covered by 2+ numbers case)
#             3. 2+ numbers
def construct_bst(nums):
    if not nums:
        return None

    mid=len(nums)//2
    return Node(nums[mid],construct_bst(nums[:mid]),construct_bst(nums[mid+1:]))

def preorder(root):
    return [root.val]+preorder(root.left)+preorder(root.right) if root else []

assert preorder(construct_bst(list(range(4))))==[2,1,0,3]
