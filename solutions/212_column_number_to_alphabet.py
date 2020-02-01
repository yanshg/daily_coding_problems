#!/usr/bin/python

"""

This problem was asked by Dropbox.

Spreadsheets often use this alphabetical encoding for its columns: "A", "B", "C", ..., "AA", "AB", ..., "ZZ", "AAA", "AAB", ....

Given a column number, return its alphabetical column id. For example, given 1, return "A". Given 27, return "AA".

"""

def convert_number_to_alphabet(num):
    result=''
    while num:
        c=chr(ord('A')+(num-1)%26)
        result=c+result
        num=(num-1)//26

    return result

assert convert_number_to_alphabet(1)=='A'
assert convert_number_to_alphabet(20)=='T'
assert convert_number_to_alphabet(26)=='Z'
assert convert_number_to_alphabet(27)=='AA'
assert convert_number_to_alphabet(28)=='AB'
assert convert_number_to_alphabet(676)=='YZ'
assert convert_number_to_alphabet(705)=='AAC'

