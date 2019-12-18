#!/usr/bin/python

"""
This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

"""

from collections import defaultdict

def bruteforce(string,k):
    n=len(string)
    results=list()
    for i in range(n):
        for j in range(n,i+k-1,-1):
            s=string[i:j]
            # use set(string) to get how manu distinct chars
            if len(set(s))<=k:
                results.append(s)

    # To return the substring with max length
    return max(results,key=len)

def bruteforce_oneline(string,k):
    n=len(string)
    return max([ string[i:j] for i in range(n) for j in range(n,i+k-1,-1) if len(set(string[i:j]))<=k ], key=len)

def longest_substring_with_k_distinct(string, k):
    start=0
    frequency=defaultdict(int)
    candidate_substr=None

    for end,ch in enumerate(string):
        # Use the hashmap with frequency of the characters to determine how many distinct chars
        # For each char, get the sub string with start and end index
        frequency[ch]+=1

        while len(frequency)>k:
            start_ch=string[start]
            start+=1
            frequency[start_ch]-=1
            if frequency[start_ch]==0:
                del frequency[start_ch]

        if not candidate_substr or end-start+1>len(candidate_substr):
            candidate_substr=string[start:end+1]
            #print("candidate substring:", candidate_substr)

    return candidate_substr


assert bruteforce('abcba',2)=="bcb"
assert bruteforce_oneline('abcba',2)=="bcb"
assert longest_substring_with_k_distinct('abcba',2)=="bcb"
assert longest_substring_with_k_distinct('araaci',2)=="araa"

