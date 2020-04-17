#!/usr/bin/python

"""

This problem was asked by Amazon.

Given a linked list, remove all consecutive nodes that sum to zero. Print out the remaining nodes.

For example, suppose you are given the input 3 -> 4 -> -7 -> 5 -> -6 -> 6. In this case, you should first remove 3 -> 4 -> -7, then -6 -> 6, leaving only 5.

"""

# Article: https://snowan.gitbook.io/study-notes/leetcode/english-solution/1171.remove-zero-sum-consecutive-nodes-from-linked-list-en

# Idea:  This problem is typical prefixSum problem, if prefixSum seen, then all elements between two same prefixSum sum = 0.
#
#        Here, we can use HashMap, key as prefixSum, value as current Node
#        If prefixSum already seen in HashMap, then delete all nodes between two same prefixSum.
#        and also delete relative prefixSum in HashMap.

class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

    def __repr__(self):
        return "{}->{}".format(self.val,self.next)

def generate_list(values):
    head,next=None,None
    for val in reversed(values):
        head=Node(val,next)
        next=head
    return head

def get_list_values(head):
    values=[]
    while head:
        values.append(head.val)
        head=head.next
    return values

def trim_zero_sum_nodes(head):
    dummy=Node(0)
    dummy.next=head

    hash_sums=dict()

    sum=0
    hash_sums[0]=dummy

    # get sums
    curr=head
    while curr:
        sum+=curr.val
        if sum in hash_sums:
            prev=hash_sums[sum]

            # remove nodes from prev.next to curr
            new_curr=prev.next
            new_sum=sum
            while new_curr!=curr:
                new_sum+=new_curr.val
                del hash_sums[new_sum]
                new_curr=new_curr.next

            prev.next=curr.next
        else:
            hash_sums[sum]=curr

        curr=curr.next

    return dummy.next

l=generate_list([3,4,-7,5,-6,6])
print(l)
assert get_list_values(trim_zero_sum_nodes(generate_list([3,4,-7,5,-6,6])))==[5]
