#!/usr/bin/python

"""

This problem was asked by Quantcast.

You are presented with an array representing a Boolean expression. The elements are of two kinds:

    T and F, representing the values True and False.
    &, |, and ^, representing the bitwise operators for AND, OR, and XOR.

Determine the number of ways to group the array elements using parentheses so that the entire expression evaluates to True.

For example, suppose the input is ['F', '|', 'T', '&', 'T']. In this case, there are two acceptable groupings: (F | T) & T and F | (T & T).

"""

# Backtracking

def operate(bool1,bool2,op):
    b1=False if bool1=='F' else True
    b2=False if bool2=='F' else True
    if op=='&':
        return b1 & b2
    elif op=='|':
        return b1 | b2
    elif op=='^':
        return b1 ^ b2

def get_bool_str(boolv):
    return 'T' if boolv else 'F'

def get_bools_groupings(bools_ops):
    n=len(bools_ops)
    if n==1:
        return 1 if bools[0] else 0
    elif n<3:
        return 0

    count=0
    new=get_bool_str(operate(bools_ops[0],bools_ops[1],op))
    count+=helper(bools_ops[:i]+[new]+bools_ops[i+2:],bools_ops[:k]+bools_ops[k+1:])
    return count

assert get_bools_groupings(['F', '|', 'T', '&', 'T'])==2
