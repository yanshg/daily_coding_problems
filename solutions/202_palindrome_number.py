#!/usr/bin/python

"""

This problem was asked by Palantir.

Write a program that checks whether an integer is a palindrome. For example, 121 is a palindrome, as well as 888. 678 is not a palindrome. Do not convert the integer into a string.

"""

FACTOR=10

def helper(num,size):
    if size==1:
        return True

    biggest_factor=FACTOR ** (size-1)
    smallest_factor=FACTOR

    left_digit=num//biggest_factor
    right_digit=num%smallest_factor
    if left_digit!=right_digit:
        return False

    if size<=3:
        return True

    # get the middle digits
    num-=left_digit*biggest_factor
    num=num//smallest_factor
    return helper(num, size-2)

def get_number_length(num):
    size=0
    while num:
        num=num//10
        size+=1
    return size

def is_palindrome_number(num):
    size=get_number_length(num)
    return helper(num,size)

assert is_palindrome_number(5)
assert is_palindrome_number(11)
assert is_palindrome_number(121)
assert is_palindrome_number(12321)
assert is_palindrome_number(123321)
assert not is_palindrome_number(123311)
assert not is_palindrome_number(123121)
