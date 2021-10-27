#  Palindromic Substrings
def largest_palindromic_substring(str) :
    n = len(str)
    dp = [[0] * n for _ in range(n)]
    for i in range(n) :
        dp[i][i] = 1    

    mx = 1
    start = 0
    for l in range(1, n) :
        i = 0
        for j in range(l, n) :
            if (str[i] == str[j] and dp[i + 1][j - 1] == j - i - 1) :
                dp[i][j] = dp[i + 1][j - 1] + 2
                if (dp[i][j] > mx) :
                    mx = dp[i][j]
                    #  Keeping track of mx length and 
                    start = i
            else :
                dp[i][j] = 0
            i += 1 
    print("Max Length Palindromic Substrings : " + str[start:start + mx])
    return  mx

str = "ABCAUCBCxxCBA"
print("Max Palindromic Substrings len: ", largest_palindromic_substring(str))

"""
Max Length Palindromic Substrings : BCxxCB
Max Palindromic Substrings len:  6
"""