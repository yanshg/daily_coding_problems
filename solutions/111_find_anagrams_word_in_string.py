#!/usr/bin/python

"""
This problem was asked by Google.

Given a word W and a string S, find all starting indices in S which are anagrams of W.

For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.
"""

from collections import Counter

def is_anagrams(word1,word2):
    return word1==word2 or Counter(word1)==Counter(word2)

def bruteforce(string,word):
    ls,lw=len(string),len(word)
    return [ i for i in range(ls-lw+1) if is_anagrams(string[i:i+lw],word) ]

def reduce_count(counter,char):
    if char in counter:
        counter[char]-=1
        if counter[char]<=0:
            del counter[char]

def add_count(counter,char):
    if char in counter:
       counter[char]+=1
    else:
       counter[char]=1

def find_anagram_words_in_string(string,word):
    results=[]

    ls,lw=len(string),len(word)
    counter=Counter(word)

    for i in range(lw):
        reduce_count(counter,string[i])

    if not counter:
        results.append(0)

    for i in range(lw,ls):
        old_char=string[i-lw]
        if old_char in word:
            add_count(counter,old_char)
        reduce_count(counter,string[i])
        if not counter:
            results.append(i-lw+1)

    return results 

assert bruteforce('abxaba', 'ab')==[0,3,4]
assert find_anagram_words_in_string('abxaba', 'ab')==[0,3,4]
