#!/usr/bin/python

"""

This problem was asked by Two Sigma.

You’re tracking stock price at a given instance of time. Implement an API with the following functions: add(), update(), remove(), which adds/updates/removes a datapoint for the stock price you are tracking. The data is given as (timestamp, price), where timestamp is specified in unix epoch time.

Also, provide max(), min(), and average() functions that give the max/min/average of all values seen thus far.

"""

class StockPriceTracking:
    def __init__(self):
        self.max_price=0
        self.min_price=0
        self.average_price=0
        pass

    def add(timestamp,price):
        pass

    def update(timestamp,price):
        pass

    def remove(timestamp,price):
        pass

    def max(self):
        return self.max_price

    def min(self):
        return self.min_price

    def average(self):
        return self.average_price
