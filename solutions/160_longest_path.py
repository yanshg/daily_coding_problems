#!/usr/bin/python

"""
This problem was asked by Uber.

Given a tree where each edge has a weight, compute the length of the longest path in the tree.

For example, given the following tree:

   a
  /|\
 b c d
    / \
   e   f
  / \
 g   h

and the weights: a-b: 3, a-c: 5, a-d: 8, d-e: 2, d-f: 4, e-g: 1, e-h: 1, the longest path would be c -> a -> d -> f, with a length of 17.

The path does not have to pass through the root, and each node can have any amount of children.

"""

from collections import defaultdict

class Node:

    def __init__(self,id):
        self.id=id
        self.max_path=0
        self.child_dists=list()

    def __repr__(self):
        return "id: {}, max_path: {}, children: {}".format(self.id,self.max_path,self.child_dists)

def get_max_path(root):
    if not root.child_dists:
        return 0

    path_lens=list()
    child_max_path_lens=list()

    for child,dist in root.child_dists:
        path_lens.append(child.max_path + dist)
        child_max_path_lens.append(get_max_path(child))

    child_max_path_len=max(child_max_path_lens)

    return max(sum(sorted(path_lens)[-2:]), child_max_path_len)

def update_max_path(root):
    if not root.child_dists:
        root.max_path=0
        return

    root_paths=list()
    for child,dist in root.child_dists:
        update_max_paths(child)
        root_paths.append(child.max_path + dist)

    root.max_path=max(root_paths)

def get_longest_path(root):
    update_max_paths(root)
    return get_max_path(root)

a=Node('a')
b=Node('b')
c=Node('c')
d=Node('d')
e=Node('e')
f=Node('f')
g=Node('g')
h=Node('h')

a.child_dists=[ (b, 3), (c, 5), (d, 8) ]
d.child_dists=[ (e, 2), (f, 4) ]
e.child_dists=[ (g, 1), (h, 1) ]

print(a)
assert get_max_path(a)==17
