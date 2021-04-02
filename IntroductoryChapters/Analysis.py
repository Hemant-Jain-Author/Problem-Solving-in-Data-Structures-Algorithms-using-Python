import math

def fun1(n):
    m = 0
    i = 0
    while i < n:
        m += 1
        i += 1
    return m

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

def fun4(n):
    m = 0
    i = 1
    while i < n:
        m += 1
        i = i * 2
    return m

def fun5(n):
    m = 0
    i = n
    while i > 0:
        m += 1
        i = i / 2
    return m

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

def fun9(n):
    m = 0
    i = n
    while i > 0:
        j = 0
        while j < i:
            m += 1
            j += 1
        i /= 2
    return m

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

def fun12(n):
    m = 0
    i = 0
    while i < n:
        j = 0
        while j < n:
            m += 1
            j += 1
        i += 1
    return m

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


print("N = 100, Number of instructions in fun1():" , fun1(100))
print("N = 100, Number of instructions in fun2():" , fun2(100))
print("N = 100, Number of instructions in fun3():" , fun3(100))
print("N = 100, Number of instructions in fun4():" , fun4(100))
print("N = 100, Number of instructions in fun5():" , fun5(100))
print("N = 100, Number of instructions in fun6():" , fun6(100))
print("N = 100, Number of instructions in fun7():" , fun7(100))
print("N = 100, Number of instructions in fun8():" , fun8(100))
print("N = 100, Number of instructions in fun9():" , fun9(100))
print("N = 100, Number of instructions in fun10():" , fun10(100))
print("N = 100, Number of instructions in fun11():" , fun11(100))
print("N = 100, Number of instructions in fun12():" , fun12(100))
print("N = 100, Number of instructions in fun13():" , fun13(100))

"""
N = 100, Number of instructions in fun1(): 100
N = 100, Number of instructions in fun2(): 10000
N = 100, Number of instructions in fun3(): 4950
N = 100, Number of instructions in fun4(): 7
N = 100, Number of instructions in fun5(): 1082
N = 100, Number of instructions in fun6(): 1000000
N = 100, Number of instructions in fun7(): 20000
N = 100, Number of instructions in fun8(): 1000
N = 100, Number of instructions in fun9(): 1276
N = 100, Number of instructions in fun10(): 4950
N = 100, Number of instructions in fun11(): 166650
N = 100, Number of instructions in fun12(): 10000
N = 100, Number of instructions in fun13(): 134
"""