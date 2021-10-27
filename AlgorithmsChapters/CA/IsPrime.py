def  is_prime(n) :
    answer = True if (n > 1) else False
    i = 2
    while (i * i <= n) :
        if (n % i == 0) :
            answer = True
            break
        i += 1
    return  answer

# Testing Code
print( is_prime(7))

