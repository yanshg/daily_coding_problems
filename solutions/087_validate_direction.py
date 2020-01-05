#!/usr/bin/python

"""
This problem was asked by Uber.

A rule looks like this:

A NE B

This means this means point A is located northeast of point B.

A SW C

means that point A is southwest of C.

Given a list of rules, check if the sum of the rules validate. For example:

A N B
B NE C
C N A

does not validate, since A cannot be both north and south of C.

A NW B
A N B

is considered valid.
"""

opposites={
    'N': 'S',
    'S': 'N',
    'E': 'W',
    'W': 'E',
}

class Node():
    def __init__(self, val):
        self.val=val
        self.neighbors = {
            'N': set(),
            'S': set(),
            'E': set(),
            'W': set(),
        }

    def __repr__(self):
        return "{}={}".format(self.val,self.neighbors)

    def __hash__(self):
        return hash(self.val)

class Map():
    def add_rule(self, node1, direction, node2):
        for d in direction:
            if node1 in node2.neighbors[d] or \
               node2 in node1.neighbors[opposites[d]]:
                raise Exception

            for nodex in node1.neighbors[d]:
                self.add_rule(nodex, d, node2)

        for d in direction:
            node2.neighbors[d].add(node1)
            node1.neighbors[opposites[d]].add(node2)


A=Node('A')
B=Node('B')
C=Node('C')

m=Map()
try:
    m.add_rule(A, "N", B)
    m.add_rule(B, "NE", C)
    m.add_rule(C, "N", A)
except Exception:
    print("Invalid rule")
