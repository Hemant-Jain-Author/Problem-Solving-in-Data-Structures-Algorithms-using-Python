
def longest_common_subseq(X,  Y) :
    m = len(X)
    n = len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)] #  Dynamic programming array.
    p = [[0] * (n + 1) for _ in range(m + 1)] #  For printing the substring.
    
    #  Fill dp list in bottom up fashion.
    for i in range(1, m+1) :
        for j in range(1, n+1) :
            if (X[i - 1] == Y[j - 1]) :
                dp[i][j] = dp[i - 1][j - 1] + 1
                p[i][j] = 0
            else :
                dp[i][j] = dp[i - 1][j] if (dp[i - 1][j] > dp[i][j - 1]) else dp[i][j - 1]
                p[i][j] = 1 if (dp[i - 1][j] > dp[i][j - 1]) else 2

    print_LCS(p, X, m, n)
    return  dp[m][n]

def print_LCS(p,  X,  i,  j) :
    if (i == 0 or j == 0) :
        return
    if (p[i][j] == 0) :
        print_LCS(p, X, i - 1, j - 1)
        print(X[i - 1], end ="")
    elif (p[i][j] == 1) : 
        print_LCS(p, X, i - 1, j)
    else :
        print_LCS(p, X, i, j - 1)

X = "carpenter"
Y = "sharpener"
print("\nLongest common subseq length:", longest_common_subseq(X, Y))

"""
arpener
Longest common subseq length: 7
"""