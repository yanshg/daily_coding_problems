#!/usr/bin/python

"""

This problem was asked by Quora.

Word sense disambiguation is the problem of determining which sense a word takes on in a particular setting, if that word has multiple meanings. For example, in the sentence "I went to get money from the bank", bank probably means the place where people deposit money, not the land beside a river or lake.

Suppose you are given a list of meanings for several words, formatted like so:

{
    "word_1": ["meaning one", "meaning two", ...],
    ...
    "word_n": ["meaning one", "meaning two", ...]
}

Given a sentence, most of whose words are contained in the meaning list above, create an algorithm that determines the likely sense of each possibly ambiguous word.

"""

# Idea: Divide and Conquer
#
#       Return Array of Array

import re

def helper(words,word_meanings):
    if not words:
        return [[]]

    l=len(words)
    mid=l//2
    mid_word=words[mid]
    mid_words=word_meanings[mid_word] if mid_word and mid_word in word_meanings else [mid_word]

    if l==1:
        return [ [word] for word in mid_words ]

    results=[]

    for left_s in helper(words[:mid],word_meanings):
        for mid_s in mid_words:
            for right_s in helper(words[mid+1:],word_meanings):
                results+=[left_s + [mid_s] + right_s]

    return results

def get_ambiguous_sentences(s,word_meanings):
    words=re.split(r'(\W+)',s)
    return [ ''.join(new_words) for new_words in helper(words,word_meanings) ]

word_meanings={
    "word1": ["word1_meaning1", "word1_meaning2" ],
    "word2": ["word2_meaning1", "word2_meaning2", "word2_meaning3" ],
    "word3": ["word3_meaning1", "word3_meaning2", "word3_meaning3" ],
    "word4": ["word4_meaning1", "word4_meaning2", "word4_meaning3", "word4_meaning4" ],
}

s="word1 has word2 and word3 but no word4."
for s in get_ambiguous_sentences(s,word_meanings):
    print(s)
