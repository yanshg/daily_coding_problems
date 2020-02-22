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
def helper(nums,n,i,path):
    if i>=n:
        return path

    last=float('-inf') if not path else path[-1]
    num=nums[i]
    if num<last:
        return helper(nums,n,i+1,path)

    return max([helper(nums,n,i+1,path),
                helper(nums,n,i+1,path+[num])], key=len)

def get_lis_dp(nums):
    return helper(nums,len(nums),0,[])


# O(n^2) use LCS(Longest Common Subsequence)
def lis_with_lcs(nums): 
    n = len(nums) 
  
    # Create an 2D array of integer 
    # for tabulation 
    L = [[0 for i in range(n + 1)]  
            for i in range(n + 1)] 
      
    # Take the second sequence as the sorted 
    # sequence of the given sequence 
    sortednums = sorted(nums) 
  
    # Classical Dynamic Programming algorithm 
    # for Longest Common Subsequence 
    for i in range(n + 1): 
        for j in range(n + 1): 
            if (i == 0 or j == 0): 
                L[i][j] = 0
  
            elif (nums[i - 1] == sortednums[j - 1]): 
                L[i][j] = L[i - 1][j - 1] + 1
  
            else: 
                L[i][j] = max(L[i - 1][j],  
                              L[i][j - 1]) 
  
    # Return the result 
    return L[n][n] 
  
# O(n log n) to only get the length 
#
# 1. If A[i] is smallest among all end 
#    candidates of active lists, we will start 
#    new active list of length 1.
#
# 2. If A[i] is largest among all end candidates of 
#   active lists, we will clone the largest active 
#   list, and extend it by A[i].
#
# 3. If A[i] is in between, we will find a list with 
#   largest end element that is smaller than A[i]. 
#   Clone and extend this list by A[i]. We will discard all
#   other lists of same length as that of this modified list.

def binary_search(s,x):
    low=0
    high=len(s)-1
    flag=1
    while low<=high:
          mid=(high+low)//2
          if s[mid]==x:
              flag=0
              break
          elif s[mid]<x:
              low=mid+1
          else:
              high=mid-1
    if flag:
       s[low]=x
    return s

def lis_length(nums):
     if not nums:
        return 0

     s=[nums[0]]
     for i in range(1,len(nums)):
         if s[-1]<nums[i]:
             s+=[nums[i]]
         else:
             s=binary_search(s,nums[i])
     return len(s)

# O(n log n) to get the sequence
# Article:  https://www.geeksforgeeks.org/construction-of-longest-monotonically-increasing-subsequence-n-log-n/

def get_ceil_index(arr, tail_indices, l, r, key): 
  
    while (r - l > 1): 
      
        m = l + (r - l)//2
        if (arr[tail_indices[m]] >= key): 
            r = m 
        else: 
            l = m 
  
    return r 
   
def get_longest_increasing_subsequence(arr, n): 
  
    # Add boundary case, 
    # when array n is zero 
    # Depend on smart pointers 
      
    # Initialized with 0 
    tail_indices =[0 for i in range(n + 1)]   
  
    # Initialized with -1 
    prev_indices =[-1 for i in range(n + 1)]   
      
    len = 1 
    for i in range(1, n): 
      
        if (arr[i] < arr[tail_indices[0]]): 
          
            # new smallest value 
            tail_indices[0] = i 
          
        elif (arr[i] > arr[tail_indices[len-1]]): 
          
            # arr[i] wants to extend largest subsequence
            prev_indices[i] = tail_indices[len-1] 
            tail_indices[len] = i 
            len += 1
          
        else: 
          
            # arr[i] wants to be a 
            # potential condidate of 
            # future subsequence 
            # It will replace ceil 
            # value in tail_indices 
            pos = get_ceil_index(arr, tail_indices, -1, len-1, arr[i])
            prev_indices[i] = tail_indices[pos-1] 
            tail_indices[pos] = i 
          
    print("LIS of given input") 
    i = tail_indices[len-1] 
    while(i >= 0): 
        print(arr[i], " ", end ="") 
        i = prev_indices[i] 
    print() 
   
    return len

assert get_lis_dp([23,2,12,15,5,10,34])==[2,5,10,34]
assert lis_length([ 2, 5, 3, 7, 11, 8, 10, 13, 6 ] )==6
assert lis_with_lcs([ 2, 5, 3, 7, 11, 8, 10, 13, 6 ] )==6

