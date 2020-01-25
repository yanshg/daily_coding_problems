#!/usr/bin/python

"""
This problem was asked by Google.

You are given an array of length n + 1 whose elements belong to the set {1, 2, ..., n}. By the pigeonhole principle, there must be a duplicate. Find it in linear time and space.

"""

# Note:

#    1. You must not modify the array (assume the array is read only).
#    2. You must use only constant, O(1) extra space.
#    3. Your runtime complexity should be less than O(n2).
#    4. There is only one duplicate number in the array, but it could be repeated more than once.

# Proved by Pigeonhole principle that at least one of the numbers is duplicated

# Article: https://leetcode.com/articles/find-the-duplicate-number/

# Idea 1: first sort the array, then return the duplicate element as soon as we find it.

# O(nlogn), O(n) space
def find_duplicated1(nums):
    nums1=sorted(nums)
    for i in range(len(nums1)-1):
        if nums1[i]==nums1[i+1]:
            return nums1[i]
    return None

# Idea 2: use set

# O(n), O(n) space
def find_duplicated2(nums):
    seen=set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return None

# Idea 3: Link Cycle Detection (Floyd's Tortoise and Hare)
#         if fast and slow pointer's value is same value, then it get into a cycle
#
# It is easier to understand after converting the array to a singly linked list like below:
#
# index   [0]     [1]     [2]     [3]     [4]     [5]     [6]
# value    2       6       4       1       3       1       5
#
# linked list with cycle:
#
# index   [0]     [2]     [4]     [3]     [1]     [6]
# value    2 ->    4->     3 ->    1 ->    6 ->    5 points by to 1 via index [5]
#
# and it became question #142 (Link Cycle detection problem) from here.
#
# O(n), O(1) space
def find_duplicated3(nums):
    slow,fast=nums[0],nums[0]
    while True:
        slow=nums[slow]
        fast=nums[nums[fast]]
        print("slow:", slow, "fast:", fast)
        if slow==fast:
            break

    # Find the "entrance" to the cycle
    ptr1 = nums[0]
    ptr2 = slow
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]

    return ptr1

# Idea 4:  Iteratively put nums[0] to the correct place so that the value equal to the index;
#          Then 1 to n will be put at index 1 to index n, except for nums[0]

def find_duplicated4(nums):
    while nums[nums[0]] != nums[0]:
        nums[nums[0]],nums[0]=nums[0],nums[nums[0]]
    return nums[0]

assert find_duplicated1([1,3,4,2,2])==2
assert find_duplicated1([3,1,3,4,2])==3

assert find_duplicated2([1,3,4,2,2])==2
assert find_duplicated2([3,1,3,4,2])==3

assert find_duplicated3([1,3,4,2,2])==2
assert find_duplicated3([3,1,3,4,2])==3

assert find_duplicated4([1,3,4,2,2])==2
assert find_duplicated4([3,1,3,4,2])==3


