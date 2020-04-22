#!/usr/bin/python

"""

This problem was asked by Zillow.

Let's define a "sevenish" number to be one which is either a power of 7, or the sum of unique powers of 7. The first few sevenish numbers are 1, 7, 8, 49, and so on. Create an algorithm to find the nth sevenish number.This problem was asked by Zillow.

"""

# Idea:  convert N to binary mode
#
#        1st:  001:      1*7^0
#        2nd:  010:      0*7^0 + 1*7^1
#        3rd:  011:      1*7^0 + 1*7^1
#        4th:  100:      1*7^2
#        5th:  101:      1*7^0 + 1*7^2
#        6th:  110:      1*7^1 + 1*7^2

def get_sevenish_number(n):
    result=0
    bit_pos=0
    while n:
        if n&1:
            result+=7**bit_pos
        n>>=1
        bit_pos+=1
    return result

assert get_sevenish_number(1)==1
assert get_sevenish_number(2)==7
assert get_sevenish_number(3)==8
assert get_sevenish_number(4)==49
assert get_sevenish_number(5)==50
assert get_sevenish_number(6)==56
