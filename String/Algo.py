#!/usr/bin/env python
    
def BruteForceSearch(text, pattern):
    i = 0
    n = len(text)
    m = len(pattern)
    while i <= n - m:
        j = 0
        while j < m and pattern[j] == text[i + j]:
            j += 1
        if j == m:
            return i
        i += 1
    return -1
   
def RobinKarp(text, pattern):
    n = len(text)
    m = len(pattern)
    prime = 101
    powm = 1
    TextHash = 0
    PatternHash = 0
    if m == 0 or m > n:
        return -1
    i = 0
    while i < m - 1:
        powm = (powm << 1) % prime
        i += 1
    i = 0
    while i < m:
        PatternHash = ((PatternHash << 1) + ord(pattern[i])) % prime
        TextHash = ((TextHash << 1) + ord(text[i])) % prime
        i += 1
    i = 0
    while i <= (n - m):
        if TextHash == PatternHash:
            j = 0
            while j < m:
                if text[i + j] != pattern[j]:
                    break
                j += 1
            if j == m:
                return i
        TextHash = (((TextHash - ord(text[i]) * powm) << 1) + ord(text[i + m])) % prime
        if TextHash < 0:
            TextHash = (TextHash + prime)
        i += 1
    return -1

def KMPPreprocess(pattern, ShiftArr):
    m = len(pattern)
    i = 0
    j = -1
    ShiftArr[i] = -1
    while i < m:
        while j >= 0 and pattern[i] != pattern[j]:
            j = ShiftArr[j]
        i += 1
        j += 1
        ShiftArr[i] = j

def KMP(text, pattern):
    i = 0
    j = 0
    n = len(text)
    m = len(pattern)
    ShiftArr = [0] * (m + 1)
    KMPPreprocess(pattern, ShiftArr)
    while i < n:
        while j >= 0 and text[i] != pattern[j]:
            j = ShiftArr[j]
        i += 1
        j += 1
        if j == m:
            return (i - m)
    return -1

def KMPFindCount(text, pattern):
    i = 0
    j = 0
    count = 0
    n = len(text)
    m = len(pattern)
    ShiftArr = [0] * (m + 1)
    KMPPreprocess(pattern, ShiftArr)
    while i < n:
        while j >= 0 and text[i] != pattern[j]:
            j = ShiftArr[j]
        i += 1
        j += 1
        if j == m:
            count += 1
            j = ShiftArr[j]
    return count

st1 = "hello, world!"
st2 = "world"
print("BruteForceSearch return : " , BruteForceSearch(st1, st2))
print("RobinKarp return : " , RobinKarp(st1, st2))
print("KMP return : " , KMP(st1, st2))