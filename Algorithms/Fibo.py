def fibonacci2(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

   
def fibonacci(n):
    first = 0
    second = 1
    if (n == 0):
        return first;
    elif (n == 1):
        return second;
    i = 2
    while(i <= n):
        temp = first + second
        first = second
        second = temp
        i += 1
    return temp


print((fibonacci(50)))
print((fibonacci2(50)))
