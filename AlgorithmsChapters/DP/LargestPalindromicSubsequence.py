import math
#  Palindromic Subsequence
def largest_palindromic_subsequence(str) :
    n = len(str)
    dp = [[0] * n for _ in range(n)]
    for i in range(n) :
        dp[i][i] = 1    #  each char is itself palindromic with length 1
    
    for l in range(1, n) :
        i = 0 
        for j in range (l, n) :
            if (str[i] == str[j]) : 
                dp[i][j] = dp[i + 1][j - 1] + 2
            else :
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
            i += 1
            
    return  dp[0][n - 1]

str = "ABCAUCBCxxCBA"
print("Max Palindromic Subsequence length: ", largest_palindromic_subsequence(str))

"""
Max Palindromic Subsequence length:  9
"""
