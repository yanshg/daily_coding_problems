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

# Idea: Use 'mid' pointer to determine if swap lower or higher
#
#       |   <pivot   |    =pivot   |         partitioning          |   >pivot    |
#       |------------|-|-----------|-|---------------------------|-|-------------|
#                    low           mid                           high
#
# arr[:low]:        Items < pivot
# arr[low:mid]:     Items == pivot
# arr[mid]:         Item > pivot
# arr[mid:high+1]:  Unknown for partition
# arr[high]         Item <= pivot
# arr[high+1:]:     Item > pivot
#

def bruteforce(nums,pivot):
    list1=[num for num in nums if num<pivot]
    list2=[num for num in nums if num==pivot]
    list3=[num for num in nums if num>pivot]
    return list1+list2+list3

def partition_with_pivot(nums,pivot):
    low,mid,high=0,0,len(nums)-1
    while mid<=high:
        if nums[mid]<pivot:
            nums[low],nums[mid]=nums[mid],nums[low]
            low+=1
            mid+=1
        elif nums[mid]==pivot:
            mid+=1
        elif nums[high]>pivot:
            high-=1
        else:
            nums[mid],nums[high]=nums[high],nums[mid]
            high-=1
    return nums

assert bruteforce([9, 12, 3, 5, 14, 10, 10], 10)==[9, 3, 5, 10, 10, 12, 14]
assert partition_with_pivot([9, 12, 3, 5, 14, 10, 10], 10)==[9, 3, 5, 10, 10, 14, 12]
