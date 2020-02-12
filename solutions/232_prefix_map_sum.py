#!/usr/bin/python

"""

This problem was asked by Google.

Implement a PrefixMapSum class with the following methods:

    insert(key: str, value: int): Set a given key's value in the map. If the key already exists, overwrite the value.

    sum(prefix: str): Return the sum of all values of keys that begin with a given prefix.

For example, you should be able to run the following code:

    mapsum.insert("columnar", 3)
    assert mapsum.sum("col") == 3

    mapsum.insert("column", 2)
    assert mapsum.sum("col") == 5

"""

# Idea:  use Trie data structure.

class PrefixMapSum:
    def __init__(self):
        self._trie=dict()
        self._trie['total']=0

    def __repr__(self):
        return str(self._trie)

    def insert(self,key,value):
        trie=self._trie
        for c in str(key):
            if c not in trie:
                trie[c]=dict()
                trie[c]['total']=0
            trie=trie[c]
            trie['total']+=value
        trie['value']=value

    def sum(self,prefix):
        trie=self._trie
        for c in prefix:
            if c not in trie:
                return None
            trie=trie[c]

        return trie['total']

mapsum=PrefixMapSum()
mapsum.insert("columnar", 3)
assert mapsum.sum("col") == 3

mapsum.insert("column", 2)
assert mapsum.sum("col") == 5
