import math

def fun1(n):
    m = 0
    i = 0
    while i < n:
        m += 1
        i += 1
    return m

print("N = 100, Number of instructions in O(n)::", fun1(100))

"""
N = 100, Number of instructions in O(n):: 100
"""

def fun2(n):
    m = 0
    i = 0
    while i < n:
        j = 0
        while j < n:
            m += 1
            j += 1
        i += 1
    return m

print("N = 100, Number of instructions in O(n^2)::", fun2(100))

"""
N = 100, Number of instructions in O(n^2):: 10000
"""

def fun3(n):
    m = 0
    i = 0
    while i < n:
        j = 0
        while j < i:
            m += 1
            j += 1
        i += 1
    return m

print("N = 100, Number of instructions in O(n^2)::", fun3(100))

"""
N = 100, Number of instructions in O(n^2):: 4950
"""

def fun4(n):
    m = 0
    i = 1
    while i < n:
        m += 1
        i = i * 2
    return m

print("N = 100, Number of instructions in O(log(n))::", fun4(100))

"""
N = 100, Number of instructions in O(log(n)):: 7
"""

def fun5(n):
    m = 0
    i = n
    while i > 0:
        m += 1
        i = i // 2
    return m

print("N = 100, Number of instructions in O(log(n))::", fun5(100))

"""
N = 100, Number of instructions in O(log(n)):: 7
"""

def fun6(n):
    m = 0
    i = 0
    while i < n:
        j = 0
        while j < n:
            k = 0
            while k < n:
                m += 1
                k += 1
            j += 1
        i += 1
    return m

print("N = 100, Number of instructions in O(n^3)::", fun6(100))

"""
N = 100, Number of instructions in O(n^3):: 1000000
"""

def fun7(n):
    m = 0
    i = 0
    while i < n:
        j = 0
        while j < n:
            m += 1
            j += 1
        i += 1
    i = 0
    while i < n:
        k = 0
        while k < n:
            m += 1
            k += 1
        i += 1
    return m

print("N = 100, Number of instructions in O(n^2)::", fun7(100))

"""
N = 100, Number of instructions in O(n^2):: 20000
"""

def fun8(n):
    m = 0
    i = 0
    while i < n:
        j = 0
        while j < math.sqrt(n):
            m += 1
            j += 1
        i += 1
    return m

print("N = 100, Number of instructions in O(n^(3/2))::", fun8(100))

"""
N = 100, Number of instructions in O(n^(3/2)):: 1000
"""

def fun9(n):
    m = 0
    i = n
    while i > 0:
        j = 0
        while j < i:
            m += 1
            j += 1
        i //= 2
    return m

print("N = 100, Number of instructions in O(n)::", fun9(100))

"""
N = 100, Number of instructions in O(n):: 197
"""

def fun10(n):
    m = 0
    i = 0
    while i < n:
        j = i
        while j > 0:
            m += 1
            j -= 1
        i += 1
    return m

print("N = 100, Number of instructions in O(n^2)::", fun10(100))

"""
N = 100, Number of instructions in O(n^2):: 4950
"""

def fun11(n):
    m = 0
    i = 0
    while i < n:
        j = i
        while j < n:
            k = j + 1
            while k < n:
                m += 1
                k += 1
            j += 1
        i += 1
    return m

print("N = 100, Number of instructions in O(n^3)::", fun11(100))

"""
N = 100, Number of instructions in O(n^3):: 166650
"""

def fun12(n):
    m = 0
    i = 0
    j = 0
    while i < n:
        while j < n:
            m += 1
            j += 1
        i += 1
    return m

print("N = 100, Number of instructions in O(n)::", fun12(100))

"""
N = 100, Number of instructions in O(n):: 100
"""

def fun13(n):
    m = 0
    i = 1
    while i <= n:
        j = 0
        while j <= i:
            m += 1
            j += 1
        i *= 2
    return m

print("N = 100, Number of instructions in O(n)::", fun13(100))

"""
N = 100, Number of instructions in O(n):: 134
"""