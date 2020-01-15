#!/usr/bin/python

"""
This problem was asked by Square.

Given a list of words, return the shortest unique prefix of each word. For example, given the list:

    dog
    cat
    apple
    apricot
    fish

Return the list:

    d
    c
    app
    apr
    f

"""

# use Trie

# 1. Construct a Trie of all words.
# 2. Maintain frequency of every node (Here frequency is number of times node is visited during insertion).
# 3. For every word, we find the character nearest to the root with frequency as 1. The prefix of the word is path from root to this character.

class Trie():
    def __init__(self):
        self._trie=dict()
        self._trie['freq']=0

    def __repr__(self):
        return str(self._trie)

    def insert(self,word):
        if not word:
            return

        trie=self._trie
        for c in word:
            if c not in trie:
                trie[c]=dict()
                trie[c]['freq']=0
            trie=trie[c]
            trie['freq']+=1

    def get_unique_prefix_helper(self,trie,path=[],prefixes=set()):
        if not trie or trie['freq']==1:
            if path:
                p=''.join(path)
                print("path: ",p)
                prefixes.add(p)
            return prefixes

        for c in trie:
            if c != 'freq':
                self.get_unique_prefix_helper(trie[c],path+[c],prefixes)

        return prefixes

    def get_unique_prefix(self):
        return self.get_unique_prefix_helper(self._trie,[],set())

def get_unique_prefix(words):
    trie=Trie()
    for w in words:
        trie.insert(w)
    #print(trie)
    return trie.get_unique_prefix()

assert get_unique_prefix({'dog','cat','apple','apricot','fish'})=={'d','c','app','apr','f'}
