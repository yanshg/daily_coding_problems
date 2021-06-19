#!/usr/bin/python

"""

Find an efficient algorithm to find the smallest distance (measured in number of words) between any two given words in a string.

For example, given words "hello", and "world" and a text content of "dog cat hello cat dog dog hello cat world", return 1 because there's only one word "cat" in between the two words.

"""

def get_smallest_distance(word1,word2,sentence):
    if word1==word2:
        return 0

    words=sentence.split()
    min_dist=len(words)+1
    prev = -1
    for i,word in enumerate(words):
        if word in [word1,word2]:
            if prev != -1 and word != words[prev]:
                min_distance=min(min_dist, i-prev-1)
            prev = i
    return min_distance

assert get_smallest_distance('hello','world', "dog cat hello cat dog dog hello cat world")==1
