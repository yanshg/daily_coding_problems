#!/usr/bin/python

"""

This problem was asked by Microsoft.

A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.

"""

# Article: https://www.geeksforgeeks.org/n-th-number-whose-sum-of-digits-is-ten/

# all multiples of 9 are present in arithmetic progression 19, 28, 37, 46, 55, 64, 73, 82, 91, 100, 109, ...

def sum_digits(n):
    if n==0:
        return 0

    return n%10+sum_digits(n//10)

def get_nth_perfect_number(n):
    count,num=0,19
    while True:
        if sum_digits(num)==10:
            count+=1
        if count==n:
            return num
        num+=9
    return -1

assert get_nth_perfect_number(1)==19
assert get_nth_perfect_number(2)==28
assert get_nth_perfect_number(3)==37
