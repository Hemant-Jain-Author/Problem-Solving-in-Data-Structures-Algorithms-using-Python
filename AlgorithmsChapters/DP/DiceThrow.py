def find_ways(n,  m,  V) :
    dp = [[0] * (V + 1) for _ in range(n + 1)]
    #  Table entries for only one dice.
    j = 1
    while (j <= m and j <= V) :
        dp[1][j] = 1    
        j += 1
    
    #  i is number of dice, j is Value, k value of dice.
    for i in range(2, n+1) :
        for j in range(1, V+1) :
            k = 1
            while (k <= j and k <= m) :
                dp[i][j] += dp[i - 1][j - k]    
                k += 1
    return  dp[n][V]
    
# Testing code.
for i in range(1, 7) :
    print(find_ways(i, 6, 6))

"""
1
5
10
10
5
1
"""