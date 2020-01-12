#!/usr/bin/python

"""

This problem was asked by Google.

Given a binary tree of integers, find the maximum path sum between two nodes. The path must go through at least one node, and does not need to go through the root.

"""

class Node():
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

    def __repr__(self):
        return "{}=>({}, {})".format(self.val,self.left,self.right)

def get_max_path_sum_helper(root):
    if not root:
        return 0,0

    left_max_so_far,left_max_overall=get_max_path_sum_helper(root.left)
    right_max_so_far,right_max_overall=get_max_path_sum_helper(root.right)

    max_so_far=max(root.val, max(left_max_so_far,right_max_so_far)+root.val)
    max_overall=max(max_so_far,left_max_so_far+right_max_so_far+root.val)

    return max_so_far,max_overall

def get_max_path_sum(root):
    max_so_far,max_overall=get_max_path_sum_helper(root)
    return max_overall

root = Node(10) 
root.left = Node(2) 
root.right   = Node(10)
root.left.left  = Node(20)
root.left.right = Node(1)
root.right.right = Node(-25)
root.right.right.left   = Node(3) 
root.right.right.right  = Node(4) 
assert get_max_path_sum(root)==42
