#!/usr/bin/python

"""
This problem was asked by Facebook.

You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.

Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.

"""

"""
Idea: An Efficient Solution is to pre-compute highest bar on left and right of every bar in O(n) time. Then use these pre-computed values to find the amount of water in every array element.
"""

def get_trapped_water(arr):

    n=len(arr)

    # left[i] contains height of tallest bar to the
    # left of i'th bar including itself
    left = [0]*n

    # Right [i] contains height of tallest bar to
    # the right of ith bar including itself
    right = [0]*n

    # Fill left array
    left[0] = arr[0]
    for i in range( 1, n):
        left[i] = max(left[i-1], arr[i])

    # Fill right array
    right[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        right[i] = max(right[i + 1], arr[i]);

    # Calculate the accumulated water element by element
    # consider the amount of water on i'th bar, the
    # amount of water accumulated on this particular
    # bar will be equal to min(left[i], right[i]) - arr[i] .
    water = 0
    for i in range(0, n):
        water += min(left[i], right[i]) - arr[i]

    return water


"""
Space Optimization in above solution: Instead of maintaing two arrays of size n for storing left and right max of each element, we will just maintain two variables to store the maximum till that point. Since water trapped at any element = min( max_left, max_right) – arr[i] we will calculate water trapped on smaller element out of A[lo] and A[hi] first and move the pointers till lo doesn’t cross hi.

Only the first and last element determine if the water trapped.  the higher or lower for the median elements does not matter. so it is enough just need store the left max and right max.
"""
def get_trapped_water_optimized(arr):
    # initialize output
    result = 0

    # maximum element on left and right
    left_max = 0
    right_max = 0

    # indices to traverse the array
    n = len(arr)
    lo = 0
    hi = n-1

    while(lo <= hi):
        if(arr[lo] < arr[hi]):
            if(arr[lo] > left_max):
                # update max in left
                left_max = arr[lo]
            else:
                # water on curr element = max - curr
                result += left_max - arr[lo]
            lo+= 1
        else:
            if(arr[hi] > right_max):
                # update right maximum
                right_max = arr[hi]
            else:
                result += right_max - arr[hi]
            hi-= 1
    return result

assert get_trapped_water([2, 1, 2])==1
assert get_trapped_water([3, 0, 1, 3, 0, 5])==8
assert get_trapped_water_optimized([2, 1, 2])==1
assert get_trapped_water_optimized([3, 0, 1, 3, 0, 5])==8
assert get_trapped_water_optimized([3, 0, 8, 3, 0, 5])==8
