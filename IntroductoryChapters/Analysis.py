#!/usr/bin/env python

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


print "Value of M fun1():" , fun1(100)
print "Value of M fun2():" , fun2(100)
print "Value of M fun3():" , fun3(100)
print "Value of M fun4():" , fun4(100)
print "Value of M fun5():" , fun5(100)
print "Value of M fun6():" , fun6(100)
print "Value of M fun7():" , fun7(100)
print "Value of M fun8():" , fun8(100)
print "Value of M fun9():" , fun9(100)
print "Value of M fun10():" , fun10(100)
print "Value of M fun11():" , fun11(100)
print "Value of M fun12():" , fun12(100)
print "Value of M fun13():" , fun13(100)
