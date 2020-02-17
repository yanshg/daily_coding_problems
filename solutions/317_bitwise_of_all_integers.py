#!/usr/bin/python

"""

This problem was asked by Yahoo.

Write a function that returns the bitwise AND of all integers between M and N, inclusive.

"""


# Article:  https://en.wikipedia.org/wiki/Two%27s_complement

#  The two's complement is calculated by inverting the digits and adding one
#
#  For example: three-bit number 010, the two's complement is 110, because 010 + 110 = 1000.

def and_all_integers(m,n):
    assert m<n

    result=~0
    for i in range(m, n+1):
        result &= i

    return result

# bit-wise & of all numbers from x to y.  
def and_operator(a, b): 
    while(a < b): 
        # -b is the 2's complement of b  
        # when do bitwise or with b we 
        # get LSB and we subtract that from b  
        b -= (b & -b)  
    return b  

assert and_all_integers(12,15)==12
assert and_all_integers(10,20)==0
assert and_operator(12,15)==12
assert and_operator(10,20)==0
