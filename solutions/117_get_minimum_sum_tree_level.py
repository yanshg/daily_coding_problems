#!/usr/bin/python

"""
This problem was asked by Facebook.

Given a binary tree, return the level of the tree with minimum sum.

"""

from collections import defaultdict,deque

class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

    def __repr__(self):
        return "{}=> ({}, {})".format(self.val,self.left,self.right)

def helper(node,sums,level):
    if not node:
        return

    sums[level]+=node.val
    helper(node.left,sums,level+1)
    helper(node.right,sums,level+1)

def helper_with_deque(node,sums,level):
    queue=deque([(node,level)])
    while(queue):
        node,level=queue.popleft()
        sums[level]+=node.val
        if node.left:
            queue.append((node.left, level+1))
        if node.right:
            queue.append((node.right, level+1))

def get_minimum_sum_tree_level(node):
    sums=defaultdict(int)
    helper(node,sums,0)
    #helper_with_deque(node,sums,0)
    return min(sums,key=sums.get)

node1=Node(6)
node2=Node(2)
node3=Node(3)
node4=Node(4)
node5=Node(7)

node1.left=node2
node1.right=node3
node3.left=node4
node3.right=node5

assert get_minimum_sum_tree_level(node1)==1
