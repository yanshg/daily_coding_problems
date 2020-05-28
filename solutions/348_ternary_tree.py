#!/usr/bin/python

"""

This problem was asked by Zillow.

A ternary search tree is a trie-like data structure where each node may have up to three children. Here is an example which represents the words code, cob, be, ax, war, and we.

       c
    /  |  \
   b   o   w
 / |   |   |
a  e   d   a
|    / |   | \
x   b  e   r  e

The tree is structured according to the following rules:

    left child nodes link to words lexicographically earlier than the parent prefix
    right child nodes link to words lexicographically later than the parent prefix
    middle child nodes continue the current word

For instance, since code is the first word inserted in the tree, and cob lexicographically precedes cod, cob is represented as a left child extending from cod.

Implement insertion and search functions for a ternary search tree.

"""

class TenaryTree():
    def __init__(self,val=None,left=None,middle=None,right=None):
        self.ch=val
        self.l=left
        self.m=middle
        self.r=right

    def __repr__(self):
        if self.l or self.m or self.r:
            return "{}->({},{},{})".format(self.ch,self.l,self.m,self.r)
        return str(self.ch)

    @staticmethod
    def add_tree(node,word):
        if not word:
            return None

        if not node:
            node=TenaryTree()
        node.insert(word)
        return node

    def insert(self,word):
        if not word:
            return

        c,remaining=word[0],word[1:]
        if not self.ch:
            self.ch=c
            self.m=TenaryTree.add_tree(self.m,remaining)
        elif c==self.ch:
            self.m=TenaryTree.add_tree(self.m,remaining)
        elif c<self.ch:
            self.l=TenaryTree.add_tree(self.l,word)
        else:
            self.r=TenaryTree.add_tree(self.r,word)

    def search(self,word):
        if not word:
            return True

        c,remaining=word[0],word[1:]
        if not self.ch:
            return False
        elif c==self.ch:
            if not remaining:
                return True
            return self.m.search(remaining) if self.m else False
        elif c<self.ch:
            return self.l.search(word) if self.l else False
        elif c>self.ch:
            return self.r.search(word) if self.r else False

words=['code', 'cob', 'be', 'ax', 'war', 'we']

tt=TenaryTree()
for word in words:
    tt.insert(word)
print(tt)

assert tt.search('ax')
assert not tt.search('ay')
