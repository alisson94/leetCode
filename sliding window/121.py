def maxProfit(prices) -> int:
    min = 101
    profit = 0

    for price in prices:
        if price < min:
            min = price
            continue

        cur_profit = price - min
        if cur_profit > profit:
            profit = cur_profit

    return profit
            



print(maxProfit([10,8,7,5,2]))