#!/usr/bin/python

"""
This problem was asked by Amazon.

Given a pivot x, and a list lst, partition the list into three parts.

    The first part contains all elements in lst that are less than x
    The second part contains all elements in lst that are equal to x
    The third part contains all elements in lst that are larger than x

Ordering within a part can be arbitrary.

For example, given x = 10 and lst = [9, 12, 3, 5, 14, 10, 10], one partition may be [9, 3, 5, 10, 10, 12, 14].
"""

def bruteforce(nums,pivot):
    list1=[num for num in nums if num<pivot]
    list2=[num for num in nums if num==pivot]
    list3=[num for num in nums if num>pivot]
    return list1+list2+list3

def partition(nums,pivot,start,end):
    left,right=start,end
    while left<=right:
        while nums[left]<pivot:
            left+=1
        while nums[right]>pivot:
            right-=1

        if left<=right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1
    return left

def pivot_sort(nums,pivot):
    left=partition(nums,pivot,0,len(nums)-1)
    partition(nums,pivot,0,left-2)
    return nums

assert bruteforce([9, 12, 3, 5, 14, 10, 10], 10)==[9, 3, 5, 10, 10, 12, 14]
assert pivot_sort([9, 12, 3, 5, 14, 10, 10], 10)==[9, 5, 3, 10, 10, 14, 12]
