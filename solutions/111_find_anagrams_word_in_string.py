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
    results=[]
    counter=defaultdict(int)

    ls,lw=len(string),len(word)
    for i in range(lw):
        add_count(counter,word[i])
    for i in range(lw):
        reduce_count(counter,string[i])
    if not counter:
        results.append(0)

    for i in range(lw,ls):
        add_count(counter,string[i-lw])
        reduce_count(counter,string[i])
        if not counter:
            results.append(i-lw+1)

    return results

assert bruteforce('abxaba', 'ab')==[0,3,4]
assert find_anagram_words_in_string('abxaba', 'ab')==[0,3,4]
