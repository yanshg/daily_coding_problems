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


def construct_bst(nums):
    if not nums:
        return None

    n=len(nums)
    if n==1:
        return Node(nums[0])

    mid=n//2
    return Node(nums[mid], construct_bst(nums[:mid]), construct_bst(nums[mid+1:]))

def preorder(root):
    results=[]

    if root:
        results+=[root.val]
        results+=preorder(root.left)
        results+=preorder(root.right)

    return results

assert preorder(construct_bst(list(range(4))))==[2,1,0,3]
