#!/usr/bin/python

"""

This question was asked by Snapchat.

Given the head to a singly linked list, where each node also has a 'random' pointer that points to anywhere in the linked list, deep clone the list.

"""

class Node:
    def __init__(self,val,next=None,random=None):
        self.val=val
        self.next=next
        self.random=random

    def __repr__(self):
        return "{}=>{}".format(self.val,self.next)

def deep_clone(head):
    arr_clone=list()
    hash_orig=dict()

    # get the 'random' nodes' index and replay in cloned list
    i=0
    curr=head
    while curr:
        hash_orig[curr]=i

        node_clone=Node(curr.val)
        arr_clone.append(node_clone)

        curr=curr.next
        i+=1

    i=0
    curr=head
    while curr:
        node_clone=arr_clone[i]
        node_clone.next=None if not curr.next else arr_clone[hash_orig[curr.next]]
        node_clone.random=None if not curr.random else arr_clone[hash_orig[curr.random]]

        curr=curr.next
        i+=1

    return arr_clone[0]

node1=Node(1)
node2=Node(2)
node3=Node(3)
node4=Node(4)
node5=Node(5)

node1.next=node2
node1.random=node4
node2.next=node3
node2.random=node5
node3.next=node4
node3.random=node1
node4.next=node5

cloned=deep_clone(node1)
print(str(cloned))

assert cloned.val==node1.val
assert cloned.random.val==4
assert cloned.next.random.val==5
