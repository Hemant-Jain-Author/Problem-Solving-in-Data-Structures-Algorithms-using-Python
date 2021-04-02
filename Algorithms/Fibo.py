def fibonacci2(n):
    if n <= 1:
        return n
    return fibonacci2(n - 1) + fibonacci2(n - 2)

   
def fibonacci(n):
    first = 0
    second = 1
    if (n == 0):
        return first
    elif (n == 1):
        return second
    i = 2
    while(i <= n):
        temp = first + second
        first = second
        second = temp
        i += 1
    return temp


print(fibonacci(10))
# 55

print(fibonacci2(10))
# 55
