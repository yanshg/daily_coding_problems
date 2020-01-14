#!/usr/bin/python

"""

Find an efficient algorithm to find the smallest distance (measured in number of words) between any two given words in a string.

For example, given words "hello", and "world" and a text content of "dog cat hello cat dog dog hello cat world", return 1 because there's only one word "cat" in between the two words.

"""

def get_smallest_distance(word1,word2,sentence):
    if word1==word2:
        return 0

    words=sentence.split()
    distance=len(words)+1
    positions=dict()

    for i,word in enumerate(words):
        if word in [word1,word2]:
            positions[word]=i

        if word1 in positions and word2 in positions:
            distance=min(distance,abs(positions[word1]-positions[word2])-1)
        
    return distance

assert get_smallest_distance('hello','world', "dog cat hello cat dog dog hello cat world")==1
