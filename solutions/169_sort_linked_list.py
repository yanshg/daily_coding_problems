#!/usr/bin/python

"""
This problem was asked by Google.

Given a linked list, sort it in O(n log n) time and constant space.

For example, the linked list 4 -> 1 -> -3 -> 99 should become -3 -> 1 -> 4 -> 99

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

def partition_list(head):
    slow,fast=head,head
    while slow.next and fast.next and fast.next.next:
        slow=slow.next
        fast=fast.next.next

    list1,list2=head,slow.next
    slow.next=None
    return list1,list2

def merge_list(list1,list2):
    if not list1:
        return list2

    if not list2:
        return list1

    # Note: need use '(', and ')' to get the tuple.
    p1,p2=(list1,list2) if list1.val<=list2.val else (list2,list1)
    head=p1

    while p1 and p2:
        while p1.next and p1.next.val<=p2.val:
            p1=p1.next

        temp_p1=p1.next
        p1.next=p2
        p1=temp_p1

        if not p1:
            break

        while p2.next and p2.next.val<=p1.val:
            p2=p2.next

        temp_p2=p2.next
        p2.next=p1
        p2=temp_p2

    return head

def merge_sort_list(head):
    if not head:
        return None

    if not head.next:
        return head

    list1,list2=partition_list(head)
    list1=merge_sort_list(list1)
    list2=merge_sort_list(list2)
    return merge_list(list1,list2)

assert get_values(merge_sort_list(generate_list([4,1,-3,99])))==[-3,1,4,99]
