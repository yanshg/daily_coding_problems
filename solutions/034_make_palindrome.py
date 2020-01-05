#!/usr/bin/python

"""

This problem was asked by Quora.

Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).

For example, given the string "race", you should return "ecarace", since we can add three letters to it (which is the smallest amount to make a palindrome). There are seven other palindromes that can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.

As another example, given the string "google", you should return "elgoogle".

"""

# Idea:  use danymic programming:
#        get possible palindrome for s[1:], s[:-1], and s[1:-1]

def is_palindrome(s):
    return s==s[::-1]

def make_palindrome(s):
    if is_palindrome(s):
        return s

    if s[0]==s[-1]:
        return s[0]+make_palindrome(s[1:-1])+s[-1]
    else:
        p1=s[0]+make_palindrome(s[1:])+s[0]
        p2=s[-1]+make_palindrome(s[:-1])+s[-1]
        l1,l2=len(p1),len(p2)
        if l1==l2:
            return p1 if p1<p2 else p2
        return p1 if l1<l2 else p2

assert make_palindrome('race')=="ecarace"
assert make_palindrome('google')=="elgoogle"

