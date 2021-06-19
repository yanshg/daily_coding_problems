#!/usr/bin/python

"""

This problem was asked by Facebook.

Describe an algorithm to compute the longest increasing subsequence of an array of numbers in O(n log n) time.

"""

# Article:  https://en.wikipedia.org/wiki/Longest_increasing_subsequence
#           https://stackoverflow.com/questions/2631726/how-to-determine-the-longest-increasing-subsequence-using-dynamic-programming
#           https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/
#           https://www.geeksforgeeks.org/longest-increasing-subsequence-using-longest-common-subsequence-algorithm/

# O(2^n)
def helper(nums,i,path):
    if i>=len(nums):
        return path

    exclude = helper(nums,i+1,path)

    last = float('-inf') if not path else path[-1]
    if nums[i] > last:
        include = helper(nums,i+1,path+[nums[i]])
        return max([include,exclude], key=len)

    return exclude

def lis_recursion(nums):
    return helper(nums,0,[])


# O(n^2) use LCS(Longest Common Subsequence)
def lis_with_lcs(nums):
    n = len(nums)

    DP = [[[] for i in range(n + 1)]
              for i in range(n + 1)]

    sortednums = sorted(nums)

    # Get Longest Common Subsequence of nums and sortednums
    for i in range(1,n + 1):
        for j in range(1,n + 1):
            if (nums[i - 1] == sortednums[j - 1]):
                DP[i][j] = DP[i - 1][j - 1] + [nums[i-1]]
            else:
                DP[i][j] = max([DP[i - 1][j], DP[i][j-1]], key=len)

    return DP[-1][-1]

# Another DP solution
def lis_dp(nums):
    n = len(nums)
    DP = [ [] for i in range(n) ]
    max_len,max_index = 0,0
     for i in range(n):
        DP[i] = [ nums[i] ]
        for j in range(i):
            if nums[i] > nums[j] and len(DP[i])<=len(DP[j]):
                DP[i] = DP[j] + [ nums[i] ]
        if len(DP[i])>max_len:
            max_len = len(DP[i])
            max_index = i
    return DP[max_index]

# O(n log n) to only get the length
#
import bisect
def lis_bisect(nums):
    tops = []
    for num in nums:
        index = bisect.bisect_right(tops, num)
        if index == len(tops):
            tops += [num]
        else:
            tops[index] = num
    return tops

assert lis_recursion([23,2,12,15,5,10,34])==[2,12,15,34]
assert lis_dp([23,2,12,15,5,10,34])==[2,12,15,34]
assert lis_with_lcs([23,2,12,15,5,10,34])==[2,12,15,34]
assert lis_with_lcs([2, 5, 3, 7, 11, 8, 10, 13, 6])==[2, 5, 7, 8, 10, 13]
assert lis_bisect([23,2,12,15,5,10,34])==[2,5,10,34]
assert lis_bisect([2, 5, 3, 7, 11, 8, 10, 13, 6])==[2, 3, 6, 8, 10, 13]

