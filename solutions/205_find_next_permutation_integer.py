#!/usr/bin/python

"""

This problem was asked by IBM.

Given an integer, find the next permutation of it in absolute order. For example, given 48975, the next permutation would be 49578.

"""

# Idea:  convert the number to gidit list, then use the solution of 095 to get next permutation, then convert back to number


def get_digit_list(num):
    return list(map(int, list(str(num))))

def get_number_from_digit_list(digits):
    return int(''.join(map(str,digits)))

def get_next_permutation_integer(num):
    if 0<=num<=9:
        return num

    digits=get_digit_list(num)
    l=len(digits)

    i=l-1
    while i>0 and digits[i]<=digits[i-1]:
        i-=1

    if i>0:
        j,pivot=l-1,i-1
        while digits[j]<=digits[pivot]:
            j-=1
        digits[pivot],digits[j]=digits[j],digits[pivot]

    digits[i:]=reversed(digits[i:])

    return get_number_from_digit_list(digits)

assert get_next_permutation_integer(48975)==49578
