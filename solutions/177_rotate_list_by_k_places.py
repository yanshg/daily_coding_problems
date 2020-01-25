#!/usr/bin/python

"""
This problem was asked by Airbnb.

Given a linked list and a positive integer k, rotate the list to the right by k places.

For example, given the linked list 7 -> 7 -> 3 -> 5 and k = 2, it should become 3 -> 5 -> 7 -> 7.

Given the linked list 1 -> 2 -> 3 -> 4 -> 5 and k = 3, it should become 3 -> 4 -> 5 -> 1 -> 2.

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

def rotate_list(head,k):
    p1,p2=head,head
    i=0
    while i<k and p2:
        p2=p2.next
        i+=1

    if not p2:
        return head

    while p2.next:
        p1=p1.next
        p2=p2.next

    temp_head=p1.next
    p1.next=None
    p2.next=head
    head=temp_head

    return head

assert get_values(rotate_list(generate_list([7,7,3,5]),2))==[3,5,7,7]
assert get_values(rotate_list(generate_list([1,2,3,4,5]),3))==[3,4,5,1,2]
