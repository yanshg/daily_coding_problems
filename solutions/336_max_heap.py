#!/usr/bin/python

"""

This problem was asked by Microsoft.

Write a program to determine how many distinct ways there are to create a max heap from a list of N given integers.

For example, if N = 3, and our integers are [1, 2, 3], there are two ways, shown below.

  3      3
 / \    / \
1   2  2   1

"""

# Idea:   T(N) = C(N, L) * T(L) * T(R)
#         L + R + 1 = N
#     =>  T(N) = C(N, L) * T(L) * T(N-1-L)

# Binary Heap is complete binary tree.
#
#     height:       h = log2(N)
#     Total Nodes:  total = 2^h - 1 = 2^0 + 2^1 + ... + 2^(h-1)
