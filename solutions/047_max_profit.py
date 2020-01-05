#!/usr/bin/python

"""
This problem was asked by Facebook.

Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.
"""

def get_max_profit(prices):
    min_price,max_profit_so_far=float('inf'),0
    for price in prices:
        min_price=min(min_price,price)
        max_profit_so_far=max(max_profit_so_far, price-min_price)
    return max_profit_so_far

assert get_max_profit([9, 11, 8, 5, 7, 10])==5
