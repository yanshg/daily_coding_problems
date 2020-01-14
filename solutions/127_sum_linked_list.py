#!/usr/bin/python

"""
This problem was asked by Microsoft.

Let's represent an integer in a linked list format by having each node represent a digit in the number. The nodes make up the number in reversed order.

For example, the following linked list:

    1 -> 2 -> 3 -> 4 -> 5

    is the number 54321.

    Given two linked lists in this format, return their sum in the same linked list format.

    For example, given

    9 -> 9

    5 -> 2

    return 124 (99 + 25) as:

    4 -> 2 -> 1

"""

class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

    def __repr__(self):
        return "{}->{}".format(self.val,self.next)

def convert_num_to_list(num):
    first=None
    prev=None
    while(num):
        digit=num%10
        num//=10
        node=Node(digit)
        if not first:
            first=node
        if prev:
            prev.next=node
        prev=node
    return first

def convert_list_to_num(head):
    cur=head
    num=0
    factor=1

    while(cur):
        num+=cur.val * factor
        cur=cur.next
        factor*=10

    return num

def add_nums_helper(link1,link2,sum_node,carry,level):
    if not link1 and not link2:
        if carry:
            if level:
                new_node=Node(carry)
                sum_node.next=new_node
            else:
                sum_node.val=carry
        return

    cur1=None
    num1=0
    if link1:
        num1=link1.val
        cur1=link1.next

    cur2=None
    num2=0
    if link2:
        num2=link2.val
        cur2=link2.next

    sum_val=num1+num2+carry
    carry=0
    if sum_val>10:
        sum_val-=10
        carry=1

    if level:
        new_node=Node(sum_val)
        sum_node.next=new_node
        sum_node=new_node
    else:
        sum_node.val=sum_val

    level+=1

    add_nums_helper(cur1,cur2,sum_node,carry,level)

def add_nums(link1,link2):
    sum_node=Node(0)
    add_nums_helper(link1,link2,sum_node,0,0)
    return sum_node

assert convert_list_to_num(convert_num_to_list(25))==25
assert convert_list_to_num(convert_num_to_list(124))==124
assert convert_list_to_num(add_nums(convert_num_to_list(99),convert_num_to_list(25)))==124
assert convert_list_to_num(add_nums(convert_num_to_list(1000),convert_num_to_list(1)))==1001

