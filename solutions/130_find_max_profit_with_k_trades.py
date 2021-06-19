#!/usr/bin/python

"""

This problem was asked by Facebook.

Given an array of numbers representing the stock prices of a company in chronological order and an integer k, return the maximum profit you can make from k buys and sells. You must buy the stock before you can sell it, and you must sell the stock before you can buy it again.

For example, given k = 2 and the array [5, 2, 4, 0, 1], you should return 3.

"""

# O(2^n)
def helper(prices,n,index,profit,remain_buys,remain_sells,records=[]):
    if index==n or not remain_sells:
        print("records:",records,"profit:",profit)
        return profit

    profit_hold=helper(prices,n,index+1,profit,remain_buys,remain_sells,records[:])

    price=prices[index]
    if remain_buys<remain_sells:
        # already buy stocks, sell the stocks
        profit_sell=helper(prices,n,index+1,profit+price,remain_buys,remain_sells-1,records+[price])
        return max(profit_hold,profit_sell)
    elif remain_buys==remain_sells:
        # buy stocks
        profit_buy=helper(prices,n,index+1,profit-price,remain_buys-1,remain_sells,records+[price])
        return max(profit_hold,profit_buy)

def get_max_profit_from_k_trades(prices,k):
    return helper(prices,len(prices),0,0,k,k,[])

# DP method

assert get_max_profit_from_k_trades([5,2,4,0,1],2)==3
