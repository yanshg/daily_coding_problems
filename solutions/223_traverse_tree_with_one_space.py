#!/usr/bin/python

"""

This problem was asked by Palantir.

Typically, an implementation of in-order traversal of a binary tree has O(h) space complexity, where h is the height of the tree. Write a program to compute the in-order traversal of a binary tree using O(1) space.

"""

# Article: https://leetcode.com/articles/binary-tree-inorder-traversal/

class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

    def __repr__(self):
        return "{}->({},{})".format(self.val,self.left,self.right)

def helper(root,results=[]):
    if not root:
        return

    helper(root.left,results)
    results.append(root.val)
    helper(root.right,results)

def inorder_traverse_recursive(root):
    results=[]
    helper(root,results)
    return results

# Note: could not use deque for inorder traversal
#       deque is for traversal level by level

# Idea:
#       1. current=root
#       1. push all nodes from the current node to its leftmost leaf to stack
#       2. pop node from the stack
#       3. for each popped node, perform same actions from #1 for its right subtree
def inorder_traverse_with_stack(root):
    if not root:
        return []

    results,stack=[],[]
    curr=root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr=curr.left

        curr=stack.pop()
        results.append(curr.val)
        curr=curr.right

    return results

# Note: use Moriss traversal without stack, only O(1) space
def moriss_traverse(root):
    results=[]
    curr=root
    while curr:
        if not curr.left:
            results.append(curr.val)
            curr=curr.right
        else:
            # Find the inorder predecessor of current
            pre=curr.left
            while pre.right and pre.right!=curr:
                pre=pre.right

            # Make current as right child of its inorder predecessor
            if not pre.right:
                pre.right=curr
                curr=curr.left
            else:
                # Revert the change to original tree
                # fix the right child of predecessor
                pre.right=None
                results.append(curr.val)
                curr=curr.right

    return results

"""
      1                        2
    /   \                    /   \
   2     3           ->     4     5
  / \   / \                        \
 4   5 6   7                        1
                                     \
                                      3
                                    /   \
                                   6     7

"""

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

assert inorder_traverse_recursive(n1)==[4,2,5,1,6,3,7]
assert inorder_traverse_with_stack(n1)==[4,2,5,1,6,3,7]
assert moriss_traverse(n1)==[4,2,5,1,6,3,7]

