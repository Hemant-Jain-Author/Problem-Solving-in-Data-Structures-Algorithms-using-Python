   
def brute_force_search(text, pattern):
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
   
def robinkarp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    prime = 101
    powm = 1
    text_hash = 0
    pattern_hash = 0
    if m == 0 or m > n:
        return -1
    i = 0
    while i < m - 1:
        powm = (powm << 1) % prime
        i += 1
    i = 0
    while i < m:
        pattern_hash = ((pattern_hash << 1) + ord(pattern[i])) % prime
        text_hash = ((text_hash << 1) + ord(text[i])) % prime
        i += 1
    i = 0
    while i <= (n - m):
        if text_hash == pattern_hash:
            j = 0
            while j < m:
                if text[i + j] != pattern[j]:
                    break
                j += 1
            if j == m:
                return i
        text_hash = (((text_hash - ord(text[i]) * powm) << 1) + ord(text[i + m])) % prime
        if text_hash < 0:
            text_hash = (text_hash + prime)
        i += 1
    return -1

def kmp_preprocess(pattern, shift_arr):
    m = len(pattern)
    i = 0
    j = -1
    shift_arr[i] = -1
    while i < m:
        while j >= 0 and pattern[i] != pattern[j]:
            j = shift_arr[j]
        i += 1
        j += 1
        shift_arr[i] = j

def kmp_search(text, pattern):
    i = 0
    j = 0
    n = len(text)
    m = len(pattern)
    shift_arr = [0] * (m + 1)
    kmp_preprocess(pattern, shift_arr)
    while i < n:
        while j >= 0 and text[i] != pattern[j]:
            j = shift_arr[j]
        i += 1
        j += 1
        if j == m:
            return (i - m)
    return -1

def kmp_find_count(text, pattern):
    i = 0
    j = 0
    count = 0
    n = len(text)
    m = len(pattern)
    shift_arr = [0] * (m + 1)
    kmp_preprocess(pattern, shift_arr)
    while i < n:
        while j >= 0 and text[i] != pattern[j]:
            j = shift_arr[j]
        i += 1
        j += 1
        if j == m:
            count += 1
            j = shift_arr[j]
    return count

# Testing code.
st1 = "hello, world!"
st2 = "world"
print("brute_force_search return :", brute_force_search(st1, st2))
print("robinkarp return :", robinkarp_search(st1, st2))
print("kmp return:" , kmp_search(st1, st2))
str3 = "Only time will tell if we stand the test of time"
print("Frequency of 'time' is ", kmp_find_count(str3, "time"))

"""
brute_force_search return : 7
robinkarp return : 7
kmp return : 7
Frequency of 'time' is  2
"""