#!/usr/bin/python

"""
This problem was asked by Google.

Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.

"""

class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

    def __repr__(self):
        return "{}->{}".format(self.val,self.next)

# Idea: connect the lists. 'List1 + List2' should have intersecting node with 'List2 + List1'
#       List1= A1 + C1
#       List2= BB1 + C1
#       List1 + List2 = A1 + C1 + BB1 + C1
#       List2 + List1 = BB1 + C1 + A1 + C1

def get_intersect_node(list1,list2):

    # handle cases that one of list is None
    p1,p2=(list1,list2) if list1 and list2 else (None,None)
    connected1,connected2=False,False

    while p1 and p2 and p1!=p2:
        p1=p1.next
        p2=p2.next

        # when reach the end of the 2 lists, p1 and p2 should be both None.
        if not p1 and not connected1:
            # connect list1 to list2
            p1=list2
            connected1=True

        if not p2 and not connected2:
            # connect list2 to list1
            p2=list1
            connected2=True

    return p1

node3=Node(3)
node7=Node(7)
node8=Node(8)
node10=Node(10)
node99=Node(99)
node1=Node(1)

node3.next=node7
node7.next=node8
node8.next=node10
list1=node3

node99.next=node1
node1.next=node8
list2=node99

print("list1:", list1)
print("list2:", list2)
assert get_intersect_node(list1,list2)==node8
