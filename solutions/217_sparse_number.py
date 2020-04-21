#!/usr/bin/python

"""

This problem was asked by Oracle.

We say a number is sparse if there are no adjacent ones in its binary representation. For example, 21 (10101) is sparse, but 22 (10110) is not. For a given input N, find the smallest sparse number greater than or equal to N.

Do this in faster than O(N log N) time.

"""

def get_next_sparse_number(n):
    while True:
        addition=n&(n>>1)
        if addition==0:
            break
        n+=addition
    return n

assert get_next_sparse_number(4)==4
assert get_next_sparse_number(6)==8
assert get_next_sparse_number(38)==40
assert get_next_sparse_number(44)==64
