#!/usr/bin/python

"""

This problem was asked by Google.

Given k sorted singly linked lists, write a function to merge all the lists into one sorted singly linked list.

"""

class Node():
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

def merge_2_lists(list1,list2):
    if not list1:
        return list2

    if not list2:
        return list1

    p1,p2=(list1,list2) if list1.val<=list2.val else (list2,list1)
    head=p1

    while p1 and p2:
        while p1.next and p1.next.val <= p2.val:
            p1=p1.next

        tmp_p1=p1.next
        p1.next=p2
        p1=tmp_p1

        if not p1:
            break

        while p2.next and p2.next.val <= p1.val:
            p2=p2.next

        tmp_p2=p2.next
        p2.next=p1
        p2=tmp_p2

    return head

def merge_lists(lists):
    if not lists:
        return lists

    n=len(lists)
    if n==1:
        return lists[0]
    elif n==2:
        return merge_2_lists(lists[0],lists[1])
    else:
        mid=n//2
        list1=merge_lists(lists[:mid])
        list2=merge_lists(lists[mid:])
        return merge_2_lists(list1,list2)

assert get_values(merge_lists([ generate_list([2,5,8]),generate_list([1,6,7,9]),generate_list([3,5,10,11]) ]))==[1,2,3,5,5,6,7,8,9,10,11]
