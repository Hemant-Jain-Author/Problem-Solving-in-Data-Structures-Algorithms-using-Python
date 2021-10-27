
def stock_buy_sell_profit(arr) :
    buy_profit = -arr[0]  #  Buy stock profit
    sell_profit = 0  #  Sell stock profit
    n = len(arr)
    for i in range(1, n) :
        new_buy_profit = (sell_profit - arr[i]) if ((sell_profit - arr[i]) > buy_profit)  else buy_profit
        new_sell_profit = (buy_profit + arr[i]) if ((buy_profit + arr[i]) > sell_profit)  else sell_profit

        buy_profit = new_buy_profit
        sell_profit = new_sell_profit

    return  sell_profit

def stock_buy_sell_profit_tc(arr,  t) :
    buy_profit = -arr[0]
    sell_profit = 0
    n = len(arr)

    for i in range(1, n) :
        new_buy_profit = (sell_profit - arr[i]) if ((sell_profit - arr[i]) > buy_profit)  else buy_profit
        new_sell_profit = (buy_profit + arr[i] - t) if ((buy_profit + arr[i] - t) > sell_profit)  else sell_profit
        buy_profit = new_buy_profit
        sell_profit = new_sell_profit

    return  sell_profit

def stock_buy_sell_profit2(arr) :
    n = len(arr)
    dp = [[0] * (2) for _ in range(n)]
    dp[0][0] = -arr[0]  #  Buy stock profit
    dp[0][1] = 0  #  Sell stock profit

    for i in range(1, n) :
        dp[i][0] = dp[i - 1][1] - arr[i] if (dp[i - 1][1] - arr[i] > dp[i - 1][0]) else dp[i - 1][0]
        dp[i][1] = dp[i - 1][0] + arr[i] if (dp[i - 1][0] + arr[i] > dp[i - 1][1]) else dp[i - 1][1]

    return  dp[n - 1][1]

def stock_buy_sell_profit_tc2(arr,  t) :
    n = len(arr)
    dp = [[0] * (2) for _ in range(n)]
    dp[0][0] = -arr[0]
    dp[0][1] = 0

    for i in range(1, n) :
        dp[i][0] = (dp[i - 1][1] - arr[i]) if ((dp[i - 1][1] - arr[i]) > dp[i - 1][0]) else dp[i - 1][0]
        dp[i][1] = (dp[i - 1][0] + arr[i] - t) if ((dp[i - 1][0] + arr[i] - t) > dp[i - 1][1])  else dp[i - 1][1]

    return  dp[n - 1][1]


arr = [10, 12, 9, 23, 25, 55, 49, 70]
print("Total profit: ", stock_buy_sell_profit(arr))
print("Total profit: ", stock_buy_sell_profit2(arr))
print("Total profit: ", stock_buy_sell_profit_tc(arr, 2))
print("Total profit: ", stock_buy_sell_profit_tc2(arr, 2))

"""
Total profit:  69
Total profit:  69
Total profit:  63
Total profit:  63
"""