#!/usr/bin/python

"""

This problem was asked by Google.

UTF-8 is a character encoding that maps each symbol to one, two, three, or four bytes.

For example, the Euro sign, corresponds to the three bytes 11100010 10000010 10101100. The rules for mapping characters are as follows:

    For a single-byte character, the first bit must be zero.
    For an n-byte character, the first byte starts with n ones and a zero. The other n - 1 bytes all start with 10.

Visually, this can be represented as follows.

 Bytes   |           Byte format
-----------------------------------------------
   1     | 0xxxxxxx
   2     | 110xxxxx 10xxxxxx
   3     | 1110xxxx 10xxxxxx 10xxxxxx
   4     | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

Write a program that takes in an array of integers representing byte values, and returns whether it is a valid UTF-8 encoding.

"""

def is_valid_utf8(arr):
    if not arr:
        return True

    first=arr[0]
    if first>>7==0:
        # ASCII
        count=1
    elif first>>5==0b110:
        count=2
    elif first>>4==0b1110:
        count=3
    elif first>>3==0b11110:
        count=4
    else:
        return False

    if len(arr)<count:
        return False
    
    for i in range(1,count):
        if arr[i]>>6!=0b10:
            return False

    return is_valid_utf8(arr[count:])

assert is_valid_utf8([56,45]) 
assert is_valid_utf8([226, 130, 172])
assert not is_valid_utf8([226, 194, 172])
assert not is_valid_utf8([226])
assert is_valid_utf8([100])
assert is_valid_utf8([194, 130])
