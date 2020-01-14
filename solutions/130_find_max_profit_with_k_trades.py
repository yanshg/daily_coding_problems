#!/usr/bin/python

"""

This problem was asked by Facebook.

Given an array of numbers representing the stock prices of a company in chronological order and an integer k, return the maximum profit you can make from k buys and sells. You must buy the stock before you can sell it, and you must sell the stock before you can buy it again.

For example, given k = 2 and the array [5, 2, 4, 0, 1], you should return 3.

"""

def helper(prices,curr_index,curr_profit,remain_buys,remain_sells):
    if (curr_index==len(prices)) or not remain_sells:
        return curr_profit

    if remain_buys<remain_sells:
        # already buy stocks, you can hold or sell the stocks
        profit_hold=helper(prices,curr_index+1,curr_profit,remain_buys,remain_sells)
        profit_sell=helper(prices,curr_index+1,curr_profit+prices[curr_index],remain_buys,remain_sells-1)
        return max(profit_hold,profit_sell)
    elif remain_buys==remain_sells:
        # you can wait or buy but can not sell stocks
        profit_hold=helper(prices,curr_index+1,curr_profit,remain_buys,remain_sells)
        profit_buy=helper(prices,curr_index+1,curr_profit-prices[curr_index],remain_buys-1,remain_sells)
        return max(profit_hold,profit_buy)

def get_max_profit_from_k_trades(prices, k):
    return helper(prices,0,0,k,k)

assert get_max_profit_from_k_trades([5,2,4,0,1], 2)==3
