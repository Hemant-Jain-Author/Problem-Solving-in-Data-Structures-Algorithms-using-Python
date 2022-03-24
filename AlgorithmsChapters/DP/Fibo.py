def fibonacci(n) :
    if n < 2 :
        return  n
    
    return  fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_series(n) :
    arr = [0] * n
    for i in range(0, n) :
        arr[i] = fibonacci(i)
    print(arr)

def fibonacci_bu(n) :
    if n < 2 :
        return  n

    dp = [0]*(n+1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n+1) :
        dp[i] = dp[i-1] + dp[i-2]

    return  dp[n]



def fibonacci_td(n) :
    dp = [0] * (n+1)
    fibonacci_td_util(n, dp)
    return dp[n]    

def fibonacci_td_util(n,  dp) :
    if n < 2 :
        dp[n] = n
        return n

    if dp[n] == 0:
        dp[n] = fibonacci_td_util(n - 1, dp) + fibonacci_td_util(n - 2, dp)
    
    return  dp[n]

#  Testing code
print(fibonacci(10))
print(fibonacci_bu(10))
print(fibonacci_td(10))
print(fibonacci(1))
print(fibonacci_bu(1))
print(fibonacci_td(1))
"""
55
55
55
"""