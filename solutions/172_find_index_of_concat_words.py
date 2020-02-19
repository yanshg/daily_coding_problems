#!/usr/bin/python

"""
This problem was asked by Dropbox.

Given a string s and a list of words words, where each word is the same length, find all starting indices of substrings in s that is a concatenation of every word in words exactly once.

For example, given s = "dogcatcatcodecatdog" and words = ["cat", "dog"], return [0, 13], since "dogcat" starts at index 0 and "catdog" starts at index 13.

Given s = "barfoobazbitbyte" and words = ["dog", "cat"], return [] since there are no substrings composed of "dog" and "cat" in s.

The order of the indices does not matter.
"""

from collections import Counter

def find_index_of_concat_words(string, words):
    n=len(string)

    num_words=len(words)
    len_word=len(words[0])
    len_all_words=num_words*len_word

    counter=Counter(words)

    if n<len_all_words:
        return []

    result=[]
    for i in range(n-len_all_words+1):
        tmp_counter=counter.copy()
        all_exists=True
        for j in range(num_words):
            start=i+j*len_word
            word=string[start:start+len_word]
            if word not in tmp_counter:
                all_exists=False
                break
            else:
                tmp_counter[word]-=1
                if tmp_counter[word]==0:
                    del tmp_counter[word]
        if all_exists and not tmp_counter:
            result.append(i)

    return result

assert find_index_of_concat_words("dogcatcatcodecatdog", ["cat", "dog"])==[0, 13]
assert find_index_of_concat_words("barfoobazbitbyte", ["dog", "cat"])==[]
