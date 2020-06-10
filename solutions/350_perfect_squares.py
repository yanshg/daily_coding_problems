#!/usr/bin/python

"""

This problem was asked by Uber.

Write a program that determines the smallest number of perfect squares that sum up to N.

Here are a few examples:
 - Given N = 4, return 1 (4)
 - Given N = 17, return 2 (16 + 1)
 - Given N = 18, return 2 (9 + 9)

"""

# Article: https://www.geeksforgeeks.org/minimum-number-of-squares-whose-sum-equals-to-given-number-n/

def get_min_squares(n):
    if n<=3:
        return n

    # 1+1+1+...+1
    result=n

    for i in range(1,n+1):
        temp=i*i
        if temp>n:
            break
        result=min(result, 1+get_min_squares(n-temp))

    return result

# bottom to up
from math import ceil,sqrt
def get_min_squares_dp(n):
    dp=[0,1,2,3]

    for i in range(4,n+1):
        dp.append(i)
        k=int(ceil(sqrt(i)))+1
        for j in range(1,k):
            temp=j*j
            if temp>i:
                break
            dp[i]=min(dp[i],1+dp[i-temp])

    return dp[n]


assert get_min_squares(4)==1
assert get_min_squares(17)==2
assert get_min_squares(18)==2
assert get_min_squares_dp(4)==1
assert get_min_squares_dp(17)==2
assert get_min_squares_dp(18)==2
