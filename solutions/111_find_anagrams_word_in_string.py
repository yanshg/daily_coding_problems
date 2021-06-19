#!/usr/bin/python

"""
This problem was asked by Google.

Given a word W and a string S, find all starting indices in S which are anagrams of W.

For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.
"""

from collections import Counter,defaultdict

def is_anagrams(word1,word2):
    return word1==word2 or Counter(word1)==Counter(word2)

def bruteforce(string,word):
    ls,lw=len(string),len(word)
    return [ i for i in range(ls-lw+1) if is_anagrams(string[i:i+lw],word) ]

def reduce_count(counter,char):
    counter[char]-=1
    if counter[char]==0:
        del counter[char]

def add_count(counter,char):
    counter[char]+=1
    if counter[char]==0:
        del counter[char]

def find_anagram_words_in_string(string,word):
    counter=defaultdict(int)
    lw=len(word)
    for i,c in enumerate(word):
        add_count(counter,c)

    results=[]
    for i,c in enumerate(string):
        if i>=lw:
            # add count for starting char
            add_count(counter,string[i-lw])

        # reduce count for current char
        reduce_count(counter,c)

        if not counter:
            results+=[i-lw+1]
    return results

assert bruteforce('abxaba', 'ab')==[0,3,4]
assert find_anagram_words_in_string('abxaba', 'ab')==[0,3,4]
