#!/usr/bin/python

"""
Given a list, sort it using this method: reverse(lst, i, j), which reverses lst from i to j.

"""

# Idea:  extended bubble sort

def reverse_list(lst,i,j):
    assert i>=0 and i<j and j<len(lst)
    lst[i:j]=reversed(list[i:j])

def sort_with_reverse(lst):
    l=len(lst)
    for i in range(l):

