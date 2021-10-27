
def unique_ways(m,  n) :
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1

    #  Initialize first column.
    for i in range(1, m) :
        dp[i][0] = dp[i - 1][0]

    #  Initialize first row.
    for j in range(1, n) :
        dp[0][j] = dp[0][j - 1]

    for i in range(1, m) :
        for j in range(1, n) :
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]    

    return  dp[m - 1][n - 1]

#  Diagonal movement allowed.
def unique_3ways(m,  n) :
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1

    #  Initialize first column.
    for i in range(1, m) :
        dp[i][0] = dp[i - 1][0]

    #  Initialize first row.
    for j in range(1, n) :
        dp[0][j] = dp[0][j - 1]

    for i in range(1, m) :
        for j in range(1, n) :
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1]    

    return  dp[m - 1][n - 1]

#  Testing code
print(unique_ways(3, 3))
print(unique_3ways(3, 3))

"""
6
13
"""