#!/usr/bin/python

"""

This problem was asked by Facebook.

Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

You can assume the list has at least three integers.

"""

# O(n^3)
def bruteforce(nums):
    n=len(nums)
    if n<3:
        return 0

    max_product=0
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                max_product=max(max_product, nums[i]*nums[j]*nums[k])

    return max_product

# O(nlogn) time, O(1) space
def get_largest_product_with_sort(nums):
    nums.sort()
    return max((nums[-3]*nums[-2]*nums[-1]), (nums[0]*nums[1]*nums[-1]))

# O(n) time, O(1) space
# get last max 3 items and first min 2 items
import sys
def get_largest_product(nums):
    n=len(nums)
    if n<3:
        return 0

    maxsize=sys.maxsize
    maxa,maxb,maxc=-maxsize,-maxsize,-maxsize
    mina,minb=maxsize,maxsize
    for n in nums:
        if n>maxa:
            maxc=maxb
            maxb=maxa
            maxa=n
        elif n>maxb:
            maxc=maxb
            maxb=n
        elif n>maxc:
            maxc=n
        if n<mina:
            minb=mina
            mina=n
        elif n<minb:
            minb=n

    return max(maxa*maxb*maxc, mina*minb*maxa)

assert bruteforce([-10, -10, 5, 2]) == 500
assert get_largest_product_with_sort([-10, -10, 5, 2]) == 500
assert get_largest_product([-10, -10, 5, 2]) == 500

