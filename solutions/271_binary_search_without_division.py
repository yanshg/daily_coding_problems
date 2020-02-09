#!/usr/bin/python

"""

This problem was asked by Netflix.

Given a sorted list of integers of length N, determine if an element x is in the list without performing any multiplication, division, or bit-shift operations.

Do this in O(log N) time.

"""

# Idea:  Use binary search but replace "length//2" operation with division by 2 algorithm described in:
#        https://en.wikipedia.org/wiki/Division_by_two#Decimal


def div_by_two(num):
    return num//2

def div_by_two_oddeven(num):
    if num==0:
        return 0

    num_str='0'+str(num)

    result=''
    for i in range(1,len(num_str)):
        prev,curr=num_str[i-1],num_str[i]
        if prev in '13579':
            if curr in '01':
                result+='5'
            elif curr in '23':
                result+='6'
            elif curr in '45':
                result+='7'
            elif curr in '67':
                result+='8'
            elif curr in '89':
                result+='9'
        elif prev in '02468':
            if curr in '01':
                result+='0'
            elif curr in '23':
                result+='1'
            elif curr in '45':
                result+='2'
            elif curr in '67':
                result+='3'
            elif curr in '89':
                result+='4'

    return int(result)

def binary_search(nums, x):
    low,high=0,len(nums)-1
    while low<=high:
        mid=div_by_two_oddeven(low+high)
        if nums[mid]==x:
            return True
        elif nums[mid]<x:
            low=mid+1
        else:
            high=mid-1
    return False

assert div_by_two_oddeven(7)==3
assert div_by_two_oddeven(17)==8
assert binary_search([3,5,23,47,58,121], 23)
assert not binary_search([3,5,23,47,58,121], 24)
