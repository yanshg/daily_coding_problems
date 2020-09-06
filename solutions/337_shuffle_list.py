#!/usr/bin/python

"""

This problem was asked by Apple.

Given a linked list, uniformly shuffle the nodes. What if we want to prioritize space over time?

"""

# Article:  https://massivealgorithms.blogspot.com/2019/03/shuffling-linked-list.html

# Idea: merge sort

import random

class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "{}->{}".format(self.val,self.next)

def generate_list(arr):
    head,next = None,None
    for v in reversed(arr):
        head = Node(v, next)
        next = head
    return head

def shuffle_list(lst):
    if not lst or not lst.next:
        return lst

    slow,fast=lst,lst
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    left = lst
    right = slow.next
    slow.next = None

    left = shuffle_list(left)
    right = shuffle_list(right)
    return merge(left,right)

def merge(left,right):
    dummy = Node('')
    current = dummy
    while left and right:
        rand = random.random()
        if rand < 0.5:
            # choose one item from left
            node = left
            left = left.next
        else:
            # choose one item from right
            node = right
            right = right.next

        node.next = None
        current.next = node
        current = node

    if left:
        current.next = left
    elif right:
        current.next = right

    return dummy.next

arr = list(range(10))
lst = generate_list(arr)
print(lst)
print(shuffle_list(lst))

