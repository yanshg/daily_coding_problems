#!/usr/bin/python

"""

This problem was asked by LinkedIn.

Determine whether a tree is a valid binary search tree.

A binary search tree is a tree with two children, left and right, and satisfies the constraint that the key in the left child must be less than or equal to the root and the key in the right child must be greater than or equal to the root.

"""

class Node():
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

    def __repr__(self):
        return "{}=>({},{})".format(self.val,self.left,self.right)

def is_valid_bst(root):
    if not root:
        return True

    if (root.left and root.left.val > root.val) or \
       (root.right and root.right.val < root.val):
        return False

    return is_valid_bst(root.left) and \
           is_valid_bst(root.right)


a=Node(200)
b=Node(50)
c=Node(201)

a.left=b
a.right=c
print a

assert is_valid_bst(a)

assert is_valid_bst(None)

a = Node(3)
b = Node(2)
c = Node(6)
d = Node(1)
e = Node(3)
f = Node(4)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
assert is_valid_bst(a)


a = Node(1)
b = Node(2)
c = Node(6)
d = Node(1)
e = Node(3)
f = Node(4)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
assert not is_valid_bst(a)

a = Node(3)
b = Node(2)
c = Node(6)
d = Node(1)
e = Node(4)
f = Node(4)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
assert not is_valid_bst(a)
