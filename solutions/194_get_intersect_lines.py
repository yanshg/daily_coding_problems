#!/usr/bin/python

"""

This problem was asked by Facebook.

Suppose you are given two lists of n points, one list p1, p2, ..., pn on the line y = 0 and the other list q1, q2, ..., qn on the line y = 1. Imagine a set of n line segments connecting each point pi to qi. Write an algorithm to determine how many pairs of the line segments intersect.

"""

# Idea:  Convert this problem to same with 044 to get inversion pairs of an un-sorted list.

#        1. sort (Pi, Qi) list
#        2. unzip the sorted (Pi, Qi) list to get sorted Pi list and un-sorted Qi list.
#        3. then this problem become to search inversion pairs in Qi list that for index i<j and Qi>Qj
#        4, then get inversion numbers with merge sort mechanism

def get_intersect_lines_num(plist,qlist):
    assert len(plist)==len(qlist)

    pqlist=list(zip(plist,qlist))
    pqlist.sort(key=lambda x:x[0])
    
    (p_sorted,q_unsorted)=zip(*pqlist)

    return get_inversions_num(list(q_unsorted))

def merge_inversions(nums,left,right):
    ll,lr=len(left),len(right)
    i,j,k=0,0,0
    inversions=0
    while i<ll and j<lr:
        if left[i] <= right[j]:
            nums[k]=left[i]
            i+=1
        else:
            nums[k]=right[j]
            j+=1
            inversions+=ll-i
        k+=1

    while i<ll:
        nums[k]=left[i]
        i+=1
        k+=1
    while j<lr:
        nums[k]=right[j]
        j+=1
        k+=1
    return inversions

def get_inversions_num(nums):
    l=len(nums)
    if l<=1:
        return 0

    mid=l//2
    left,right=nums[:mid],nums[mid:]
    inversions=get_inversions_num(left)
    inversions+=get_inversions_num(right)
    inversions+=merge_inversions(nums,left,right)
    return inversions

assert get_intersect_lines_num([7,2,4,8,10,6,9],[2,5,4,6,7,8,1])==11

