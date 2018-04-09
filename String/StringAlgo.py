#!/usr/bin/env python
from collections import Counter
import math

def matchExpUtil(exp, text, i, j):
    if i == len(exp) and j == len(text):
        return True
    if (i == len(exp) and j != len(text)) or (i != len(exp) and j == len(text)):
        return False
    if exp[i] == '?' or exp[i] == text[j]:
        return matchExpUtil(exp, text, i + 1, j + 1)
    if exp[i] == '*':
        return matchExpUtil(exp, text, i + 1, j) or matchExpUtil(exp, text, i, j + 1) or matchExpUtil(exp, text, i + 1, j + 1)
    return False

def matchExp(exp, text):
    return matchExpUtil(exp, text, 0, 0)

# Match if the pattern is present in the source text.
def match(source, pattern):
    iSource = 0
    iPattern = 0
    sourceLen = len(source)
    patternLen = len(pattern)
    while iSource < sourceLen:
        if source[iSource] == pattern[iPattern]:
            iPattern += 1
        if iPattern == patternLen:
            return True
        iSource += 1
    return False

def myStrdup(src):
    length = len(src)
    dst = [None] * length
    index = 0
    for ch in src:
        dst[index] = ch
        index += 1
    return dst

def isPrime(n):
    if (n > 1):
        answer = True  
    else:
        answer = False
    i = 2
    while i * i <= n:
        if n % i == 0:
            answer = False
            break
        i += 1
    return answer

def myAtoi(text):
    value = 0
    size = len(text)
    i = 0
    while i < size:
        value = (value << 3) + (value << 1) + (ord(text[i]) - ord('0'))
        i += 1
    return value

def isUniqueChar(text):
    charset = set()
    for ch in text:
        if(ch in charset):
            return False
        charset.add(ch)
    return True

def isPermutation(s1, s2):
    mycounter = Counter()
    if len(s1) != len(s2):
        return False
    
    for ch in s1:
        mycounter[ch] += 1
    
    for ch in s2:
        if (ch in mycounter) == False:
            return False
        
        if(mycounter[ch] == 1):
            mycounter.pop(ch)
        else:
            mycounter[ch] -= 1
    return (len(mycounter) == 0)

def isPalindrome(text):
    i = 0
    j = len(text) - 1
    while i < j and text[i] == text[j]:
        i += 1
        j -= 1
    if i < j:
        print("String is not a Palindrome")
        return False
    else:
        print("String is a Palindrome")
        return True

def pow(x, n):
    value = int()
    if n == 0:
        return (1)
    elif n % 2 == 0:
        value = pow(x, math.floor(n / 2))
        return (value * value)
    else:
        value = pow(x, math.floor(n / 2))
        return (x * value * value)

def myStrcmp(a, b):
    index = 0
    len1 = len(a)
    len2 = len(b)
    minlen = len1
    if len1 > len2:
        minlen = len2
    while index < minlen and a[index] == b[index]:
        index += 1
    if index == len1 and index == len2:
        return 0
    elif len1 == index:
        return -1
    elif len2 == index:
        return 1
    else:
        return ord(a[index]) - ord(b[index])


def reverseString(a):
    a = list(a)
    lower = 0
    upper = len(a) - 1
    while lower < upper:
        tempChar = a[lower]
        a[lower] = a[upper]
        a[upper] = tempChar
        lower += 1
        upper -= 1
    return "".join(a)

def reverseStringUtil(a, lower, upper):
    while lower < upper:
        tempChar = a[lower]
        a[lower] = a[upper]
        a[upper] = tempChar
        lower += 1
        upper -= 1

def reverseWords(a):
    a = list(a)
    length = len(a)
    upper = -1
    lower = 0
    i = 0
    while i <= length:
        if i == length or a[i] == ' ':
            reverseStringUtil(a, lower, upper)
            lower = i + 1
            upper = i
        else:
            upper += 1
        i += 1
    reverseStringUtil(a, 0, length - 1)
    return "".join(a)

def printAnagram(a):
    n = len(a)
    a = list(a)
    printAnagramUtil(a, n, n)


def printAnagramUtil(a, maxindex, n):
    if maxindex == 1:
        print("".join(a))
    i = -1
    while i < maxindex - 1:
        if i != -1:
            temp = a[i]
            a[i] = a[maxindex - 1] 
            a[maxindex - 1] = temp
        printAnagramUtil(a, maxindex - 1, n)
        if i != -1:
            temp = a[i] 
            a[i] = a[maxindex - 1] 
            a[maxindex - 1] = temp
        i += 1

def shuffle(text):
    n = math.floor(len(text) / 2)
    ar = list(text)
    count = 0
    k = 1
    temp = '\0'
    i = 1
    while i < n:
        temp = ar[i]
        k = i
        while True:
            k = (2 * k) % (2 * n - 1)
            temp2 = ar[k]
            ar[k] = temp
            temp = temp2
            count += 1
            if not ((i != k)):
                break
            
        if count == (2 * n - 2):
            break
        i = i + 2
    return "".join(ar)

def addBinary(first, second):
    size1 = len(first)
    size2 = len(second)
    totalIndex = 0
    total = []
    if size1 > size2:
        total = [0] * (size1 + 1)
        totalIndex = size1
    else:
        total = [0] * (size2 + 1)
        totalIndex = size2
    carry = 0
    size1 -= 1
    size2 -= 1
    while size1 >= 0 or size2 >= 0:
        firstValue = 0
        secondValue = 0 
        if (size1 >= 0):
            firstValue = ord(first[size1]) - ord('0');
        if (size2 >= 0):
            secondValue = ord(second[size2]) - ord('0');
        sumvalue = firstValue + secondValue + carry
        carry = sumvalue >> 1
        sumvalue = sumvalue & 1
        if (sumvalue == 0):
            total[totalIndex] = '0'  
        else:
            total[totalIndex] ='1'
        totalIndex -= 1
        size1 -= 1
        size2 -= 1
    if (carry == 0):
        total[totalIndex] = '0'  
    else:
        total[totalIndex] = '1'
    return "".join(total)


print(isPalindrome("hello"))
print(isPalindrome("eoloe"))
print(addBinary("1000", "11111111"))
print(matchExp("*ello?","zdfsdfsdhellox"))
print(match("hellappleappleappleapplexxappleapplexxxyyyxyyy","hellappleappleappleapplexxxyyy"))
for i in range(100):
   if(isPrime(i)):
       print(i, end=' ')
print(myAtoi("1000"))
print(isUniqueChar("1213456"))
print(isPermutation("apple","plepa"))
print(pow(5,2))
print(myStrcmp("abs", "abs"))
print(reverseString("apple"))
print(reverseWords("hello world"))
print(printAnagram("1234"))
print(shuffle("ABCDE12345"))
        
