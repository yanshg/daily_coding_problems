#!/usr/bin/python

"""
This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.
"""

class Node:
    def __init__(self,val):
        self.val=val
        self.both=0

    def __repr__(self):
        return str(self.val)

class XorList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.idmap=dict()

    def __repr__(self):
        prev_id=0
        string=""
        curr=self.head
        while curr:
            if string:
                string+=" <-> "
            string+=str(curr)
            next_id=curr.both ^ prev_id
            prev_id=id(curr)
            curr=self.idmap[next_id] if next_id in self.idmap else None

        return string

    def add(self,node):
        if not node:
            return

        if not self.head:
            self.head=node

        node_id=id(node)

        prev_id=0
        if self.tail:
            prev_id=id(self.tail)
            self.tail.both ^= node_id

        node.both=prev_id

        self.tail=node
        self.idmap[node_id]=node

    def get(self,index):
        prev_id=0
        curr=self.head
        for i in range(index):
            next_id=curr.both ^ prev_id
            prev_id=id(curr)
            curr=self.idmap[next_id] if next_id in self.idmap else None

        return curr

a=Node('a')
b=Node('b')
c=Node('c')
d=Node('d')
e=Node('e')
f=Node('f')

xlist=XorList()
xlist.add(a)
xlist.add(b)
xlist.add(c)
xlist.add(d)
xlist.add(e)
xlist.add(f)
print(xlist)

assert xlist.get(0) == a
assert xlist.get(1) == b
assert xlist.get(2) == c
assert xlist.get(3) == d
assert xlist.get(4) == e
assert xlist.get(5) == f

