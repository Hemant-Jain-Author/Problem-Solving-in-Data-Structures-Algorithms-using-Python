def is_prime(n):
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

print(is_prime(10))
print(is_prime(11))

"""
False
True
"""