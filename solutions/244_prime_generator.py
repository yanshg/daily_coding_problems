#!/usr/bin/python

"""

This problem was asked by Square.

The Sieve of Eratosthenes is an algorithm used to generate all prime numbers smaller than N. The method is to take increasingly larger prime numbers, and mark their multiples as composite.

For example, to find all primes less than 100, we would first mark [4, 6, 8, ...] (multiples of two), then [6, 9, 12, ...] (multiples of three), and so on. Once we have done this for all primes less than N, the unmarked numbers that remain will be prime.

Implement this algorithm.

Bonus: Create a generator that produces primes indefinitely (that is, without taking N as an input).

"""

def get_next_prime():
    prime_seen=[2]
    num=2
    while True:
        num+=1
        if all([num % x for x in prime_seen]):
            yield prime_seen[-1]
            prime_seen+=[num]


def get_primes(n):
    primes=[]
    for p in get_next_prime():
        if p>n:
            break
        primes+=[p]
    return primes


assert get_primes(10)==[2,3,5,7]
