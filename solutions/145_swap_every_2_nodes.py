#!/usr/bin/python

"""
This problem was asked by Google.

Given the head of a singly linked list, swap every two nodes and return its head.

For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.
"""

class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

    def __repr__(self):
        return "{}->{}".format(self.val, self.next)

def get_nodes(values):
    next=None
    for val in values[::-1]:
        node=Node(val)
        node.next=next
        next=node
    return next
    
def get_list(head):
    values=[];
    while head:
        values.append(head.val)
        head=head.next
    return values

def swap_two_nodes(head):
    if not head:
        return None

    if not head.next:
        return head

    tmp_head=head.next
    remain=tmp_head.next
    tmp_head.next=head
    head.next=swap_two_nodes(remain)
    return tmp_head

assert get_list(swap_two_nodes(get_nodes([])))==[]
assert get_list(swap_two_nodes(get_nodes([1,2,3,4])))==[2,1,4,3]
assert get_list(swap_two_nodes(get_nodes([1,2,3,4,5])))==[2,1,4,3,5]
