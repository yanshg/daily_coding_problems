#!/usr/bin/python

"""

This problem was asked by Google.

Given a binary search tree and a range [a, b] (inclusive), return the sum of the elements of the binary search tree within the range.

For example, given the following tree:

    5
   / \
  3   8
 / \ / \
2  4 6  10

and the range [4, 9], return 23 (5 + 4 + 6 + 8).


"""

class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

    def __repr__(self):
        return "{}->({},{})".format(self.val,self.left,self.right)

def sum_range(root,low,high):
    if not root:
        return 0

    if root.val<low:
        return sum_range(root.right,low,high)

    if root.val>high:
        return sum_range(root.left,low,high)

    return root.val + \
            sum_range(root.left,low,high) + \
            sum_range(root.right,low,high)

n1=Node(5)
n2=Node(3)
n3=Node(8)
n4=Node(2)
n5=Node(4)
n6=Node(6)
n7=Node(10)
n1.left=n2
n1.right=n3
n2.left=n4
n2.right=n5
n3.left=n6
n3.right=n7

assert sum_range(n1,4,9)==23
