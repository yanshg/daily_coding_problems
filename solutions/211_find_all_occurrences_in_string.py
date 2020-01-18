#!/usr/bin/python

"""

This problem was asked by Microsoft.

Given a string and a pattern, find the starting indices of all occurrences of the pattern in the string. For example, given the string "abracadabra" and the pattern "abr", you should return [0, 7].

"""

def find_all_indices(pattern,string):
    lp,ls=len(pattern),len(string)
    return [ i for i in range(ls-lp+1) if string[i:i+lp] == pattern ]

assert find_all_indices('abr','abracadabra')==[0,7]
assert find_all_indices('abr','abracadabrabr')==[0,7,10]
assert find_all_indices('bab','abababcababrbab')==[1,3,8,12]
