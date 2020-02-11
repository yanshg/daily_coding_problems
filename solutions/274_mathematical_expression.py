#!/usr/bin/python

"""

This problem was asked by Facebook.

Given a string consisting of parentheses, single digits, and positive and negative signs, convert the string into a mathematical expression to obtain the answer.

Don't use eval or a similar built-in parser.

For example, given '-1 + (2 + 3)', you should return 4.

"""

# Idea:     Use 2 stacks: values and oprators
#           '()' has highest precedence, then operator
#
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

def get_number(string,i,n):
    l=0

    # check for sign
    if string[i+l] in r'+-':
        l+=1

    # check for digits
    while i+l<n and string[i+l].isdigit():
        l+=1

    return int(string[i:i+l]),l

def calculate_one_operator(values,ops):
    v2=values.pop()
    v1=values.pop()
    op=ops.pop()
    values.append(apply_operation(v1,v2,op))

def evaluate(string):
    values,ops=[],[]

    # check if invalide characters
    valid_chars=r" 1234567890+-*/()"
    if set(string)-set(valid_chars):
        raise ValueError("Invalid characters in expression")

    #print("string: ", string)
    i,n=0,len(string)
    value_expected=True
    while i<n:

        # skip spaces
        while i<n and string[i]==' ':
            i+=1

        if i==n:
            break

        #print("values:", values, "ops: ",ops)
        if string[i]=='(':
            ops.append('(')
            i+=1
            value_expected=True
        elif string[i]==')':
            while len(values)>1 and len(ops)>0 and ops[-1]!='(':
                calculate_one_operator(values,ops)
            if not ops or ops[-1]!='(':
                raise ValueError("Parenthese is not matched")
            else:
                ops.pop()
            i+=1
            value_expected=False
        elif value_expected:
            # get value
            value,l=get_number(string,i,n)
            i+=l
            values.append(value)
            value_expected=False
        else:
            # get operator
            op=string[i]
            if op in r"+-*/":
                while len(values)>1 and len(ops)>0 and \
                      precedence(op)<=precedence(ops[-1]):
                    calculate_one_operator(values,ops)

                ops.append(op)
            else:
                raise ValueError("Invalid Operator")

            i+=1
            value_expected=True

    while len(values)>1 and len(ops)>0:
        calculate_one_operator(values,ops)

    return values[-1]

assert apply_operation(1,2,'+')==3
assert evaluate("-1+(2+3)")==4
assert evaluate("-1+(2+3)*3-5+2*3")==15

