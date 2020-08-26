#!/usr/bin/python

"""

This problem was asked by YouTube.

Write a program that computes the length of the longest common subsequence of three given strings. For example, given "epidemiologist", "refrigeration", and "supercalifragilisticexpialodocious", it should return 5, since the longest common subsequence is "eieio".

"""

# Recursion

def helper(strings,sequence,indices):
    #print("sequence:",sequence)

    lcs_len=len(sequence)
    chars=set((strings[0])[indices[0]+1:])

    for c in chars:
        # if c is in all the strings' substring ( (strings[i])[indices[i]+1:] )
        #     lcs_len=max(lcs_len, helper(strings,sequence+c,new_indices))
        # else:
        #     continue with next char
        new_indices=list()
        for i,string in enumerate(strings):
            index=string.find(c, indices[i]+1)
            if index==-1:
                break
            new_indices+=[index]

        if len(new_indices)==len(strings):
            lcs_len=max(lcs_len,helper(strings,sequence+c,new_indices))

    return lcs_len

def get_lcs_len(strings):
    return helper(strings,'',[-1]*len(strings))


# DP table

# DP[i][j][k]: means the LCS for X[:i+1], Y[:j+1], Z[:k+1]
#

def get_lcs_len_dp(strings):
    s1,s2,s3 = strings
    l,m,n = len(s1),len(s2),len(s3)

    DP = [[[0 for i in range(n+1)] for j in range(m+1)]
          for k in range(l+1)]

    for i in range(l+1):
        for j in range(m+1):
            for k in range(n+1):
                if s1[i-1]==s2[j-1]==s3[k-1]:
                    DP[i][j][k] = DP[i-1][j-1][k-1] + 1
                else:
                    DP[i][j][k] = max(DP[i-1][j][k], DP[i][j-1][k], DP[i][j][k-1])

    return DP[l][m][n]

assert get_lcs_len(["epidemiologist", "refrigeration", "supercalifragilisticexpialodocious"])==5
assert get_lcs_len_dp(["epidemiologist", "refrigeration", "supercalifragilisticexpialodocious"])==5
assert get_lcs_len_dp(['AGGT12','12TXAYB','12XBA']) == 2
