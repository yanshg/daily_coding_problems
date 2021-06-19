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

class Node1:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "{}->{}".format(self.val,self.next)

def create_singly_link(nums):
    head,next = None,None
    for num in reversed(nums):
        head = Node1(num, next)
        next = head
    return head


# Post Order handling
def traverse_compare(right):
    global left
    if not right or not left:
        return True

    #print("left: {},  right: {}".format(left, right))
    res = traverse_compare(right.next)
    print("left: {},  right: {}".format(left, right))
    #print("")
    left_val,right_val=left.val,right.val
    left=left.next
    if res and left_val == right_val:
        return True
    return False

def is_singly_link_palindrome(head):
    return traverse_compare(head)

assert is_palindrome(create_list([1,4,3,4,1]))
assert not is_palindrome(create_list([1,4]))

head = create_singly_link([1,4,3,4,1])
left=head
assert is_singly_link_palindrome(head)

head = create_singly_link([3,4,1])
left=head
assert not is_singly_link_palindrome(head)
