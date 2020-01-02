#!/usr/bin/python

"""

This problem was asked by Amazon.

Given a string s and an integer k, break up the string into multiple lines such that each line has a length of k or less. You must break it up so that words don't break across lines. Each line has to have the maximum possible amount of words. If there's no way to break the text up, then return null.

You can assume that there are no spaces at the ends of the string and that there is exactly one space between each word.

For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, you should return: ["the quick", "brown fox", "jumps over", "the lazy", "dog"]. No string in the list has a length of more than 10.

"""

def helper(words,k,lines=[]):
    if not words:
        return lines

    i,l=0,0
    for word in words:
        l+=len(word)
        if l>k:
            break
        i+=1
        l+=1

    if i==0:
        return None

    return helper(words[i:],k,lines+[ ' '.join(words[:i]) ])

def break_string_into_lines(string,k):
    if not string:
        return None

    words=string.split()
    return helper(words,k,[])

assert break_string_into_lines("the quick brown fox jumps over the lazy dog",10)==["the quick", "brown fox", "jumps over", "the lazy", "dog"]
assert break_string_into_lines("the quick brown fox jumpsovert the lazy dog",10)==["the quick", "brown fox", "jumpsovert", "the lazy", "dog"]
assert not break_string_into_lines("the quick brown foxjumpsover the lazy dog",10)

