#!/usr/bin/python

"""
This problem was asked by Alibaba.

Given an even number (greater than 2), return two prime numbers whose sum will be equal to the given number.

A solution will always exist. See Goldbach's conjecture.

Example:

Input: 4
Output: 2 + 2 = 4

If there are more than one solution possible, return the lexicographically smaller solution.

If [a, b] is one solution with a <= b, and [c, d] is another solution with c <= d, then

[a, b] < [c, d]

If a < c OR a==c AND b < d.

"""

def get_primes(n):
    is_prime = [True]*(n+1)
    p = 2
    while p*p <= n:
        if is_prime[p]:
            i = p * p
            while i <= n:
                is_prime[i] = False
                i += p
        p += 1

    return is_prime

def get_two_prime_numbers_sum_to_target(n):
    is_prime=get_primes(n)
    #print("is_prime: ",is_prime)
    for i in range(2,n+1):
        if is_prime[i] and is_prime[n-i]:
            return (i, n-i)
    return ()

assert get_two_prime_numbers_sum_to_target(4) == (2,2)
assert get_two_prime_numbers_sum_to_target(74) == (3,71)
