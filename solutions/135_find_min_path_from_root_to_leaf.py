#!/usr/bin/python

"""
This question was asked by Apple.

Given a binary tree, find a minimum path sum from root to a leaf.

For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.

  10
 /  \
5    5
 \     \
   2    1
       /
     -1
"""

from collections import defaultdict

class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

    def __repr__(self):
        return "{}=>({}, {})".format(self.val,self.left,self.right)

def get_min_sum_path_helper(node,sum,path):
    if not node:
        return (sum,path)

    sum+=node.val
    path+=[node.val]

    if not node.left and not node.right:
        return (sum,path)

    sum_left,sum_right=float('inf'),float('inf')
    path_left,path_right=path,path
    if node.left:
        sum_left,path_left=get_min_sum_path_helper(node.left,sum,path[:])

    if node.right:
        sum_right,path_right=get_min_sum_path_helper(node.right,sum,path[:])

    return (sum_left,path_left) if sum_left<sum_right else (sum_right,path_right)

def get_min_sum_path(root):
    _, path=get_min_sum_path_helper(root,0,[])
    return path

node1=Node(10)
node2=Node(5)
node3=Node(5)
node4=Node(2)
node5=Node(1)
node6=Node(-1)

node1.left=node2
node1.right=node3
node2.right=node4
node3.right=node5
node5.left=node6

print(node1)

assert get_min_sum_path(node1)==[10,5,1,-1]
