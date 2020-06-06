#!/usr/bin/python

"""
This problem was asked by Google.

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

"""

class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

    def __repr__(self):
        return "{}=>({},{})".format(self.val,self.left,self.right)

def is_exact_tree(t,s):
    if not t and not s:
        return True

    if not t or not s:
        return False

    return t.val==s.val and \
            is_exact_tree(t.left,s.left) and \
            is_exact_tree(t.right,s.right)

# check if s is subtree of t:
def is_subtree(t,s):
    if s is None:
        return True

    if t is None:
        return False

    if is_exact_tree(t,s):
        return True

    return is_subtree(t.left,s) or \
           is_subtree(t.right,s)

"""
       1
     /   \
   2       3
         /   \
       4       5


"""

node1=Node(1)
node2=Node(2)
node3=Node(3)
node4=Node(4)
node5=Node(5)
node1.left=node2
node1.right=node3
node3.left=node4
node3.right=node5

node6=Node(1)
node7=Node(2)
node8=Node(3)
node9=Node(4)
node10=Node(5)
node6.left=node7
node6.right=node8
node8.left=node9
node8.right=node10

node11=Node(6)
node11.right=node6

assert is_exact_tree(node1, node6)
assert not is_exact_tree(node6, node11)
assert is_subtree(node1, node6)
assert not is_subtree(node1, node11)
assert not is_subtree(node3, node1)
