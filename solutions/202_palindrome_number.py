#!/usr/bin/python

"""

This problem was asked by Palantir.

Write a program that checks whether an integer is a palindrome. For example, 121 is a palindrome, as well as 888. 678 is not a palindrome. Do not convert the integer into a string.

"""

def get_reverse_num(num):
    reverse_num = 0
    while num:
        reverse_num = (reverse_num * 10) + (num % 10)
        num = num // 10

    return reverse_num

def is_palindrome_number(num):
    return num == get_reverse_num(num)

assert is_palindrome_number(5)
assert is_palindrome_number(11)
assert is_palindrome_number(121)
assert is_palindrome_number(12321)
assert is_palindrome_number(123321)
assert not is_palindrome_number(123311)
assert not is_palindrome_number(123121)
