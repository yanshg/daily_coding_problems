#!/usr/bin/python

"""

This problem was asked by Google.

You are given a set of synonyms, such as (big, large) and (eat, consume). Using this set, determine if two sentences with the same number of words are equivalent.

For example, the following two sentences are equivalent:

    "He wants to eat food."
    "He wants to consume food."

Note that the synonyms (a, b) and (a, c) do not necessarily imply (b, c): consider the case of (coach, bus) and (coach, teacher).

Follow-up: what if we can assume that (a, b) and (a, c) do in fact imply (b, c)?

"""

import re
from collections import defaultdict

def helper_recursion(words1,words2,synonyms_dict):
    if not words1 and not words2:
        return True
    if not words1 or not words2:
        return False

    w1,w2=words1[0],words2[0]
    if w1==w2 or w1 in synonyms_dict[w2]:
        return helper(words1[1:],words2[1:],synonyms_dict)
    return False

def helper(words1,words2,synonyms_dict):
    for w1,w2 in zip(words1,words2):
        if w1!=w2 and w1 not in synonyms_dict[w2]:
            return False
    return True

def equivalent_sentences(s1,s2,synonyms):
    words1=re.split(",|\.| |\t|",s1)
    words2=re.split(",|\.| |\t|",s2)

    if len(words1)!=len(words2):
        return False

    synonyms_dict=defaultdict(list)
    for w1,w2 in synonyms:
        synonyms_dict[w1]+=[w2]
        synonyms_dict[w2]+=[w1]

    return helper(words1,words2,synonyms_dict)

assert equivalent_sentences("He wants to eat food.","He wants to consume food.",[('big', 'large'),('eat', 'consume')])
