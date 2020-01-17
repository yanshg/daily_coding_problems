#!/usr/bin/python

"""
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""

def findMissingPositive(arr, n):

    # Default smallest Positive Integer
    m = 1

    # Store values in set which are
    # greater than variable m
    x = []
    for i in range(n):

        # Store value when m is less than
        # current index of given array
        if (m < arr[i]):
            x.append(arr[i])

        elif (m == arr[i]):

            # Increment m when it is equal
            # to current element
            m = m + 1

            while (x.count(m)):
                x.remove(m)

                # Increment m when it is one of the
                # element of the set
                m = m + 1

    # Return the required answer
    return m

def find_first_missing_positive_integer(arr):
    return findMissingPositive(arr,len(arr))

assert find_first_missing_positive_integer([3, 4, -1, 1])==2
assert find_first_missing_positive_integer([1, 2, 0])==3
assert find_first_missing_positive_integer([1, 2, 5]) == 3
assert find_first_missing_positive_integer([1]) == 2
assert find_first_missing_positive_integer([-1, -2]) == 1
assert find_first_missing_positive_integer([]) == 1
