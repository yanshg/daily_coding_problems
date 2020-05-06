#!/usr/bin/python

"""
This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

"""

# bruteforce solution

def bruteforce(strs,prefix):
    return { s for s in strs if s.startswith(prefix) }

# use Trie data structure

class Trie:
    def __init__(self):
        self.trie=dict()

    def insert(self,string):
        if not string:
            return

        trie=self.trie
        for c in string:
            if c not in trie:
                trie[c]=dict()
            trie=trie[c]
        trie['#']=''

    def _elements(self,trie,path='',results=set()):
        if not trie and path:
            results.add(path)
            return results

        for c in trie:
            if c=='#':
                results.add(path)
            else:
                self._elements(trie[c],path+c,results)

        return results

    def find(self,prefix):
        trie=self.trie
        for c in prefix:
            if c not in trie:
                return None
            trie=trie[c]

        return { prefix+elem for elem in self._elements(trie) }

def autocomplete(strs,prefix):
    trie=Trie()
    for s in strs:
        trie.insert(s)
    return trie.find(prefix)

assert bruteforce({'dog','de','deer','deal'},'de')=={'de','deer','deal'}
assert autocomplete({'dog','de','deer','deal'},'de')=={'de', 'deer','deal'}
