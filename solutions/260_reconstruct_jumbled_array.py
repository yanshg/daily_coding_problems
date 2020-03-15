#!/usr/bin/python

"""

This problem was asked by Pinterest.

The sequence [0, 1, ..., N] has been jumbled, and the only clue you have for its order is an array representing whether each number is larger or smaller than the last. Given this information, reconstruct an array that is consistent with it. For example, given [None, +, +, -, +], you could return [1, 2, 3, 0, 4]

"""

# Backtracking

def is_valid_array(clue_arr,result_arr):
    first=result_arr[0]
    for i in range(1,len(result_arr)):
        if (clue_arr[i]=='+' and result_arr[i]<first) or \
                (clue_arr[i]=='-' and result_arr[i]>first):
            return False
    return True

def helper(clue_arr,result_arr,nums):
    if len(result_arr)==len(clue_arr):
        return result_arr

    for num in nums:
        result_arr.append(num)
        if is_valid_array(clue_arr,result_arr):
            print("Tried: ", result_arr)
            result=helper(clue_arr,result_arr,nums-{num})
            if result:
                return result
        result_arr.pop()

    return None

def reconstruct_array(n,clue_arr):
    nums=set(range(n+1))
    result_arr=[]
    return helper(clue_arr,result_arr,nums) 

assert reconstruct_array(4, [None, '+', '+', '-', '+'])==[1, 2, 3, 0, 4]
