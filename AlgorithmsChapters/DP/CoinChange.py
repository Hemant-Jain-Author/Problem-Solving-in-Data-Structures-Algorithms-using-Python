import math
import sys

def min_coins(d, n, val) : # Greedy may be wrong.
    if (val <= 0) :
        return 0
    count = 0
    d.sort()
    i = n - 1
    while (i >= 0 and val > 0) :
        if (d[i] <= val) :
            count += 1
            val -= d[i]
        else :
            i -= 1

    return count if (val == 0) else -1


def min_coins2(d, n, val) : # Brute force.
    if (val == 0) :
        return 0
        
    count = sys.maxsize
    for i in range (0, n) :
        if (d[i] <= val) :
            sub_count = min_coins2(d, n, val - d[i])
            if (sub_count != -1) : 
                count = min(count, sub_count + 1)

    return count if (count != sys.maxsize) else -1

def min_coins_td(d, n, val) : # DP top down approach.
    coins = [sys.maxsize] * (val + 1)
    return min_coins_td_util(coins, d, n, val)

def min_coins_td_util(coins, d, n, val) : 
    # Base Case
    if (val == 0) : 
        return 0

    if (coins[val] != sys.maxsize) :
        return coins[val]

    # Recursion
    for i in range(0, n) :
        if (d[i] <= val) : # check validity of a sub-problem
            sub_count = min_coins_td_util(coins, d, n, val - d[i])
            if (sub_count != sys.maxsize) : 
                coins[val] = min(coins[val], sub_count + 1)
    return coins[val]

def min_coins_bu(d, n, val) : # DP bottom up approach.
    # coins[i] used to store number of coins required to make sum i
    coins = [sys.maxsize] * (val + 1)
    coins[0] = 0 # Base value.

    for i in range (1, val+1) :
        for j in range (0, n) :
            if (d[j] <= i) : # For all coins smaller than or equal to i.
                if (coins[i - d[j]] != sys.maxsize) : 
                    coins[i] = min(coins[i], coins[i - d[j]] + 1)
    return coins[val] if (coins[val] != sys.maxsize) else -1


def min_coins_bu2(d, n, val) : # DP bottom up approach.
    # coins[i] used to store number of coins required to make sum i
    coins = [sys.maxsize] * (val + 1)
    deno = [sys.maxsize] * (val + 1)
    coins[0] = 0 # Base value.

    for i in range (1, val+1) :
        for j in range (0, n) :
            # For all coins smaller than or equal to i.
            if d[j] <= i and coins[i - d[j]] != sys.maxsize and coins[i] > coins[i - d[j]] + 1: 
                coins[i] = coins[i - d[j]] + 1
                deno[i] = d[j]

    print_coins(deno, val)
    return coins[val] if (coins[val] != sys.maxsize) else -1

def print_coins_util(deno, val) :
    if val > 0 :
        print_coins_util(deno, val - deno[val])
        print(deno[val], end=" ")

def print_coins(deno, val) :
    print("Coins are : ", end="")
    print_coins_util(deno, val)
    print()

# Testing code
d = [1, 4, 6, 9, 12]
value = 15
n = len(d)
print("Coins count :" + str(min_coins(d, n, value)))
print("Coins count :" + str(min_coins2(d, n, value)))
print("Coins count :" + str(min_coins_bu(d, n, value)))
print("Coins count :" + str(min_coins_bu2(d, n, value)))
print("Coins count :" + str(min_coins_td(d, n, value)))

"""
Coins count :-1
Coins count :3
Coins count :3
Coins are : 6 5 5 
Coins count :3
Coins count :3
"""