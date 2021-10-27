from collections import Counter
import math

def match_exp_util(exp, text, i, j):
    if i == len(exp) and j == len(text):
        return True
    if (i == len(exp) and j != len(text)) or (i != len(exp) and j == len(text)):
        return False
    if exp[i] == '?' or exp[i] == text[j]:
        return match_exp_util(exp, text, i + 1, j + 1)
    if exp[i] == '*':
        return match_exp_util(exp, text, i + 1, j) or match_exp_util(exp, text, i, j + 1) or match_exp_util(exp, text, i + 1, j + 1)
    return False

def match_exp(exp, text):
    return match_exp_util(exp, text, 0, 0)

# Testing code.
def main1():
    print(match_exp("hello*", "helloworld"))
    print(match_exp("hello?d", "hellowd"))
    print(match_exp("hello*hemant", "helloworldfsdfsdfdsfhemant"))
    print(match_exp("*hemantj", "helloworldfsdfsdfdsfhemant"))

#main1()

"""
True
True
True
False
"""

# Match if the pattern is present in the source text.
def match(source, pattern):
    index_source = 0
    index_pattern = 0
    sourceLen = len(source)
    patternLen = len(pattern)
    while index_source < sourceLen:
        if source[index_source] == pattern[index_pattern]:
            index_pattern += 1
        if index_pattern == patternLen:
            return True
        index_source += 1
    return False

# Testing code.
def main2():
    print(match("hellofskdlfjsdlfjsldjflksdworld", "helloworld"))
    print(match("hellod", "hellowd"))
    print(match("hello*xxxxxxxxxxhemantxxxxxxxxxxxx", "hellnt"))
    print()

#main2()

"""
True
False
True
"""

def my_strdup(src):
    length = len(src)
    dst = [None] * length
    index = 0
    for ch in src:
        dst[index] = ch
        index += 1
    return dst

def is_prime(n):
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

# Testing code.
def main3():
    print("Prime numbers under 10 :: ", end = " ")
    for i in range(10):
        if (is_prime(i)):
            print(i, end = " ")
    print()

main3()

"""
Prime numbers under 10 :: 2 3 5 7 
"""

def my_atoi(text):
    value = 0
    size = len(text)
    for i in range(size):
        value = (value << 3) + (value << 1) + (ord(text[i]) - ord('0'))
    return value

# Testing code.
#print(my_atoi("100"))
"""
100
"""

def is_unique_char(text):
    charset = set()
    for ch in text:
        if(ch in charset):
            return False
        charset.add(ch)
    return True

# Testing code.
def main4():
    is_unique_char("aple")
    is_unique_char("apple")

main4()

"""
No duplicate detected!
Duplicate detected!
"""

def is_permutation(s1, s2):
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

# Testing code.
def main5():
    print("is_permutation :", is_permutation("apple", "plepa"))
    print("is_permutation :", is_permutation("appleb", "plepaa"))

main5()

"""
is_permutation : True
is_permutation : False
"""

def is_palindrome(text):
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

# Testing code.
def main6():
    is_palindrome("hello")
    is_palindrome("eoloe")

main6()

"""
String is not a Palindrome
String is a Palindrome
"""

def pow(x, n):
    value = int()
    if n == 0:
        return (1)
    elif n % 2 == 0:
        value = pow(x, n // 2)
        return (value * value)
    else:
        value = pow(x, n // 2)
        return (x * value * value)

# Testing code.
def main7():
    print(pow(5, 2))

main7()

"""
25
"""

def my_strcmp(a, b):
    len1 = len(a)
    len2 = len(b)
    minlen = min(len1, len2)

    index = 0
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


# Testing code.
def main8():
    print("StrCmp returns :", my_strcmp("aba", "aas"))

main8()

"""
StrCmp returns : 1
"""

def reverse_string(a):
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

def reverse_string_util(a, lower, upper):
    while lower < upper:
        tempChar = a[lower]
        a[lower] = a[upper]
        a[upper] = tempChar
        lower += 1
        upper -= 1

def reverse_words(a):
    a = list(a)
    length = len(a)
    upper = -1
    lower = 0
    for i in range(length+1):
        if i == length or a[i] == ' ':
            reverse_string_util(a, lower, upper)
            lower = i + 1
            upper = i
        else:
            upper += 1
    reverse_string_util(a, 0, length - 1)
    return "".join(a)

# Testing code.
def main9():
    print(reverse_string("apple"))
    print(reverse_words("hello world"))

main9()

"""
elppa
world hello
"""


def print_anagram(a):
    n = len(a)
    a = list(a)
    print_anagram_util(a, n, n)


def print_anagram_util(a, maxindex, n):
    if maxindex == 1:
        print("".join(a))
    i = -1
    for i in range(-1, maxindex - 1) :
        if i != -1:
            temp = a[i]
            a[i] = a[maxindex - 1] 
            a[maxindex - 1] = temp
        print_anagram_util(a, maxindex - 1, n)
        if i != -1:
            temp = a[i] 
            a[i] = a[maxindex - 1] 
            a[maxindex - 1] = temp

# Testing code.
def main10():
    print_anagram("123")

main10()

"""
123
213
321
231
132
312
"""

def shuffle(text):
    n = len(text) // 2
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
            temp, ar[k] = ar[k], temp
            count += 1
            if not ((i != k)):
                break
            
        if count == (2 * n - 2):
            break
        i = i + 2
    return "".join(ar)

# Testing code.
def main11():
    print(shuffle("ABCDE12345"))

main11()

"""
A1B2C3D4E5
"""

def add_binary(first, second):
    size1 = len(first)
    size2 = len(second)
    index = 0
    total = []
    if size1 > size2:
        total = [0] * (size1 + 1)
        index = size1
    else:
        total = [0] * (size2 + 1)
        index = size2
    carry = 0
    size1 -= 1
    size2 -= 1
    while size1 >= 0 or size2 >= 0:
        firstValue = 0
        secondValue = 0 
        if (size1 >= 0):
            firstValue = ord(first[size1]) - ord('0')
        if (size2 >= 0):
            secondValue = ord(second[size2]) - ord('0')
        sumvalue = firstValue + secondValue + carry
        carry = sumvalue >> 1
        sumvalue = sumvalue & 1
        if (sumvalue == 0):
            total[index] = '0'  
        else:
            total[index] ='1'
        index -= 1
        size1 -= 1
        size2 -= 1
    if (carry == 0):
        total[index] = '0'  
    else:
        total[index] = '1'
    return "".join(total)

# Testing code.
def main12():
    a = "101010"
    b = "111111"
    print(add_binary(a, b))

main12()

"""
1101001
"""