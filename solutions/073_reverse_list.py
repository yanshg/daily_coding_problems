#!/usr/bin/python

"""

This problem was asked by Google.

Given the head of a singly linked list, reverse it in-place.

"""

class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

    def __repr__(self):
        return "{}->{}".format(self.val,self.next)

def generate_list(vals):
    head,next=None,None
    for val in reversed(vals):
        head=Node(val,next)
        next=head
    return head

def get_values(head):
    return [head.val]+get_values(head.next) if head else []

def _reverse_list(curr):
    if not curr:
        return None,None

    if not curr.next:
        return curr,curr

    head,tail=_reverse_list(curr.next)
    tail.next=curr
    tail=curr
    curr.next=None

    return head,tail

def reverse_list(head):
    head,tail=_reverse_list(head)
    return head

assert get_values(reverse_list(generate_list([1,2,3,4,5])))==[5,4,3,2,1]

