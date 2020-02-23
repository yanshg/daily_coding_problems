#!/usr/bin/python

"""

This problem was asked by Facebook.

Boggle is a game played on a 4 x 4 grid of letters. The goal is to find as many words as possible that can be formed by a sequence of adjacent letters in the grid, using each cell at most once. Given a game board and a dictionary of valid words, implement a Boggle solver.

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
           if len(trie)==1:
               return
        
        moves=[(0,1),(0,-1),(-1,-1),(-1,0),(-1,1),(1,-1),(1,0),(1,1)]
        for (dx,dy) in moves:
            self._find_all_words(grid,trie,rows,cols,i+dx,j+dy,current_word,all_words,visited.copy())

    def find_all_words(self):
        all_words=set()
        grid=self.grid
        trie=self.trie._trie
        rows,cols=len(grid),len(grid[0])
        for i in range(rows):
            for j in range(cols):
                self._find_all_words(grid,trie,rows,cols,i,j,'',all_words,set())

        return all_words

grid = [['c', 'a', 't'],
        ['r', 'r', 'e'],
        ['t', 'o', 'n']]

dictionary = set(["cat", "cater", "cartoon", "art", "toon", "moon", "eat", "ton"])

b = Boggle(grid, dictionary)
words = b.find_all_words()

for w in words:
  print(w)

# Results: cater cat art eat ton
