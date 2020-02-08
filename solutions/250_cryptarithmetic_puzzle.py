#!/usr/bin/python

"""

This problem was asked by Google.

A cryptarithmetic puzzle is a mathematical game where the digits of some numbers are represented by letters. Each letter represents a unique digit.

For example, a puzzle of the form:

   SEND
 + MORE
--------
  MONEY

may have the solution:

   {'S': 9, 'E': 5, 'N': 6, 'D': 7, 'M': 1, 'O': 0, 'R': 8, 'Y': 2}

Given a three-word puzzle like the one above, create an algorithm that finds a solution.

"""

# Idea: use backtracking
#
#       1. First initialize ordered dictionary for letters,
#       2. Then get unassigned letters, and numbers for assign
#       3. Choose one number and assign to one unassigned letter, 
#       4. Check if valid, if valid, continue same procedure for other letters.
#       5. if not valid, choose another number
#
# Notes:
#       1. Need support 4+ words
#       2. Prepare to use map(len,words) to get length information for all words and re-use it

from collections import OrderedDict

# For each word, from right to left to add the char into OrderedDict.
def initialize_letters(words,lens):
    n=max(lens)

    letters=OrderedDict()
    for i in range(1,n+1):
        for j,word in enumerate(words):
            if i<=lens[j]:
               c=word[-i]
               if c not in letters:
                   letters[c]=None

    return letters

def is_valid(words,lens,letters):
    n=max(lens)

    # First character should not be zero
    if any([ letters[word[0]]==0 for word in words ]):
        return False

    carry=0
    for i in range(1,n+1):
        digits=[ letters[word[-i]] for j,word in enumerate(words) if i<=lens[j] ]
        if any([ digit==None for digit in digits ]):
            return True

        t=sum(digits[:-1])+carry
        if t>=10:
            carry=1
            t-=10
        else:
            carry=0

        if t!=digits[-1]:
            return False

    return True

def solve_puzzle(words,lens,letters,unassigned,nums):
    if not unassigned:
        print("letters: ", dict(letters))
        return dict(letters)

    c=unassigned[0]
    for num in nums:
        letters[c]=num
        if is_valid(words,lens,letters):
            solution=solve_puzzle(words,lens,letters,unassigned[1:],nums-{num})
            if solution:
                return solution
        letters[c]=None

    return None

def solve_cryptarithmetic_puzzle(words):
    lens=list(map(len,words))
    letters=initialize_letters(words,lens)
    unassigned=list(letters.keys())
    nums=set(range(10))
    #print("words:",words, "letters:",letters, "unassigned:", unassigned)

    return solve_puzzle(words,lens,letters,unassigned,nums)

assert is_valid(['SEND','MORE','MONEY'],[4,4,5],{'S':9,'E':5,'N':6,'D':7,'M':1,'O':0,'R':8,'Y':2})
assert solve_cryptarithmetic_puzzle(['SEND','MORE','MONEY'])=={'S':9,'E':5,'N':6,'D':7,'M':1,'O':0,'R':8,'Y':2}
assert solve_cryptarithmetic_puzzle(['CP','IS','FUN','TRUE'])=={'P':2,'S':5,'N':7,'E':4,'C':3,'I':6,'U':8,'F':9,'R':0,'T':1}

