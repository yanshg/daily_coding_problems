#!/usr/bin/python

"""

This problem was asked by Square.

In front of you is a row of N coins, with values v1, v2, ..., vn.

You are asked to play the following game. You and an opponent take turns choosing either the first or last coin from the row, removing it from the row, and receiving the value of the coin.

Write a program that returns the maximum amount of money you can win with certainty, if you move first, assuming your opponent plays optimally.

"""
# Idea 1:
#        F(i, j)  represents the maximum value the user can collect from 
#                 i'th coin to j'th coin.
#
#        F(i, j)  = Max(Vi + min(F(i+2, j), F(i+1, j-1) ), 
#                       Vj + min(F(i+1, j-1), F(i, j-2) )) 
#
#        Base Cases:
#                     F(i, j)  = Vi           If j == i
#                     F(i, j)  = max(Vi, Vj)  If j == i+1


def helper1(nums,i,j,path=[],sum=0):
    if i==j:
        selection=nums[i]
        sum+=selection
        path+=[selection]
        return sum,path
    elif j==i+1:
        selection=max(nums[i],nums[j])
        sum+=selection
        path+=[selection]
        return sum,path
    else:
        selection=nums[i]
        sum1,path1=helper1(nums,i+2,j,path+[selection],sum+selection)
        sum2,path2=helper1(nums,i+1,j-1,path+[selection],sum+selection)
        selection=nums[j]
        sum3,path3=helper1(nums,i+1,j-1,path+[selection],sum+selection)
        sum4,path4=helper1(nums,i,j-2,path+[selection],sum+selection)
        sum1,path1=(sum1,path1) if sum1<sum2 else (sum2,path2)
        sum3,path3=(sum3,path3) if sum3<sum4 else (sum4,path4)
        return (sum1,path1) if sum1>sum3 else (sum3,path3)


def max_amount_coins_row1(nums):
    sum,path=helper1(nums, 0, len(nums)-1, [], 0)
    print("path: ",path, "sum: ", sum)
    return sum


# Idea 2:

#    F(i, j)  represents the maximum value the user can collect from 
#             i'th coin to j'th coin.
#
#    F(i, j)  = Max(Sum - F(i+1, j, Sum-Vi), 
#                   Sum - F(i, j-1, Sum-Vj)) 
#
#    Base Case:
#         F(i, j)  = max(Vi, Vj)  If j == i+1
#
# For both of your choices, the opponent gives you total Sum minus maximum of his value

def helper2(nums,i,j,s):
    if j==i+1:
        return max(nums[i], nums[j])

    return max(s-helper2(nums,i+1,j,s-nums[i]),
               s-helper2(nums,i,j-1,s-nums[j]))

def max_amount_coins_row2(nums):
    return helper2(nums, 0, len(nums)-1, sum(nums))

assert max_amount_coins_row1([ 20, 30, 2, 2, 2, 10 ])==42
assert max_amount_coins_row2([ 20, 30, 2, 2, 2, 10 ])==42
