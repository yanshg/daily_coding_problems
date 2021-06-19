#!/usr/bin/python

"""

This problem was asked by Google.

You're given a string consisting solely of '(', ')', and '*'. * can represent either a (, ), or an empty string. Determine whether the parentheses are balanced.

For example, '(()*' and '(*)' are balanced. ')*(' is not balanced.

"""

# Idea:  put checked string in stack(), handle '*' case in remaining.
#        Handle only one character in each DP sub calling

def validate_parentheses_helper(string,stack=list()):
    if not string:
        return not stack

    ch,remain=string[0],string[1:]
    s=stack.copy();

    if ch=='*':
        return validate_parentheses_helper('('+remain,s) or \
               validate_parentheses_helper(')'+remain,s) or \
               validate_parentheses_helper(remain,s)

    if ch==')' and not s:
        return False
    elif ch==')' and s[-1]=='(':
        s.pop()
    else:
        s.append(ch)

    return validate_parentheses_helper(remain,s)

def validate_parentheses(string):
    return validate_parentheses_helper(string,[])


# Backtrack
def isvalid(s):
    bal=0
    for c in s:
        if c=='(': bal+=1
        if c==')': bal-=1
        if bal<0:  break
    return bal==0

def backtrack(s, index):
    if index==len(s):
        return isvalid(s)

    if s[index]=='*':
        for c in '() ':
            s1=s[:]
            s1[index]=c
            if backtrack(s1, index+1):
                return True
    elif backtrack(s, index+1):
         return True
    return False

def validate_parentheses_bt(s):
    return backtrack(list(s),0)

# DP[i][j]: mean s[i:j+1] is valid then True else False

def validate_parentheses_dp(s):
    pass

def checkValidString(s):
    lo = hi = 0
    for c in s:
        lo += 1 if c == '(' else -1
        hi += 1 if c != ')' else -1
        if hi < 0: break
        lo = max(lo, 0)
    return lo == 0

assert validate_parentheses("(()*")
assert validate_parentheses("(())")
assert validate_parentheses("((*)")
assert validate_parentheses("((**")
assert validate_parentheses("(*)")
assert not validate_parentheses(")*(")

assert validate_parentheses_bt("(()*")
assert validate_parentheses_bt("(())")
assert validate_parentheses_bt("((*)")
assert validate_parentheses_bt("((**")
assert validate_parentheses_bt("(*)")
assert not validate_parentheses_bt(")*(")

assert checkValidString("(()*")
assert checkValidString("(())")
assert checkValidString("((*)")
assert checkValidString("((**")
assert checkValidString("(*)")
assert not checkValidString(")*(")
