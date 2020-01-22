#!/usr/bin/python

"""
This problem was asked by Google.

Given the head of a singly linked list, swap every two nodes and return its head.

For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.

"""

class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

    def __repr__(self):
        return "{}->{}".format(self.val, self.next)

def generate_list(values):
    head,next=None,None
    for val in values[::-1]:
        head=Node(val,next)
        next=head
    return head
    
def get_list_values(head):
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

assert get_list_values(swap_two_nodes(generate_list([])))==[]
assert get_list_values(swap_two_nodes(generate_list([1,2,3,4])))==[2,1,4,3]
assert get_list_values(swap_two_nodes(generate_list([1,2,3,4,5])))==[2,1,4,3,5]
