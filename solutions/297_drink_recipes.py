#!/usr/bin/python

"""

This problem was asked by Amazon.

At a popular bar, each customer has a set of favorite drinks, and will happily accept any drink among this set. For example, in the following situation, customer 0 will be satisfied with drinks 0, 1, 3, or 6.

preferences = {
    0: [0, 1, 3, 6],
    1: [1, 4, 7],
    2: [2, 4, 7, 5],
    3: [3, 2, 5],
    4: [5, 8]
}

A lazy bartender working at this bar is trying to reduce his effort by limiting the drink recipes he must memorize. Given a dictionary input such as the one above, return the fewest number of drinks he must learn in order to satisfy all customers.

For the input above, the answer would be 2, as drinks 1 and 5 will satisfy everyone.

"""

from collections import defaultdict

def get_min_drinks(preferences):
    drinks_custs=defaultdict(set)
    for cust in preferences:
        for drink in preferences[cust]:
            drinks_custs[drink].add(cust)
    drinks=set(drinks_custs.keys())
    custs=set(preferences.keys())

    min_option=minimize_drinks(drinks,custs,remaining_

preferences = {
    0: [0, 1, 3, 6],
    1: [1, 4, 7],
    2: [2, 4, 7, 5],
    3: [3, 2, 5],
    4: [5, 8]
}

assert get_min_drinks(preferences)==2
