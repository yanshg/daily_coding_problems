#!/usr/bin/python

"""
This problem was asked by Twitter.

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree. Assume that each node in the tree also has a pointer to its parent.

According to the definition of LCA on Wikipedia: "The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself)."
"""

class Node:
    def __init__(self,val,parent=None):
        self.val=val
        self.parent=parent

    def __repr__(self):
        return "{}=>{}".format(self.val,self.parent)

def get_length(node):
    if not node:
        return 0
    return 1+get_length(node.parent)

def get_lca(node1,node2):
    len1,len2=get_length(node1),get_length(node2)
    (longer,longer_len,shorter,shorter_len)=(node1,len1,node2,len2) if len1>len2 else (node2,len2,node1,len1)

    for _ in range(longer_len-shorter_len):
         longer=longer.parent

    while longer and shorter and longer != shorter:
        longer=longer.parent
        shorter=shorter.parent

    return longer

node1=Node(1)
node2=Node(2)
node3=Node(3)
node4=Node(4)
node5=Node(5)
node6=Node(6)
node7=Node(7)
node8=Node(8)
node9=Node(9)
node10=Node(10)
node11=Node(11)

node2.parent=node1
node3.parent=node2
node4.parent=node3
node5.parent=node3
node6.parent=node4
node7.parent=node3
node8.parent=node3
node9.parent=node8
node10.parent=node8

assert get_lca(node6,node9)==node3
assert get_lca(node7,node10)==node3
assert not get_lca(node11,node10)
