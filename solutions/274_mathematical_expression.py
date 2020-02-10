#!/usr/bin/python

"""

This problem was asked by Facebook.

Given a string consisting of parentheses, single digits, and positive and negative signs, convert the string into a mathematical expression to obtain the answer.

Don't use eval or a similar built-in parser.

For example, given '-1 + (2 + 3)', you should return 4.

"""

# Idea:     Use 2 stacks: values and oprators
#           Need check numbers, operators('+'/'-'/'*'/'/'), signs('+'/'-'), parentheses('('/')'), space
#        
# Article:  http://www2.lawrence.edu/fast/GREGGJ/CMSC150/071Calculator/Calculator.html

def precedence(op):
    if op in '+-': return 1
    if op in '*/': return 2
    return 0

def apply_operation(v1,v2,op):
    if op=='+': return v1+v2
    if op=='-': return v1-v2
    if op=='*': return v1*v2
    if op=='/': return v1//v2

def evaluate1(string):
    values,ops=[],[]

    i,n=0,len(string)
    new_value=1
    value,sign=1,0
    while i<n:
        c=string[i]
        if c not in r" 1234567890+-*/()":
            raise ValueError("Invalid characters in expression")
        elif c==' ':
            i+=1
            continue

        # get value
        i+=1

    while ops:
        v1=values.pop()
        v2=values.pop()
        op=ops.pop()
        values.append(apply_operation(v1,v2,op))

    return values[-1]


def evaluate(tokens): 
    values = [] 
    ops = [] 
    i = 0
      
    while i < len(tokens): 
        if tokens[i] == ' ': 
            i += 1
            continue
        elif tokens[i] == '(': 
            ops.append(tokens[i]) 
        elif tokens[i].isdigit(): 
            val = 0
            while (i < len(tokens) and
                tokens[i].isdigit()): 
              
                val = (val * 10) + int(tokens[i]) 
                i += 1
            values.append(val) 
        elif tokens[i] == ')': 
            while len(ops) != 0 and ops[-1] != '(': 
              
                val2 = values.pop() 
                val1 = values.pop() 
                op = ops.pop() 
                  
                values.append(apply_operation(val1, val2, op)) 
            ops.pop() 
        else: 
            while (len(ops) != 0 and
                precedence(ops[-1]) >= precedence(tokens[i])): 
                          
                val2 = values.pop() 
                val1 = values.pop() 
                op = ops.pop() 
                  
                values.append(apply_operation(val1, val2, op)) 
              
            ops.append(tokens[i]) 
          
        i += 1

    while len(ops) != 0: 
        val2 = values.pop() 
        val1 = values.pop() 
        op = ops.pop() 
                  
        values.append(apply_operation(val1, val2, op)) 
      
    return values[-1] 


assert apply_operation(1,2,'+')==3
assert evaluate("1+(2+3)")==4
assert evaluate("1+(2*3)")==7

