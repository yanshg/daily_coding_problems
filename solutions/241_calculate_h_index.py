#!/usr/bin/python

"""

This problem was asked by Palantir.

In academia, the h-index is a metric used to calculate the impact of a researcher's papers. It is calculated as follows:

A researcher has index h if at least h of her N papers have h citations each. If there are multiple h satisfying this formula, the maximum is chosen.

For example, suppose N = 5, and the respective citations of each paper are [4, 3, 0, 1, 5]. Then the h-index would be 3, since the researcher has 3 papers with at least 3 citations.

Given a list of paper citations of a researcher, calculate their h-index.

"""

# Article: https://en.wikipedia.org/wiki/H-index
#
# We compute the h-index as follows:
#
#     1. First we order the values of f from the largest to the lowest value.
#     2. Then, we look for the last position in which f is greater than or equal to the position (we call h this position).
#
#     h-index(f) = max(min(f(i),i))
#
# For example:
#
# If a researcher with 5 publications A, B, C, D, and E with 10, 8, 5, 4, and 3 citations, respectively,
# then the h-index is equal to 4 because the 4th publication has 4 citations and the 5th has only 3.
#
# If the same publications have 25, 8, 5, 3, and 3 citations, then the index is 3 because the fourth paper has only 3 citations.
#
#    f(A)=10, f(B)=8, f(C)=5, f(D)=4, f(E)=3　-> h-index=4
#    f(A)=25, f(B)=8, f(C)=5, f(D)=3, f(E)=3　-> h-index=3

def h_index(citations):
    citations.sort(reverse=True)
    h_index=None
    for i,c in enumerate(citations):
        if c>=i+1:
            h_index=i+1
    return h_index

assert h_index([10, 8, 5, 4, 3]) == 4
assert h_index([25, 8, 5, 3, 3]) == 3
assert h_index([4, 3, 0, 1, 5]) == 3
assert h_index([4, 1, 0, 1, 1]) == 1
assert h_index([4, 4, 4, 5, 4]) == 4
assert h_index([4, 1, 0, 2, 3]) == 2
