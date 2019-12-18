#!/usr/bin/python

"""
This problem was asked by Microsoft.

Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

    2
    1.5
    2
    3.5
    2
    2
    2

"""

import heapq as hq

def get_running_medians(arr):
    if not arr:
        return None

    min_heap = list()
    max_heap = list()
    medians = list()

    for x in arr:
        hq.heappush(min_heap, x)

        if len(min_heap) > len(max_heap) + 1:
            smallest_large_element = hq.heappop(min_heap)
            hq.heappush(max_heap, -smallest_large_element)

        if len(min_heap) == len(max_heap):
            median = float(min_heap[0] - max_heap[0]) / 2
        else:
            median = min_heap[0]
        medians.append(median)

        print "x: ", x
        print "min_heap", min_heap
        print "max_heap", max_heap
        print "medians", medians
        print "\n"

    return medians


print get_running_medians([2, 5])
print get_running_medians([3, 3, 3, 3])

assert not get_running_medians(None)
assert not get_running_medians([])
assert get_running_medians([2, 5]) == [2, 3.5]
assert get_running_medians([3, 3, 3, 3]) == [3, 3, 3, 3]
assert get_running_medians([2, 1, 5, 7, 2, 0, 5]) == [2, 1.5, 2, 3.5, 2, 2, 2]
