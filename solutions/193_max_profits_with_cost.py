#!/usr/bin/python

"""

This problem was asked by Affirm.

Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock. You're also given a number fee that represents a transaction fee for each buy and sell transaction.

You must buy before you can sell the stock, but you can make as many transactions as you like.

For example, given [1, 3, 2, 8, 4, 10] and fee = 2, you should return 9, since you could buy the stock at 1 dollar, and sell at 8 dollars, and then buy it at 4 dollars and sell it at 10 dollars. Since we did two transactions, there is a 4 dollar fee, so we have 7 + 6 = 13 profit minus 4 dollars of fees.

"""

# O(2^n)
def max_stock_profit_helper(prices,n,fee,index,profit=0,buyable=True,records=[]):
    if index==n:
        print("records: ", records, "profit: ", profit)
        return profit

    price=prices[index]
    gain=-price if buyable else price-fee

    profit_buy_or_sell=max_stock_profit_helper(prices,n,fee,index+1,profit+gain,not buyable,records+[price])
    profit_hold=max_stock_profit_helper(prices,n,fee,index+1,profit,buyable,records[:])

    return max(profit_buy_or_sell,profit_hold)

def max_stock_profit(prices,fee):
    return max_stock_profit_helper(prices,len(prices),fee,0,0,True,[])

assert max_stock_profit([1, 3, 2, 8, 4, 10],2)==9
