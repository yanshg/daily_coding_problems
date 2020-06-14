#!/usr/bin/python

"""

This problem was asked by YouTube.

Write a program that computes the length of the longest common subsequence of three given strings. For example, given "epidemiologist", "refrigeration", and "supercalifragilisticexpialodocious", it should return 5, since the longest common subsequence is "eieio".

"""

CHARS="abcdefghijklmnopqrstuvwxyz"

def helper(strings,sequence,indices):
    #print("sequence:",sequence)
    lcs=len(sequence)
    for c in CHARS:
        # if c is in all the strings' substring ( (strings[i])[indices[i]+1:] )
        #     lcs=min(lcs, helper(strings,sequence+c,new_indices))
        # else:
        #     continue with next char
        new_indices=list()
        for i,string in enumerate(strings):
            index=string.find(c, indices[i]+1)
            if index==-1:
                break
            new_indices+=[index]

        if len(new_indices)==len(strings):
            lcs=max(lcs,helper(strings,sequence+c,new_indices))

    return lcs

def get_lcs(strings):
    return helper(strings,'',[-1]*len(strings))

assert get_lcs(["epidemiologist", "refrigeration", "supercalifragilisticexpialodocious"])==5
