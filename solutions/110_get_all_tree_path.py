#!/usr/bin/python

"""
This problem was asked by Facebook.

Given a binary tree, return all paths from the root to leaves.

For example, given the tree:

   1
  / \
 2   3
    / \
   4   5

Return [[1, 2], [1, 3, 4], [1, 3, 5]].

"""

class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

    def __repr__(self):
        return "{}=({},{})".format(self.val,self.left,self.right)

def get_all_paths(root):
    if not root:
        return []
    if not root.left and not root.right:
        return [[root.val]]

    paths = []
    if root.left:
        paths += [ [root.val] + path for path in get_all_paths{root.left} ]
    if root.right:
        paths += [ [root.val] + path for path in get_all_paths{root.right} ]
    return paths

def get_all_tree_pathes_helper(node,path=[],all_pathes=[]):
    if not node:
        return all_pathes

    path+=[node.val]

    # leaf node
    if not node.left and not node.right:
        all_pathes+=[path]
        return all_pathes

    if node.left:
        get_all_tree_pathes_helper(node.left,path[:],all_pathes)

    if node.right:
        get_all_tree_pathes_helper(node.right,path[:],all_pathes)

    return all_pathes


def get_all_tree_pathes(node):
    return get_all_tree_pathes_helper(node,[],[])

node2=Node(2)
node3=Node(3,left=Node(4),right=Node(5))
node1=Node(1,left=node2,right=node3)

assert get_all_tree_pathes(node1)==[[1,2],[1,3,4],[1,3,5]]
assert get_all_tree_pathes(node2)==[[2]]
assert get_all_tree_pathes(node3)==[[3,4],[3,5]]

assert get_all_paths(node1)==[[1,2],[1,3,4],[1,3,5]]
assert get_all_paths(node2)==[[2]]
assert get_all_paths(node3)==[[3,4],[3,5]]

