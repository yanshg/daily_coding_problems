#!/usr/bin/python

"""

This problem was asked by Fitbit.

Given a linked list, rearrange the node values such that they appear in alternating low -> high -> low -> high ... form. For example, given 1 -> 2 -> 3 -> 4 -> 5, you should return 1 -> 3 -> 2 -> 5 -> 4.

"""

class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

    def __repr__(self):
        return "{}->{}".format(self.val,self.next)

def generate_list(nums):
    head,next=None,None
    for num in reversed(nums):
        head=Node(num,next)
        next=head
    return head

def get_values(head):
    values=[]
    while head:
        values+=[head.val]
        head=head.next
    return values

def alter_list(head):
    if not head or not head.next:
        return head

    remain=head.next.next
    head.next.next=head
    head=head.next
    head.next.next=alter_list(remain)
    return head

assert get_values(alter_list(generate_list([1,2,3,4,5])))==[2,1,4,3,5]

