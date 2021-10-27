def fibonacci(n) :
    if (n <= 2) :
        return  n - 1
    return  fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_series(n) :
    arr = [0] * n
    for i in range(0, n) :
        arr[i] = fibonacci(i+1)
    print(arr)

def fibonacci_bu(n) :
    if (n <= 2) :
        return  n - 1
    first = 0
    second = 1
    temp = 0
    for i in range(2, n) :
        temp = first + second
        first = second
        second = temp
    return  temp

def fibonacci_series_bu(n) :
    if (n < 1) :
        return
    if (n == 1) :
        print(0)
        return
    dp = [0] * n
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n) :
        dp[i] = dp[i - 2] + dp[i - 1]
    print(dp)

def fibonacci_series_td(n) :
    if (n < 1) :
        return
    dp = [0] * n
    fibonacci_series_td_util(n - 1, dp)
    print(dp)    

def fibonacci_series_td_util(n,  dp) :
    if (n <= 1) :
        dp[n] = n
        return dp[n]
    if (dp[n] != 0) :
        return  dp[n]
    dp[n] = fibonacci_series_td_util(n - 1, dp) + fibonacci_series_td_util(n - 2, dp)
    return  dp[n]

#  Testing code
fibonacci_series(6)
fibonacci_series_bu(6)
fibonacci_series_td(6)
print(fibonacci(6))
print(fibonacci_bu(6))



"""
[0, 1, 1, 2, 3, 5]
[0, 1, 1, 2, 3, 5]
[0, 1, 1, 2, 3, 5]
5
5
"""