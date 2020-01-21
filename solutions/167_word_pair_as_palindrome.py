#!/usr/bin/python

"""
Given a list of words, find all pairs of unique indices such that the concatenation of the two words is a palindrome.

For example, given the list ["code", "edoc", "da", "d"], return [(0, 1), (1, 0), (2, 3)].
"""

def is_palindrome(word):
    return word==word[::-1]

def bruteforce(words):
    return [ (i,j) for i,word1 in enumerate(words) for j,word2 in enumerate(words) if i!=j and is_palindrome(word1+word2) ]

def find_word_pairs_palindrome(words):
    d=dict()
    for i,word in enumerate(words):
        d[word]=i

    results=[]

    for i,word in enumerate(words):
        for char_i in range(len(word)):
            prefix,suffix=word[:char_i],word[char_i:]
            reversed_prefix,reversed_suffix=prefix[::-1],suffix[::-1]

            if (suffix==reversed_suffix and reversed_prefix in d):
                if i!=d[reversed_prefix]:
                    results.append((i,d[reversed_prefix]))
            if (prefix==reversed_prefix and reversed_suffix in d):
                if i!=d[reversed_suffix]:
                    results.append((i,d[reversed_suffix]))

    return results

assert bruteforce(["code", "edoc", "da", "d"])== [(0, 1), (1, 0), (2, 3)]
assert find_word_pairs_palindrome(["code", "edoc", "da", "d"])== [(0, 1), (1, 0), (2, 3)]
