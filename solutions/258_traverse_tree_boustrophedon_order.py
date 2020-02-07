#!/usr/bin/python

"""

This problem was asked by Morgan Stanley.

In Ancient Greece, it was common to write text with the first line going left to right, the second line going right to left, and continuing to go back and forth. This style was called "boustrophedon".

Given a binary tree, write an algorithm to print the nodes in boustrophedon order.

For example, given the following tree:

       1
    /     \
  2         3
 / \       / \
4   5     6   7

You should return [1, 3, 2, 4, 5, 6, 7].

"""

from collections import deque,defaultdict

class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

    def __repr__(self):
        return "{}->({},{})".format(self.val,self.left,self.right)


def boustrophedon_order_traverse(root):
    level_dict=defaultdict(list)
    dq=deque([(root,0)])
    while dq:
        node,level=dq.popleft()

        level_dict[level]+=[node.val]

        if node.left:
            dq.append((node.left,level+1))

        if node.right:
            dq.append((node.right,level+1))

    values=[]
    for i in range(len(level_dict)):
        if i%2==0:
            values.extend(level_dict[i])
        else:
            values.extend(reversed(level_dict[i]))

    return values

n1=Node(1)
n2=Node(2)
n3=Node(3)
n4=Node(4)
n5=Node(5)
n6=Node(6)
n7=Node(7)
n1.left=n2
n1.right=n3
n2.left=n4
n2.right=n5
n3.left=n6
n3.right=n7

assert boustrophedon_order_traverse(n1)==[1, 3, 2, 4, 5, 6, 7]
