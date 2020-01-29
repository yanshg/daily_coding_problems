#!/usr/bin/python

"""

This problem was asked by Google.

We can determine how "out of order" an array A is by counting the number of inversions it has. Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j. That is, a smaller element appears after a larger element.

Given an array, count the number of inversions it has. Do this faster than O(N^2) time.

You may assume each element in the array is distinct.

For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), and (4, 3). The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.

"""

# O(N^2)
def bruteforce(nums):
    count,max_so_far=0,0
    for i,num in enumerate(nums):
        max_so_far=max(num,max_so_far)
        if num<max_so_far:
            count+=sum(1 for x in nums[0:i] if x>num)
    return count

# Idea: Get inversions during merge sort procedure
#       inversions=inversions(left_half)+
#                  inversions(right_half)+
#                  inversions(merge left_half and right_half)
# O(NlogN)

def merge(nums,left,right):
    inversions=0
    i,j,k=0,0,0
    len_left,len_right=len(left),len(right)
    while i<len_left and j<len_right:
        if left[i]<=right[j]:
            nums[k]=left[i]
            i+=1
        else:
            nums[k]=right[j]
            j+=1
            inversions+=len_left-i
        k+=1
    while i<len_left:
        nums[k]=left[i]
        i+=1
        k+=1
    while j<len_right:
        nums[k]=right[j]
        j+=1
        k+=1
    return inversions

def get_inversions_with_merge_sort(nums):
    n=len(nums)
    if n<=1:
        return 0

    mid=n//2
    left,right=nums[:mid],nums[mid:]
    inversions=get_inversions_with_merge_sort(left)
    inversions+=get_inversions_with_merge_sort(right)
    inversions+=merge(nums,left,right)

    return inversions

assert bruteforce([2, 4, 1, 3, 5])==3
assert get_inversions_with_merge_sort([2, 4, 1, 3, 5])==3
