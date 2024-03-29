from collections import Counter

def is_anagram(str1, str2):
    size1 = len(str1)
    size2 = len(str2)
    if size1 != size2:
        return False
    cm = Counter()
    for ch in str1:
        cm[ch] += 1
    for ch in str2:
        if cm[ch] == 0:
            return False
        else:
            cm[ch] -= 1
    return True

# Testing Code
first = "hello"
second = "elloh"
third = "world"
print("is_anagram : " , is_anagram(first, second))
print("is_anagram : " , is_anagram(first, third))

"""
is_anagram :  True
is_anagram :  False
"""

def remove_duplicate(exp):
    hs = set()
    return_exp = ""
    for ch in exp:
        if (ch in hs) == False:
            return_exp += ch
            hs.add(ch)
    return return_exp

# Testing Code
first = "hello"
print(remove_duplicate(first))

"""
helo
"""

def find_missing(arr, start, end):
    hs = set()
    for i in arr:
        hs.add(i)
    for curr in range(start, end+1):
        if (curr in hs) == False:
            return curr
    return sys.maxsize

# Testing Code
arr = [1, 2, 3, 5, 6, 7, 8, 9, 10]
print("Missing number :", find_missing(arr, 1, 10))

"""
Missing number : 4
"""

def print_repeating(arr):
    hs = set()
    print("Repeating elements are:", end=' ')
    for val in arr:
        if val in hs:
            print(val, end=' ')
        else:
            hs.add(val)

# Testing Code
arr = [1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 1]
print_repeating(arr)

"""
Repeating elements are: 4 1 
"""

def print_first_repeating(arr):
    size = len(arr)
    hs = Counter()
    for i in range(size):
        hs[arr[i]] += 1
    
    for i in range(size):
        if hs.get(arr[i]) > 1:
            print("First Repeating number is :" , arr[i])
            return arr[i]

# Testing Code
arr = [1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 1]
print_first_repeating(arr)

"""
First Repeating number is : 1
"""

def horner_hash(self, key, tableSize):
    size = len(key)
    h = 0
    for i in range(size):
        h = (32 * h + key[i]) % tableSize
    return h