#!/usr/bin/python

"""

This problem was asked by Amazon.

A tree is symmetric if its data and shape remain unchanged when it is reflected about the root node. The following tree is an example:

        4
      / | \
    3   5   3
  /           \
 9             9

Given a k-ary tree, determine whether it is symmetric.

"""

class KaryTree():
    def __init__(self,val,children=[]):
        self.val=val
        self.children=children

    def __repr__(self):
        return "{}: {}".format(self.val,self.children)

def is_same_shape(tree1,tree2):
    if not tree1 and not tree2:
        return True

    if not tree1 or not tree2:
        return False

    if tree1.val != tree2.val or \
        len(tree1.children) != len(tree2.children):
        return False

    for c1,c2 in zip(tree1.children, tree2.children):
        if not is_same_shape(c1,c2):
            return False

    return True

def is_symmetric_kary_tree(tree):
    if not tree or not tree.children:
        return True

    n=len(tree.children)
    mid=n//2
    for i in range(mid):
        if not is_same_shape(tree.children[i],tree.children[-i-1]):
            return False

    if n%2==1:
        return is_symmetric_kary_tree(tree.children[mid])

    return True

n1=KaryTree(9)
n2=KaryTree(9)
n3=KaryTree(3,[n1])
n4=KaryTree(5)
n5=KaryTree(3,[n2])
n6=KaryTree(4,[n3,n4,n5])
print(n6)
assert is_symmetric_kary_tree(n6)

n1.val=6
assert not is_symmetric_kary_tree(n6)

