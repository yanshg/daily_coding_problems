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

# Idea: prepare 2 heaps, one min heap for larger numbers with ascending order,
#                        one max heap for smaller numbers with descending order.
#
#                                  |--> H1, H2, H3 ...     (min heap with ascending order)
#     An, An-1, ... A2, A1, A0 --> |
#                                  |--> M1, M2, M3 ...     (max heap with descending order)
#
#     First always push the new coming number to min heap,
#     Then adjust to push the min_heap[0] to max heap to make the heaps balanced.
#
#   How to prove it works:
#
#   For a balanced min and max heaps:  H1<H2<H3, and M1>M2>M3, and H1>M1.
#   For new number A0, after add it to the heaps and make them balanced,
#   Need prove still min_heap[0] > max_heap[0] for the following cases:
#      1. A0 >= H1
#      2. M1 =< A0 < H1
#      3. A0 =< M1 < H1
#

import heapq

def get_running_medians(arr):
    if not arr:
        return None

    min_heap = list()
    max_heap = list()
    medians = list()

    for x in arr:
        heapq.heappush(min_heap, x)

        if len(min_heap) > len(max_heap) + 1:
            smallest_large_element = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -smallest_large_element)

        if len(min_heap) == len(max_heap):
            median = float(min_heap[0] - max_heap[0]) / 2
        else:
            median = min_heap[0]

        medians.append(median)

    #print("medians:", medians)
    return medians


assert not get_running_medians(None)
assert not get_running_medians([])
assert get_running_medians([2, 5]) == [2, 3.5]
assert get_running_medians([3, 3, 3, 3]) == [3, 3, 3, 3]
assert get_running_medians([2, 1, 5, 7, 2, 0, 5]) == [2, 1.5, 2, 3.5, 2, 2, 2]
