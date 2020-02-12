#!/usr/bin/python

"""

This problem was asked by Oracle.

Given a binary search tree, find the floor and ceiling of a given integer. The floor is the highest element in the tree less than or equal to an integer, while the ceiling is the lowest element in the tree greater than or equal to an integer.

If either value does not exist, return None.

"""

class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

    def __repr__(self):
        return "{}->({},{})".format(self.val,self.left,self.right)

def helper(root,n,floor=None,ceil=None):
    if not root:
        return floor,ceil
    if root.val==n:
        return n,n
    elif root.val<n:
        return helper(root.right,n,root.val,ceil)
    else:
        return helper(root.left,n,floor,root.val)



def get_floor_ceil(root,n):
    return helper(root,n,None,None)

"""
         6
       /   \
      4     10
     / \   /  \
    3   5 8   12
"""

n1=Node(6)
n2=Node(4)
n3=Node(10)
n4=Node(3)
n5=Node(5)
n6=Node(8)
n7=Node(12)

n1.left=n2
n1.right=n3
n2.left=n4
n2.right=n5
n3.left=n6
n3.right=n7

assert get_floor_ceil(n1,1)==(None,3)
assert get_floor_ceil(n1,7)==(6,8)
assert get_floor_ceil(n1,17)==(12,None)
