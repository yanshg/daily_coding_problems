#!/usr/bin/python

"""

This problem was asked by Amazon.

Given n numbers, find the greatest common denominator between them.

For example, given the numbers [42, 56, 14], return 14.

"""

def get_gcd(x,y):
    if x<y:
        x,y=y,x

    while y:
        x,y=y,y%x

    return x

def get_gcd_from_numbers(nums):
    if not nums:
        return 1

    l=len(nums)
    if l==1:
        return nums[0]

    gcd=nums[0]
    for i in range(1,l):
        gcd=get_gcd(gcd, nums[i])

    return gcd

assert get_gcd_from_numbers([ 42, 56, 14 ])==14
