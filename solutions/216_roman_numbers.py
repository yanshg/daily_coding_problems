#!/usr/bin/python

"""

This problem was asked by Facebook.

Given a number in Roman numeral format, convert it to decimal.

The values of Roman numerals are as follows:

{
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}

In addition, note that the Roman numeral system uses subtractive notation for numbers such as IV and XL.

For the input XIV, for instance, you should return 14.

"""

# Article:  https://www.mathsisfun.com/roman-numerals.html

# Idea:  When a symbol appears after a larger (or equal) symbol it is added
#        But if the symbol appears before a larger symbol it is subtracted

#        Think "MeDiCaL XaVIer". It has the roman numerals in descending order from 1000 to 1.

def value(c):
    mapping={ 'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1 }
    return mapping.get(c, 0)

def convert_roman_to_decimal(s):
    result=0
    for i in range(len(s)):
        v=value(s[i])
        if not v:
            raise ValueError("Not valid Roman string")
        result+=v

        if i>0 and v>value(s[i-1]):
            result-=2*value(s[i-1])

    return result

assert convert_roman_to_decimal('XIV')==14
