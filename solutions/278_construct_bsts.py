#!/usr/bin/python

"""

This problem was asked by Amazon.

Given an integer N, construct all possible binary search trees with N nodes.

"""

class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

    def __repr__(self):
        return "{}-({},{})".format(self.val,self.left,self.right)

def preorder(root):
    results=[]

    if root:
        results+=[root.val]
        results+=preorder(root.left)
        results+=preorder(root.right)

    return results

def construct_bsts(nums):
    if not nums:
        return [ None ]

    n=len(nums)
    if n==1:
        return [ Node(nums[0]) ]

    all_bsts=[]
    for i in range(n):
        all_bsts_left=construct_bsts(nums[:i])
        all_bsts_right=construct_bsts(nums[i+1:])
        for left in all_bsts_left:
            for right in all_bsts_right:
                all_bsts+=[ Node(nums[i],left,right) ]

    return all_bsts

def make_trees(n):
    trees=construct_bsts(list(range(1,n+1)))
    for tree in trees:
         print(preorder(tree))

make_trees(3)
