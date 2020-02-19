#!/usr/bin/python

"""

This problem was asked by Pivotal.

Write an algorithm that finds the total number of set bits in all integers between 1 and N.

"""

# n&(n-1):           reset the rightmost 1 bit to 0.
# n&~(n-1) or n&-n:  only keep the rightmost 1 bit, others reset to 0.
# -n:                reverse all bits, then add 1.  for example, -3 = -011 = 100 + 1 = 101

def count_bits(n):
    count=0
    while n:
        n&=n-1
        count+=1
    return count

# O(n*k)  k: bits length
def count_bits_from_one(n):
    return sum([count_bits(i) for i in range(1,n+1)])

assert count_bits_from_one(3)==4


# Idea:  count 1 bits with columns
#
#        A B C D E F G H
#   0:   0 0 0 0 0 0 0 0
#   1:   0 0 0 0 0 0 0 1
#   2:   0 0 0 0 0 0 1 0
#   3:   0 0 0 0 0 0 1 1
#   4:   0 0 0 0 0 1 0 0 
#   5:   0 0 0 0 0 1 0 1
#   6:   0 0 0 0 0 1 1 0
#   7:   0 0 0 0 0 1 1 1
#   8:   0 0 0 0 1 0 0 0
#
#   H column, 1 occur once every 2   
#   G column, 1 occur twice every 4   
#   F column, 1 occur four every 8   

def count_bits_from_one_new(n):
    # Add the zero line
    n+=1

    # the rightmost column
    count=n//2

    # From the second rightmost column
    powerof2=2
    while powerof2 <= n:
        pairs=n//powerof2
        count+=(pairs//2) * powerof2
        if (pairs & 1) : 
            count += (n % powerof2) 

        powerof2<<=1
    return count

assert count_bits_from_one_new(3)==4
