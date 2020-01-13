#!/usr/bin/python

"""
This problem was asked by Google.

Determine whether a doubly linked list is a palindrome. What if it's singly linked?

For example, 1 -> 4 -> 3 -> 4 -> 1 returns True while 1 -> 4 returns False.

"""

class Node():
    def __init__(self,val,prev=None,next=None):
        self.val=val
        self.prev=prev
        self.next=next

    def __repr__(self):
        return "{}<=>{}".format(self.val,self.next)

def create_list(values):
    head,prev,next=None,None,None
    for val in reversed(values):
        head=Node(val,None,next)
        if prev:
            prev.prev=head
        prev,next=head,head
    return head

def is_palindrome(head):
    tail=head
    while tail and tail.next:
        tail=tail.next

    while tail and head:
        if tail.val != head.val:
            return False
        tail=tail.prev
        head=head.next
    return True

assert is_palindrome(create_list([1,4,3,4,1]))
assert not is_palindrome(create_list([1,4]))

