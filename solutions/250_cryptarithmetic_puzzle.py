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

# Idea: Use backtracking
#
# 1. First initialize the words to get the data structure:
#
#    'chars':  ['D', 'E', 'Y', 'N', 'R', 'O', 'S', 'M'],
#    'cols':   [('D', 'E', 'Y'), ('N', 'R', 'E'), ('E', 'O', 'N'), ('S', 'M', 'O'), (' ', ' ', 'M')]}
#    'values': {'E': None, 'D': None, 'M': None, 'O': None, 'N': None, 'S': None, 'R': None, 'Y': None},
#
# 2. Choose one number and assign to first letter in 'chars' array,
# 4. Check if valid, if valid, continue same procedure for other letters.
# 5. if not valid, choose another number
#
# Notes:
#       1. Need support 4+ words
#       2. Prepare to use map(len,words) to get length information for all words and re-use it

SPACE_CHAR = ' '

# For each word, from right to left to add the char.
def init_crypt_data(words):
    crypt_data = dict()

    values = dict()
    chars = list()

    max_len = len(words[-1])
    reversed_words = [ list(reversed(word)) + list((max_len-len(word))*SPACE_CHAR) for word in words ]
    cols = zip(*reversed_words)
    for col in cols:
        for c in col:
            if c != SPACE_CHAR and c not in values:
                values[c] = None
                chars += [c]

    crypt_data['chars'] = chars
    crypt_data['values'] = values
    crypt_data['cols'] = cols
    return crypt_data

def is_valid(crypt_data):
    chars = crypt_data['chars']
    values = crypt_data['values']
    cols = crypt_data['cols']

    carry = 0
    for col in cols:
        value = carry
        l = len(col)
        for i,c in enumerate(col):
            if c == SPACE_CHAR:
                continue

            if values[c] is None:
                return True

            if i < l-1:
                value += values[c]

        if (value % 10) != values[col[-1]]:
            return False

        carry = value // 10

    for c in cols[-1]:
        if c != SPACE_CHAR and values[c] == 0:
            return False

    return True

def solve_puzzle(crypt_data,i,nums):
    chars=crypt_data['chars']
    if i==len(chars):
        return crypt_data['values']

    if not nums:
        return None

    c=chars[i]
    for num in nums:
        crypt_data['values'][c]=num
        if is_valid(crypt_data):
            solution = solve_puzzle(crypt_data,i+1,nums-{num})
            if solution is not None:
                return solution
        crypt_data['values'][c]=None

    return None

def solve_cryptarithmetic(words):
    crypt_data=init_crypt_data(words)
    nums=set(range(10))

    # Starting from the first character to solv
    return solve_puzzle(crypt_data,0,nums)

assert solve_cryptarithmetic(['SEND','MORE','MONEY'])=={'S':9,'E':5,'N':6,'D':7,'M':1,'O':0,'R':8,'Y':2}
assert solve_cryptarithmetic(['CP','IS','FUN','TRUE'])=={'P':2,'S':5,'N':7,'E':4,'C':3,'I':6,'U':8,'F':9,'R':0,'T':1}
