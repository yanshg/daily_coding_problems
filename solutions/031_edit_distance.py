#!/usr/bin/python

"""
This problem was asked by Google.

The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. For example, the edit distance between "kitten" and "sitting" is three: substitute the "k" for "s", substitute the "e" for "i", and append a "g".

Given two strings, compute the edit distance between them.
"""

def edit_distance(s, t, debt=0):
    if (not s or not t):
        return len(s)+len(t)+debt

    # insert first character of s to the beginning of t
    i=edit_distance(s[1:], t, debt+1)

    # delete the first character of t
    d=edit_distance(s, t[1:], debt+1)

    # replace the first charcter of t with first character of s
    e=edit_distance(s[1:], t[1:], debt+(s[0] != t[0]))

    return min(i,d,e)

# https://github.com/labuladong/fucking-algorithm/blob/master/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E7%B3%BB%E5%88%97/%E7%BC%96%E8%BE%91%E8%B7%9D%E7%A6%BB.md

def edit_distance_dp(word1, word2):
    m, n= len(word1), len(word2)
    dp = [[0 for i in range(0,n+1)] for j in range(0,m+1)]
    for i in range(1,m+1):
        dp[i][0] = i
    for j in range(1,n+1):
        dp[0][j] = j
    for i in range(1,m+1):
        for j in range(1,n+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(
                    dp[i-1][j]+1,
                    dp[i][j-1]+1,
                    dp[i-1][j-1]+1
                )

    return dp[m][n]

assert edit_distance('kitten', 'sitting')==3
assert edit_distance('black', 'white')==5
assert edit_distance_dp('kitten', 'sitting')==3
assert edit_distance_dp('black', 'white')==5
