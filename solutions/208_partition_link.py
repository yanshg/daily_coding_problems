#!/usr/bin/python

"""

This problem was asked by LinkedIn.

Given a linked list of numbers and a pivot k, partition the linked list so that all nodes less than k come before nodes greater than or equal to k.

For example, given the linked list 5 -> 1 -> 8 -> 0 -> 3 and k = 3, the solution could be 1 -> 0 -> 5 -> 8 -> 3.

"""

# Idea:  always place the node which < pivot to the head

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


def partition_list(head, pivot):
    prev,curr=head,head.next
    while curr:
        if curr.val < pivot:
            # move node to the head
            prev.next=curr.next
            curr.next=head
            head=curr
            curr=prev.next
        else:
            prev=curr
            curr=curr.next

    return head

assert get_values(partition_list(generate_list([5,1,8,0,3]),3))==[0,1,5,8,3]

