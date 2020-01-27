#!/usr/bin/python

"""
This problem was asked by Google.

Given a string, split it into as few strings as possible such that each string is a palindrome.

For example, given the input string racecarannakayak, return ["racecar", "anna", "kayak"].

Given the input string abc, return ["a", "b", "c"].

"""

def is_palindrome(s):
    return bool(s) and s==s[::-1]

def helper(s,curr='',pals_so_far=[]):
    if not s:
        #print("curr: ",curr, "pals_so_far: ",pals_so_far)
        return pals_so_far if not curr else pals_so_far + list(curr)

    candidate=curr+s[0]
    
    pals_with_candidate=[]
    if is_palindrome(candidate):
        pals_with_candidate=helper(s[1:],'',pals_so_far+[candidate])
    pals_without_candidate=helper(s[1:],candidate,pals_so_far)

    return pals_with_candidate if bool(pals_with_candidate) and len(pals_with_candidate) < len(pals_without_candidate) else pals_without_candidate

def split_to_palindrome_strs(s):
    return helper(s,'',[])

assert split_to_palindrome_strs("racecarannakayak") == ["racecar", "anna", "kayak"]
assert split_to_palindrome_strs("abc") == ["a", "b", "c"]
