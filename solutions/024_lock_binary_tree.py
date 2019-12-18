#!/usr/bin/python

"""
This problem was asked by Google.

Implement locking in a binary tree. A binary tree node can be locked or unlocked only if all of its descendants or ancestors are not locked.

Design a binary tree node class with the following methods:

    is_locked, which returns whether the node is locked
    lock, which attempts to lock the node. If it cannot be locked, then it should return false. Otherwise, it should lock it and return true.
    unlock, which unlocks the node. If it cannot be unlocked, then it should return false. Otherwise, it should unlock it and return true.

You may augment the node to add parent pointers or any other property you would like. You may assume the class is used in a single-threaded program, so there is no need for actual locks or mutexes. Each method should run in O(h), where h is the height of the tree.

"""

class Node:
    def __init__(self,val,left=None,right=None,parent=None,locked=False):
        self.val=val
        self.left=left
        self.right=right
        self.parent=parent
        self.locked=locked

    def __repr__(self):
        return "{}=>({},{})".format(self.val,self.left,self.right)

    def is_ancestors_locked(self):
        if not self.parent:
            return False

        if self.parent.locked:
            return True

        return self.parent.is_ancestors_locked()

    def is_descendants_locked(self):
        if (self.left and self.left.locked) or \
                (self.right and self.right.locked):
            return True

        return (self.left and self.left.is_descendants_locked()) or \
                (self.right and self.right.is_descendants_locked())

    def is_locked(self):
        return self.locked

    def can_lock(self):
        if self.is_ancestors_locked() or \
                self.is_descendants_locked():
            return False
        return True

    def set_lock_state(self,lock_state):
        success=self.can_lock()
        if success:
            self.locked=lock_state
        return success

    def lock(self):
        return self.set_lock_state(True)

    def unlock(self):
        return self.set_lock_state(False)

node1=Node(1)
node2=Node(2)
node3=Node(3)
node4=Node(4)
node5=Node(5)
node6=Node(6)
node7=Node(7)
node8=Node(8)
node9=Node(9)

node1.left=node2
node1.right=node3
node2.parent=node1
node3.parent=node1

node2.left=node4
node4.parent=node2

node3.left=node5
node3.right=node6
node5.parent=node3
node6.parent=node3

node5.left=node7
node5.right=node8
node7.parent=node5
node8.parent=node5

node6.right=node9
node9.parent=node6

print(node1)

"""
       1
      / \
     2   3
    /   / \
   4   5   6
      / \   \
     7   8   9

"""

assert not node9.is_locked()

node5.lock()
assert node5.is_locked()

node6.lock()

assert not node8.unlock()

node5.unlock()
assert node8.unlock()

