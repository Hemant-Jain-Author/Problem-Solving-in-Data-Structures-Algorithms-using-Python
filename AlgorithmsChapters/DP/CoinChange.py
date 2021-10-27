import math
import sys

def min_coins(coins,  n,  val) : # Greedy may be wrong.
    if (val <= 0) :
        return  0
    count = 0
    coins.sort()
    i = n - 1
    while (i >= 0 and val > 0) :
        if (coins[i] <= val) :
            count += 1
            val -= coins[i]
        else :
            i -= 1

    return  count if (val == 0) else -1


def min_coins2(coins,  n,  val) : # Brute force.
    if (val == 0) :
        return  0
        
    count = sys.maxsize
    for i in range (0,  n) :
        if (coins[i] <= val) :
            subCount = min_coins2(coins, n, val - coins[i])
            if (subCount >= 0) : 
                count = min(count,subCount + 1)
    return count if (count != sys.maxsize) else -1

def min_coins_td(coins,  n,  val) : #  DP top down approach.
    dp = [sys.maxsize] * (val + 1)
    return  min_coins_td_util(dp, coins, n, val)

def min_coins_td_util(dp,  coins,  n,  val) : 
    #  Base Case
    if (val == 0) : 
        return  0
    if (dp[val] != sys.maxsize) :
        return  dp[val]

    #  Recursion
    for i in range(0, n) :
        if (coins[i] <= val) : #  check validity of a sub-problem
            subCount = min_coins_td_util(dp, coins, n, val - coins[i])
            if (subCount != sys.maxsize) : 
                dp[val] = min(dp[val], subCount + 1)
    return  dp[val]

def min_coins_bu(coins,  n,  val) : #  DP bottom up approach.
    dp = [sys.maxsize] * (val + 1)
    dp[0] = 0 #  Base value.

    for i in range (1, val+1) :
        for j in range (0, n) :
            if (coins[j] <= i) : #  For all coins smaller than or equal to i.
                if (dp[i - coins[j]] != sys.maxsize) : 
                    dp[i] = min(dp[i],dp[i - coins[j]] + 1)
    return  dp[val] if (dp[val] != sys.maxsize) else -1

#  Testing code
coins = [5, 6]
value = 16
n = len(coins)
print("Count is:" + str(min_coins(coins, n, value)))
print("Count is:" + str(min_coins2(coins, n, value)))
print("Count is:" + str(min_coins_bu(coins, n, value)))
print("Count is:" + str(min_coins_td(coins, n, value)))

"""
Count is:-1
Count is:3
Count is:3
Count is:3
"""