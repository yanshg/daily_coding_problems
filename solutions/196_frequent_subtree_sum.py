#!/usr/bin/python

"""

This problem was asked by Apple.

Given the root of a binary tree, find the most frequent subtree sum. The subtree sum of a node is the sum of all values under a node, including the node itself.

For example, given the following tree:

  5
 / \
2  -5

Return 2 as it occurs twice: once as the left leaf, and once as the sum of 2 + 5 - 5.

"""

from collections import defaultdict

class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

    def __repr__(self):
        return "{}->({}, {})".format(self.val,self.left,self.right)

def helper(root,freqs={}):
    if not root:
        return 0

    sum=helper(root.left,freqs) + root.val + helper(root.right,freqs)
    freqs[sum]+=1

    return sum

def get_most_frequent_subtree_sum(root):
    freqs=defaultdict(int)
    helper(root,freqs)
    return max(freqs, key=freqs.get)

a=Node(2)
b=Node(-5)
c=Node(5,a,b)

assert get_most_frequent_subtree_sum(c)==2
