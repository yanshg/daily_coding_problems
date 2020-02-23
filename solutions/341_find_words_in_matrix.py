#!/usr/bin/python

"""

This problem was asked by Google.

You are given an N by N matrix of random letters and a dictionary of words. Find the maximum number of words that can be packed on the board from the given dictionary.

A word is considered to be able to be packed on the board if:

    It can be found in the dictionary
    It can be constructed from untaken letters by other words found so far on the board
    The letters are adjacent to each other (vertically and horizontally, not diagonally).

Each tile can be visited only once by any word.

For example, given the following dictionary:

{ 'eat', 'rain', 'in', 'rat' }

and matrix:

[['e', 'a', 'n'],
 ['t', 't', 'i'],
 ['a', 'r', 'a']]

Your function should return 3, since we can make the words 'eat', 'in', and 'rat' without them touching each other. We could have alternatively made 'eat' and 'rain', but that would be incorrect since that's only 2 words.

"""

# use DFS with Trie

# O(N^3)
class Trie:
    def __init__(self):
        self._trie=dict()

    def insert(self,word):
        trie=self._trie
        for c in word:
            if c not in trie:
                trie[c]=dict()
            trie=trie[c]
        trie['#']=''

class Boggle:
    def __init__(self,grid,dictionay):
        self.grid=grid
        self.dictionay=dictionary
        self.trie=Trie()
        for word in dictionay:
            self.trie.insert(word)

    # DFS
    def _find_all_words(self,grid,trie,rows,cols,i,j,current_word='',all_words=set(),visited=set()):
        if i<0 or i>=rows or j<0 or j>=cols:
            return

        coord="{}-{}".format(i,j)
        if coord in visited:
            return

        c=grid[i][j]
        if c not in trie:
            return

        visited.add(coord)

        current_word+=c
        trie=trie[c]
        if '#' in trie:
           # find a new word
           all_words.add(current_word)
        
        moves=[(0,1),(0,-1),(-1,0),(1,0)]
        for (dx,dy) in moves:
            self._find_all_words(grid,trie,rows,cols,i+dx,j+dy,current_word,all_words,visited)

    def find_all_words(self):
        all_words=set()
        visited=set()
        grid=self.grid
        trie=self.trie._trie
        rows,cols=len(grid),len(grid[0])
        for i in range(rows):
            for j in range(cols):
                self._find_all_words(grid,trie,rows,cols,i,j,'',all_words,visited)

        return all_words

grid = [['e', 'a', 'n'],
        ['t', 't', 'i'],
        ['a', 'r', 'a']]

dictionary = { 'eat', 'rain', 'in', 'rat' }

b = Boggle(grid, dictionary)
words = b.find_all_words()

for w in words:
  print(w)

