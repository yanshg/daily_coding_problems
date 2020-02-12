#!/usr/bin/python

"""

This problem was asked by Salesforce.

Given an array of integers, find the maximum XOR of any two elements.

"""

# Idea: use Trie data structure

# Notes: use (int).bit_length() to get bits length of the integer

class Trie:
    def __init__(self,bit_length):
        self._trie=dict()
        self.bit_length=bit_length

    def __repr__(self):
        return str(self._trie)

    def insert(self,n):
        size=self.bit_length
        trie=self._trie

        for i in range(size-1,-1,-1):
            bit=int(bool(n & (1<<i)))
            if bit not in trie:
                trie[bit]=dict()
            trie=trie[bit]

    def get_max_xor(self,n):
        size=self.bit_length
        trie=self._trie

        xor=0
        for i in range(size-1,-1,-1):
            bit=int(bool(n & (1<<i)))
            if (1-bit) in trie:
                trie=trie[1-bit]
                xor |= 1<<i
            else:
                trie=trie[bit]

        return xor


def bruteforce(nums):
    return max([ n1^n2 for n1 in nums for n2 in nums])

def get_max_xor(nums):
    bit_length=max(nums).bit_length()
    trie=Trie(bit_length)
    for n in nums:
        trie.insert(n)

    return max([trie.get_max_xor(n) for n in nums ])

assert bruteforce([5,9,8,23,42])==61
assert get_max_xor([5,9,8,23,42])==61
