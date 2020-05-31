#!/usr/bin/python

"""

This problem was asked by Yext.

Two nodes in a binary tree can be called cousins if they are on the same level of the tree but have different parents. For example, in the following diagram 4 and 6 are cousins.

    1
   / \
  2   3
 / \   \
4   5   6

Given a binary tree and a particular node, find all cousins of that node.

"""

from collections import deque,defaultdict

class Node():
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

    def __repr__(self):
        #return "{}".format(self.val)
        return "{}=>({},{})".format(self.val,self.left,self.right)

# BFS
def get_cousins(root,node):
    level_nodes=defaultdict(list)
    found_level,found_parent=-1,None

    dq=deque([(root,0,None)])
    while dq:
        (n,level,parent)=dq.popleft()

        if n==node:
            found_level=level
            found_parent=parent

        if found_level>0 and level>found_level:
            break

        level_nodes[level].append((n,parent))

        if n.left:
            dq.append((n.left,level+1,n))
        if n.right:
            dq.append((n.right,level+1,n))

    cousins=[]
    if found_level>0:
        for n,parent in level_nodes[found_level]:
            if parent != found_parent:
                cousins+=[n]
    return cousins

n1=Node(1)
n2=Node(2)
n3=Node(3)
n4=Node(4)
n5=Node(5)
n6=Node(6)
n1.left=n2
n1.right=n3
n2.left=n4
n2.right=n5
n3.right=n6

assert get_cousins(n1,n4)==[n6]
assert get_cousins(n1,n6)==[n4,n5]
assert not get_cousins(n1,n2)
assert not get_cousins(n1,n3)

