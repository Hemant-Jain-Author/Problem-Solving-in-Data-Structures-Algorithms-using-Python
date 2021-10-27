import math

def edit_dist(str1,  str2) :
    return  edit_dist_util(str1, str2, len(str1), len(str2))

def edit_dist_util (str1,  str2,  m,  n) :
    if (m == 0 or n == 0) : #  If any one string is empty, then empty the other string.
        return  m + n
    #  If last characters of both strings are same, ignore last characters.
    if (str1[m - 1] == str2[n - 1]) :
        return  edit_dist_util (str1, str2, m - 1, n - 1)
    #  If last characters are not same, 
    #  then consider all three operations:
    #  Insert last char of second into first.
    #  Remove last char of first.
    #  Replace last char of first with second.
    return  1 + min(edit_dist_util (str1, str2, m, n - 1), 
    edit_dist_util(str1, str2, m - 1, n), 
    edit_dist_util(str1, str2, m - 1, n - 1))

def edit_dist_dp(str1,  str2) :
    m = len(str1)
    n = len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    #  Fill dp[][] in bottom up manner.
    for i in range(0, m+1) :
        for j in range(0, n+1) :
            #  If any one string is empty, then empty the other string.
            if (i == 0 or j == 0) : 
                dp[i][j] = (i + j)
            elif (str1[i - 1] == str2[j - 1]) : 
                dp[i][j] = dp[i - 1][j - 1]
            else :
                dp[i][j] = 1 + min( dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
    return  dp[m][n]

#  Testing code
str1 = "sunday"
str2 = "saturday"
print("Edit distance is:", edit_dist(str1, str2))
print("Edit distance is:", edit_dist_dp(str1, str2))

"""
Edit distance is: 3
Edit distance is: 3
"""