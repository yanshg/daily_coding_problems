#!/usr/bin/python

"""

This problem was asked by Apple.

A fixed point in an array is an element whose value is equal to its index. Given a sorted array of distinct elements, return a fixed point, if one exists. Otherwise, return False.

For example, given [-6, 0, 2, 40], you should return 2. Given [1, 5, 7, 8], you should return False.

"""

def bruteforce(arr):
    for i,num in enumerate(arr):
        if i == num:
            return i
    return False

# O(logN): Binary search with distinct elements
def get_fixed_point(arr):
    n=len(arr)
    low,high = 0,n-1
    while low <= high:
        mid=(low+high)//2
        if arr[mid] == mid:
            return mid
        elif arr[mid] < mid:
            low = mid + 1
        else:
            high = mid - 1

    return False

# O(logN): Binary search with duplicated elements
#
# Articles:  https://www.geeksforgeeks.org/find-fixed-point-value-equal-index-given-array-duplicates-allowed/
#
# Consider the arr[] = {-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13}, arr[mid] = 3
#
# If elements are not distinct, then we see arr[mid] < mid, we can NOT conclude which side the fixed is on.
# It could be on left side or on the right side.

# We know for sure that since arr[5] = 3, arr[4] couldn't be magic index
# because arr[4] must be less than or equal to arr[5] (the array is Sorted).

# So, the general pattern of our search would be:

#    Left Side: start = start, end = min(arr[midIndex], midIndex-1)
#    Right Side: start = max(arr[midIndex], midIndex+1), end = end

def helper(arr,start,end):
    #print("start: ", start, "end: ", end)
    if start > end:
        return -1

    mid = (start+end)//2
    if arr[mid] == mid:
        return mid

    left = helper(arr, start, min(arr[mid],mid-1))
    if left != -1:
        return left

    return helper(arr, max(arr[mid],mid+1), end)

def get_fixed_point_with_duplicated_elements(arr):
    ret = helper(arr,0,len(arr)-1)
    return ret if ret != -1 else False

assert get_fixed_point([-6, 0, 2, 40]) == 2
assert get_fixed_point([1, 5, 7, 8]) == False
assert get_fixed_point_with_duplicated_elements([-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13]) == 2
