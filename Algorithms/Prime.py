def isPrime(n):
    if(n > 1):
        answer = True
    else:
        answer = False
    i = 2
    while(i*i <= n):
        if(n % i == 0):
            answer = False
            break
        i += 1
    return answer

print(isPrime(50))
print(isPrime(47))