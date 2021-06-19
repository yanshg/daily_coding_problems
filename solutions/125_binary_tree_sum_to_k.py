#!/usr/bin/python

"""
This problem was asked by Google.

Given the root of a binary search tree, and a target K, return two nodes in the tree whose sum equals K.

For example, given the following tree and K of 20

    10
   /   \
 5      15
       /  \
     11    15

Return the nodes 5 and 15.

"""

class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

    def __repr__(self):
        return "{}=>({},{})".format(self.val,self.left,self.right)

def sum_to_k(root,target,hashset=set()):
    if not root:
        return None

    v1 = root.val
    v2 = target - v1
    if v2 in hashset:
        return [ v1, v2 ] if v1 <= v2 else [ v2, v1 ]

    hashset.add(root.val)

    return sum_to_k(root.left,target,hashset) or \
           sum_to_k(root.right,target,hashset)


node1=Node(10)
node2=Node(5)
node3=Node(15)
node4=Node(11)
node5=Node(15)
node1.left=node2
node1.right=node3
node3.left=node4
node3.right=node5
print(node1)

assert sum_to_k(node1, 20)==[5, 15]
assert sum_to_k(node1, 16)==[5, 11]
assert not sum_to_k(node1, 17)

