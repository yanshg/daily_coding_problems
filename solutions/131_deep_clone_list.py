#!/usr/bin/python

"""

This question was asked by Snapchat.

Given the head to a singly linked list, where each node also has a “random” pointer that points to anywhere in the linked list, deep clone the list.

"""

class Node:
    def __init__(self,val,next=None,random=None):
        self.val=val
        self.next=next
        self.random=random

    def __repr__(self):
        return "{}=>{}".format(self.val,self.next)

def deep_clone(head):
    curr=head

    arr_orig=list()
    arr_clone=list()
    hash_orig=dict()

    # get the 'random' nodes' index and replay in cloned list
    i=0
    while curr:
        arr_orig.append(curr)
        hash_orig[curr]=i

        node_clone=Node(curr.val)
        arr_clone.append(node_clone)

        curr=curr.next
        i+=1

    l=len(arr_orig)
    for i in range(l):
        if i<l-1:
            arr_clone[i].next=arr_clone[i+1]

        random_node=arr_orig[i].random
        if random_node and \
                random_node in hash_orig:
            idx=hash_orig[random_node]
            arr_clone[i].random=arr_clone[idx]

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
