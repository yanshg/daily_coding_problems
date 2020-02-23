#!/usr/bin/python

"""

This problem was asked by Facebook.

Mastermind is a two-player game in which the first player attempts to guess the secret code of the second. In this version, the code may be any six-digit number with all distinct digits.

Each turn the first player guesses some number, and the second player responds by saying how many digits in this number correctly matched their location in the secret code. For example, if the secret code were 123456, then a guess of 175286 would score two, since 1 and 6 were correctly placed.

Write an algorithm which, given a sequence of guesses and their scores, determines whether there exists some secret code that could have produced them.

For example, for the following scores you should return True, since they correspond to the secret code 123456:
 {175286: 2, 293416: 3, 654321: 0}

However, it is impossible for any key to result in the following scores, so in this case you should return False:
 {123456: 4, 345678: 4, 567890: 4}

"""

def is_code_guess_match(code,guess,count):
    matched=0
    for pair in zip(list(str(code)),list(str(guess))):
        if pair[0]==pair[1]:
            matched+=1
    return matched==count

def is_valid_guesses(guesses):
    for code in range(100000,1000000):
        valid=True
        for guess,count in guesses.items():
            if not is_code_guess_match(code,guess,count):
                valid=False
                break
        if valid:
            print("code:",code)
            return True
    return False

assert is_valid_guesses({175286: 2, 293416: 3, 654321: 0})
assert not is_valid_guesses({123456: 4, 345678: 4, 567890: 4})
