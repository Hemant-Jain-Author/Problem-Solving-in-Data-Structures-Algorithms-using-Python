import math
import sys

def linear_search_unsorted(arr, value):
    size = len(arr)
    for i in range(size):
        if value == arr[i]:
            return True
    return False

def linear_search_sorted(arr, value):
    size = len(arr)
    for i in range(size):
        if value == arr[i]:
            return True
        elif value < arr[i]:
            return False
    return False

    
#  Binary Search Algorithm - Iterative Way
def binary_search(arr, value):
    size = len(arr)
    low = 0
    high = size - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == value:
            return True
        elif arr[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return False


def binary_search_recursive(arr, value):
    return binary_search_recursive_util(arr, 0, len(arr) - 1, value)


#  Binary Search Algorithm - Recursive Way
def binary_search_recursive_util(arr, low, high, value):
    if low > high:
        return False
    mid = (low + high) // 2
    if arr[mid] == value:
        return True
    elif arr[mid] < value:
        return binary_search_recursive_util(arr, mid + 1, high, value)
    else:
        return binary_search_recursive_util(arr, low, mid - 1, value)

def fibonacciSearch(arr,  size,  value) :
    # Initialize fibonacci numbers 
    fibNMn2 = 0
    fibNMn1 = 1
    fibN = fibNMn2 + fibNMn1
    while (fibN < size) :
        fibNMn2 = fibNMn1
        fibNMn1 = fibN
        fibN = fibNMn2 + fibNMn1
    low = 0
    while (fibN > 1) :
        #  fibonacci series start with 0, 1, 1, 2
        i = min(low + fibNMn2,size - 1)
        if (arr[i] == value) :
            return  True
        elif (arr[i] < value) :
            fibN = fibNMn1
            fibNMn1 = fibNMn2
            fibNMn2 = fibN - fibNMn1
            low = i
        else :
            #  for feb2 <= 1, these will be invalid.
            fibN = fibNMn2
            fibNMn1 = fibNMn1 - fibNMn2
            fibNMn2 = fibN - fibNMn1
    if (arr[low + fibNMn2] == value) : #  above loop does not check when fibNMn2 = 0
        return  True
    return  False

def main1():
    first = [1, 3, 5, 7, 9, 25, 30]
    print(linear_search_unsorted(first, 8))
    print(linear_search_unsorted(first, 3))
    print(linear_search_sorted(first, 8))
    print(linear_search_sorted(first, 3))

    first = [1, 3, 5, 7, 9, 25, 30]
    print(binary_search_recursive(first, 3))
    print(binary_search(first, 3))

    for i in range(10):
        print(i, " : " + str(fibonacciSearch(first, 7, i)))    

main1()
"""
False
True
False
True
True
True
"""
"""
0  : False
1  : True
2  : False
3  : True
4  : False
5  : True
6  : False
7  : True
8  : False
9  : True
"""

def first_repeated(arr):
    size = len(arr)
    for i in range(size):
        for j in range(i+1, size):
            if arr[i] == arr[j]:
                return arr[i]
    return sys.maxsize  # can raise exception.

def first_repeated2(arr) :
    size = len(arr)
    hm =  dict()
    for i in range(size) :
        if ((arr[i] in hm.keys())) : 
            hm[arr[i]] = 2
        else :
            hm[arr[i]] = 1
    
    for i in range(size) :
        if (hm.get(arr[i]) == 2) :
            return  arr[i]
    return  0


def main2():
    arr = [34, 56, 77, 1, 5, 6, 6, 8, 10, 20, 30, 34 ]
    print(first_repeated(arr))
    print(first_repeated2(arr))


main2()
"""
34
34
"""

def print_repeating(arr):
    size = len(arr)
    print("Repeating elements are:: ", end='')
    for i in range(size):
        for j in range(i+1, size):
            if arr[i] == arr[j]:
                print(arr[i], end=' ')


def print_repeating2(arr):
    size = len(arr)
    arr.sort()
    print("Repeating elements are:: ", end='')
    for i in range(size):
        if arr[i] == arr[i - 1]:
            print(arr[i], end=' ')


def print_repeating3(arr):
    size = len(arr)
    hs = set()
    print("Repeating elements are:: ", end='')
    for i in range(size):
        if arr[i] in hs:
            print(arr[i], end=' ')
        else:
            hs.add(arr[i])


def print_repeating4(arr, valrange):
    size = len(arr)
    count = [0] * valrange
    print("Repeating elements are:: ", end='')
    for i in range(size):
        if count[arr[i]] == 1:
            print(arr[i], end=' ')
        else:
            count[arr[i]] = 1


def main3():
    first = [1, 3, 5, 3, 9, 1, 30]
    print_repeating(first)
    print_repeating2(first)
    print_repeating3(first)
    print_repeating4(first, 50)

main3()
"""
Repeating elements are :: 1 3  
Repeating elements are :: 1 3  
Repeating elements are :: 1 3  
Repeating elements are :: 1 3 
"""


def get_max(arr):
    size = len(arr)
    maxval = arr[0]
    count = 1
    max_count = 1
    for i in range(size):
        count = 1
        for j in range(i+1, size):
            if arr[i] == arr[j]:
                count += 1
        if count > max_count:
            maxval = arr[i]
            max_count = count
    return maxval


def get_max2(arr):
    size = len(arr)
    maximum = arr[0]
    max_count = 1
    curr = arr[0]
    curr_count = 1
    arr.sort()
    for i in range(size):
        if arr[i] == arr[i - 1]:
            curr_count += 1
        else:
            curr_count = 1
            curr = arr[i]
        if curr_count > max_count:
            max_count = curr_count
            maximum = curr
    return maximum


def get_max3(arr, value_range):
    size = len(arr)
    maximum = arr[0]
    max_count = 1
    count = [0] * value_range
    for i in range(size):
        count[arr[i]] += 1
        if count[arr[i]] > max_count:
            max_count = count[arr[i]]
            maximum = arr[i]
    return maximum


def main4():
    first = [1, 30, 5, 13, 9, 31, 5] 
    print(get_max(first))
    print(get_max2(first))
    print(get_max3(first, 50))

main4()
"""
5
5
5
"""

def get_majority(arr):
    size = len(arr)
    maximum = 0
    count = 0
    max_count = 0
    for i in range(size):
        for j in range(i+1, size):
            if arr[i] == arr[j]:
                count += 1
        if count > max_count:
            maximum = arr[i]
            max_count = count
    if max_count > size // 2:
        return maximum
    else:
        return sys.maxsize # can also raised exception.

def get_majority2(arr):
    size = len(arr)
    maj_index = size // 2
    arr.sort()
    candidate = arr[maj_index]
    count = 1
    for i in range(size):
        if arr[i] == candidate:
            count += 1
    if count > size // 2:
        return arr[maj_index]
    else:
        return sys.maxsize # can also raised exception.

def get_majority3(arr):
    size = len(arr)
    maj_index = 0
    count = 1
    for i in range(1, size):
        if arr[maj_index] == arr[i]:
            count += 1
        else:
            count -= 1
        if count == 0:
            maj_index = i
            count = 1
    candidate = arr[maj_index]
    count = 0

    for i in range(size):
        if arr[i] == candidate:
            count += 1
    
    if count > size // 2:
        return arr[maj_index]
    else:
        return sys.maxsize  # can also raised exception.


def main5():
    first = [1, 5, 5, 13, 5, 31, 5]
    print(get_majority(first))
    print(get_majority2(first))
    print(get_majority3(first))

main5()
"""
5
5
5
"""

def missing_values(arr) :
    size = len(arr)
    max = arr[0]
    min = arr[0]
    missing = []
    for i in range(1, size) :
        if (max < arr[i]) : 
            max = arr[i]
        if (min > arr[i]) : 
            min = arr[i]

    for i in range(min + 1, max) :
        found = False
        for j in range(size) :
            if (arr[j] == i) :
                found = True
                break
        if (not found) : 
            missing.append(i)
    return missing

def missing_values2(arr):
    size = len(arr)
    arr.sort()
    value = arr[0]
    missing = []
    i = 0
    while(i < size):
        if value == arr[i]:
            value += 1
            i += 1
        else:
            missing.append(value)
            value += 1
    return missing

def missing_values3(arr):
    size = len(arr)
    missing = []
    dict = {}
    minVal = sys.maxsize
    maxVal = -sys.maxsize

    for i in range(size):
        dict[arr[i]] = 1
        if minVal > arr[i]:
            minVal = arr[i]
        if maxVal < arr[i]:
            maxVal = arr[i]

    for i in range(minVal, maxVal+1):
        if i not in dict:
            missing.append(i)
    return missing

def main6():
    first = [11, 14, 13, 17, 21, 18, 19, 23, 24]
    print(missing_values(first))
    print(missing_values2(first))
    print(missing_values3(first))

        
main6()
"""
[12, 15, 16, 20, 22]
[12, 15, 16, 20, 22]
[12, 15, 16, 20, 22]
"""

def odd_count(arr) :
    size = len(arr)
    xorSum = 0
    for i in range(size) :
        xorSum ^= arr[i]
    print("Odd value: " + str(xorSum))

def odd_count2(arr):
    size = len(arr)
    hs = {}
    for i in range(size):
        if arr[i] in hs :
            hs[arr[i]] += 1
        else:
            hs[arr[i]] = 1

    print("Odd values:", end=' ')
    for key in hs:
        if hs[key] % 2 == 1:
            print(key, end=' ')


def odd_count3(arr):
    size = len(arr)
    # xor of all elements in arr[]
    # even occurrence will cancel each other.
    # sum will contain sum of two odd elements.
    
    xor_sum = 0
    for i in range(size):
        xor_sum = xor_sum ^ arr[i]
    
    # Rightmost set bit.
    set_bit = xor_sum & ~(xor_sum - 1)
    
    # Dividing elements in two group: 
    # Elements having set_bit bit as 1.
    # Elements having set_bit bit as 0.
    # Even elements cancelled themself if group and we get our numbers.
    first, second = 0, 0
    for i in range(size):
        if(arr[i] & set_bit):
            first = first ^ arr[i]
        else:
            second = second ^ arr[i] 

    print("Odd values:", first, second)
 
def main7():
    arr = [10, 25, 30, 10, 15, 25, 15]
    odd_count(arr)
    arr = [10, 25, 30, 10, 15, 25, 15, 40]
    odd_count2(arr)
    arr = [10, 25, 30, 10, 15, 25, 15, 40]
    odd_count3(arr)

main7()
"""
Odd value: 30
Odd values: 30 40 
Odd values: 30 40
"""

def sum_distinct(arr):
    size = len(arr)
    arr.sort()
    output = []
    sum = 0
    for i in range(size - 1):
        if arr[i] != arr[i+1]:
            output.append(arr[i])
            sum += arr[i]
    sum += arr[size - 1]
    print(sum)

def main8():
    arr = [1, 2, 3, 1, 1, 4, 5, 6]
    sum_distinct(arr)

main8()
"""
21
"""

def min_abs_sum_pair(arr):
    size = len(arr)
    if size < 2:
        print("Invalid Input")
        return
    min_first = 0
    min_second = 1
    min_sum = abs(arr[0] + arr[1])
    for i in range(size - 1):
        for j in range(i+1, size):
            currsum = abs(arr[i] + arr[j])
            if currsum < min_sum:
                min_sum = currsum
                min_first = i
                min_second = j
    print("The two elements with minimum sum are:", arr[min_first], "&", arr[min_second])


def min_abs_sum_pair2(arr):
    size = len(arr)
    if size < 2:
        print("Invalid Input")
        return
    arr.sort()
    min_first = 0
    min_second = size - 1
    min_sum = abs(arr[min_first] + arr[min_second])        
    l = 0
    r = size - 1
    while l < r:
        currsum = (arr[l] + arr[r])
        if abs(currsum) < min_sum:
            min_sum = currsum
            min_first = l
            min_second = r
        if currsum < 0:
            l += 1
        elif currsum > 0:
            r -= 1
        else:
            break
    print("The two elements with minimum sum are:", arr[min_first], "&" , arr[min_second])


def main9():
    first = [1, 5, -10, 3, 2, -6, 8, 9, 6] 
    min_abs_sum_pair2(first)
    min_abs_sum_pair(first)

main9()
"""
The two elements with minimum sum are : -6 & 6
The two elements with minimum sum are : -6 & 6
"""

def find_pair(arr, value):
    size = len(arr)
    for i in range(size):
        for j in range(i+1, size):
            if (arr[i] + arr[j]) == value:
                print("The pair is::", arr[i], "&" , arr[j])
                return True
    return False


def find_pair2(arr, value):
    size = len(arr)
    first = 0
    second = size - 1
    arr.sort()
    while first < second:
        curr = arr[first] + arr[second]
        if curr == value:
            print("The pair is::", arr[first], "&", arr[second])
            return True
        elif curr < value:
            first += 1
        else:
            second -= 1
    return False


def find_pair3(arr, value):
    size = len(arr)
    hs = set()
    for i in range(size):
        if (value - arr[i]) in hs:
            print("The pair is::", arr[i] , "&" , (value - arr[i]))
            return True
        hs.add(arr[i])
    return False

def find_pair4(arr,  size,  rangeval,  value) :
    count = [0] * (rangeval + 1)
    for i in range(size) :
        if (count[value - arr[i]] > 0) :
            print("The pair is :", arr[i] , "&" , ((value - arr[i])))
            return  True
        count[arr[i]] += 1
    return  False

def main10():
    first = [1, 5, 4, 3, 2, 7, 8, 9, 6]
    print(find_pair(first, 8))
    print(find_pair2(first, 8))
    print(find_pair3(first, 8))
    print(find_pair4(first, len(first), 9, 8))

main10()
"""
The pair is:: 1 & 7
True
The pair is:: 1 & 7
True
The pair is:: 5 & 3
True
The pair is : 5 & 3
True
"""

def find_pair_two_lists(arr1,  size1,  arr2,  size2,  value) :
    i = 0
    while (i < size1) :
        j = 0
        while (j < size2) :
            if ((arr1[i] + arr2[j]) == value) :
                print("The pair is:", arr1[i], "&", arr2[j])
                return  True
            j += 1
        i += 1
    return  False

def find_pair_two_lists2(arr1,  size1,  arr2,  size2,  value) :
    arr2.sort()
    i = 0
    while (i < size1) :
        if (binary_search(arr2, value - arr1[i])) : 
            print("The pair is:", arr1[i], "&", value - arr1[i])
            return  True
        i += 1
    return  False

def find_pair_two_lists3(arr1,  size1,  arr2,  size2,  value) :
    first = 0
    second = size2 - 1
    curr = 0
    arr1.sort()
    arr2.sort()
    while (first < size1 and second >= 0) :
        curr = arr1[first] + arr2[second]
        if (curr == value) :
            print("The pair is:", arr1[first], "&", arr2[second])
            return  True
        elif (curr < value) :
            first += 1
        else :
            second -= 1
    return  False

def find_pair_two_lists4(arr1,  size1,  arr2,  size2,  value) :
    hs =  set()
    i = 0
    while (i < size2) :
        hs.add(arr2[i])    
        i += 1
    i = 0
    while (i < size1) :
        if (value - arr1[i] in hs) :
            print("The pair is:", arr1[i], "&", (value - arr1[i]))
            return  True
        i += 1
    return  False

def find_pair_two_lists5(arr1,  size1,  arr2,  size2,  range,  value) :
    count = [0] * (range + 1)
    i = 0
    while (i < size2) :
        count[arr2[i]] = 1    
        i += 1
    i = 0
    while (i < size1) :
        if (count[value - arr1[i]] != 0) :
            print("The pair is:", arr1[i], "&",  value - arr1[i])
            return  True
        i += 1
    return  False

def main11() :
    first = [1, 5, 4, 3, 2, 7, 8, 9, 6]
    second = [1, 5, 4, 3, 2, 7, 8, 9, 6]
    print(find_pair_two_lists(first, len(first), second, len(second), 8))
    print(find_pair_two_lists2(first, len(first), second, len(second), 8))
    print(find_pair_two_lists3(first, len(first), second, len(second), 8))
    print(find_pair_two_lists4(first, len(first), second, len(second), 8))
    print(find_pair_two_lists5(first, len(first), second, len(second), 9, 8))

main11()
"""
The pair is: 1 & 7
True
The pair is: 1 & 7
True
The pair is: 1 & 7
True
The pair is: 1 & 7
True
The pair is: 1 & 7
True
"""

def find_difference(arr, value):
    size = len(arr)
    for i in range(size):
        for j in range(i+1, size):
            if abs(arr[i] - arr[j]) == value:
                print("The pair is:", arr[i], "&" , arr[j])
                return True
    return False


def find_difference2(arr, value):
    size = len(arr)
    first = 0
    second = 0
    arr.sort()
    while first < size and second < size:
        curr = abs(arr[first] - arr[second])
        if curr == value:
            print("The pair is:", arr[first], "&", arr[second])
            return True
        elif curr > value:
            first += 1
        else:
            second += 1
    return False

def main12():
    first = [1, 5, 4, 3, 2, 7, 8, 9, 6]
    print(find_difference(first, 6))
    print(find_difference2(first, 6))


main12()
"""
The pair is: 1 & 7
True
The pair is: 1 & 7
True
"""

def find_min_diff(arr) :
    size = len(arr)
    diff = sys.maxsize
    for i in range(size) :
        for j in range(i + 1, size) :
            value = abs(arr[i] - arr[j])
            if (diff > value) : 
                diff = value
    return  diff

def find_min_diff2(arr):
    size = len(arr)
    arr.sort()
    diff = sys.maxsize
    for i in range(size - 1):
        if arr[i+1] - arr[i] < diff:
            diff = arr[i+1] - arr[i]
    return diff
 
# Testing code.
def main13():
    arr = [1, 6, 4, 19, 17, 20]
    print(find_min_diff(arr))
    print(find_min_diff2(arr))


main13()
"""
1
1
"""

def min_diff_pair(arr1,  size1,  arr2,  size2) :
    diff = sys.maxsize
    first = 0
    second = 0
    for i in range(size1) :
        for j in range(size2) :
            value = abs(arr1[i] - arr2[j])
            if (diff > value) :
                diff = value
                first = arr1[i]
                second = arr2[j]
    print("The pair is :: " + str(first) + " & " + str(second))
    print("Minimum difference is :: " + str(diff))
    return  diff

def min_diff_pair2(arr1,  size1,  arr2,  size2) :
    minDiff = sys.maxsize
    i, j, first, second = 0, 0, 0, 0
    arr1.sort()
    arr2.sort()
    while (i < size1 and j < size2) :
        diff = abs(arr1[i] - arr2[j])
        if (minDiff > diff) :
            minDiff = diff
            first = arr1[i]
            second = arr2[j]
        if (arr1[i] < arr2[j]) : 
            i += 1
        else :
            j += 1
    print("The pair is :: " + str(first) + " & " + str(second))
    print("Minimum difference is :: " + str(minDiff))
    return  minDiff

def main14() :
    first = [1, 5, 4, 3, 2, 7, 8, 9, 6]
    second = [6, 4, 19, 17, 20]
    min_diff_pair(first, len(first), second, len(second))
    min_diff_pair2(first, len(first), second, len(second))

main14()

"""
The pair is :: 4 & 4
Minimum difference is :: 0
The pair is :: 4 & 4
Minimum difference is :: 0
"""

def closest_pair(arr, value):
    size = len(arr)
    diff = sys.maxsize
    first, second = -1, -1
    for i in range(size):
        for j in range(i+1, size):
            curr = abs(value - (arr[i] + arr[j]))
            if curr < diff:
                diff = curr
                first = arr[i]
                second = arr[j]
    print("Closest pair is::", first, "&",  second)

def closest_pair2(arr, value):
    size = len(arr)
    first, second = 0, 0
    start, stop = 0, size - 1
    arr.sort()
    diff = sys.maxsize
    while start < stop:
        curr = (value - (arr[start] + arr[stop]))
        if abs(curr) < diff:
                diff = abs(curr)
                first = arr[start]
                second = arr[stop]
        if curr == 0:
            break 
        elif curr > 0:
            start += 1
        else:
            stop -= 1
    print("Closest pair is::", first, "&", second)

def main15():
    first = [10, 20, 3, 4, 50, 80]
    closest_pair(first, 47)
    closest_pair2(first, 47)

main15()

"""
Closest pair is:: 3 & 50
Closest pair is:: 3 & 50
"""


def sum_pair_rest_array(arr):
    size = len(arr)
    arr.sort()
    total = 0
    for i in range(size):
        total += arr[i]

    value = total // 2
    low, high = 0, size - 1

    while low < high:
        curr = arr[low] + arr[high]
        if curr == value:
            print(arr[low] , arr[high])
            return True
        elif curr < value:
            low += 1
        else :
            high -= 1
    return False

# Testing Code
def main16():
    arr = [1, 2, 4, 8, 16, 15]
    print(sum_pair_rest_array(arr))

main16()

"""
8 15
True
"""


def zero_sum_triplets(arr):
    size = len(arr) 
    for i in range(size-2):
        for j in range(i+1, size-1): 
            for k in range(j + 1, size):
                if arr[i] + arr[j] + arr[k] == 0:
                    print(arr[i], arr[j], arr[k])

def zero_sum_triplets2(arr):
    size = len(arr)
    arr.sort()
    for i in range(size-2):
        start = i+1
        stop = size-1

        while start < stop:
            if arr[i] + arr[start] + arr[stop] == 0:
                print(arr[i], arr[start], arr[stop])
                start += 1
                stop -= 1
            elif arr[i] + arr[start] + arr[stop] > 0:
                stop -= 1
            else:
                start += 1

def main17():
    arr = [0, -1, 2, -3, 1]
    zero_sum_triplets(arr)
    zero_sum_triplets2(arr)

main17()
"""
0 -1 1
2 -3 1
-3 1 2
-1 0 1
"""

def min_abs_diff_adj_circular(arr):
    size = len(arr)
    diff = sys.maxsize
    if (size < 2):
        return -1
    
    for i in range(size):
        diff = min(diff, abs(arr[i] - arr[(i + 1)%size]))
    return diff

# Testing code.
def main18():
    arr = [5, 29, 18, 51, 11]
    print(min_abs_diff_adj_circular(arr))

main18()
"""
6
"""

def search_bitonic_array_max(arr):
    size = len(arr)
    start = 0
    end = size - 1
    mid = (start + end) // 2
    maxima_found = 0
    if size < 3:
        print("error")
        return 0
    while start <= end:
        mid = (start + end) // 2
        if arr[mid - 1] < arr[mid] and arr[mid + 1] < arr[mid]:
            maxima_found = 1
            break
        elif arr[mid - 1] < arr[mid] and arr[mid] < arr[mid + 1]:
            start = mid + 1
        elif arr[mid - 1] > arr[mid] and arr[mid] > arr[mid + 1]:
            end = mid - 1
        else:
            break
    if maxima_found == 0:
        print("error")
        return sys.maxsize
    return arr[mid]

def find_max_bitonic_index(arr, size):
    start = 0
    end = size - 1
    if size < 3:
        print("error")
        return -1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid - 1] < arr[mid] and arr[mid + 1] < arr[mid]:
            return mid
        elif arr[mid - 1] < arr[mid] and arr[mid] < arr[mid + 1]:
            start = mid + 1
        elif arr[mid - 1] > arr[mid] and arr[mid] > arr[mid + 1]:
            end = mid - 1
        else:
            break
    print("error")
    return -1

def binary_search2(arr, start, end, key, isInc):
    if end < start:
        return False
    mid = (start + end) // 2
    if key == arr[mid]:
        return True
    if isInc != False and key < arr[mid] or isInc == False and key > arr[mid]:
        return binary_search2(arr, start, mid - 1, key, isInc)
    else:
        return binary_search2(arr, mid + 1, end, key, isInc)


def search_bitonic_array(arr, key):
    size = len(arr)
    maxval = find_max_bitonic_index(arr, size)
    k = binary_search2(arr, 0, maxval, key, True)
    if k == True:
        return True
    else:
        return binary_search2(arr, maxval + 1, size - 1, key, False)

def main19():
    first = [1, 5, 10, 13, 20, 30, 8, 7, 6] 
    print(search_bitonic_array_max(first))
    print(search_bitonic_array(first, 8))
    
main19()
"""
30
True
"""

def find_key_count(arr, key):
    size = len(arr)
    count = 0
    for i in range(size):
        if arr[i] == key:
            count += 1
    return count

def find_first_index(arr, start, end, key):
    if end < start:
        return -1
    mid = (start + end) // 2
    if key == arr[mid] and (mid == start or arr[mid - 1] != key):
        return mid
    if key <= arr[mid]:
        return find_first_index(arr, start, mid - 1, key)
    else:
        return find_first_index(arr, mid + 1, end, key)

def find_last_index(arr, start, end, key):
    if end < start:
        return -1
    mid = (start + end) // 2
    if key == arr[mid] and (mid == end or arr[mid + 1] != key):
        return mid
    if key < arr[mid]:
        return find_last_index(arr, start, mid - 1, key)
    else:
        return find_last_index(arr, mid + 1, end, key)

def find_key_count2(arr, key):
    size = len(arr)
    first_index = find_first_index(arr, 0, size - 1, key)
    last_index = find_last_index(arr, 0, size - 1, key)
    return (last_index - first_index + 1)

def main21():
    first = [1, 5, 10, 13, 20, 30, 8, 7, 6]
    print(find_key_count(first, 6))

    first = [1, 5, 6, 6, 6, 6, 6, 6, 7, 8, 10, 13, 20, 30 ]
    print(find_key_count2(first, 6))

main21()
"""
1
6
"""

def swap(arr, first, second):
    arr[first], arr[second] = arr[second], arr[first]

def separate_even_and_odd(arr):
    size = len(arr)
    left = 0
    right = size - 1
    while left < right:
        if arr[left] % 2 == 0:
            left += 1
        elif arr[right] % 2 == 1:
            right -= 1
        else:
            swap(arr, left, right)
            left += 1
            right -= 1
    return arr


def main22():
    first = [1, 5, 6, 6, 6, 6, 6, 6, 7, 8, 10, 13, 20, 30 ]
    print(separate_even_and_odd(first))

main22()
"""
[30, 20, 6, 6, 6, 6, 6, 6, 10, 8, 7, 13, 5, 1]
"""

def max_profit(stocks):
    size = len(stocks)
    buy, sell, cur_min, cur_profit, max_profit = 0, 0, 0, 0, 0
    for i in range(size):
        if stocks[i] < stocks[cur_min]:
            cur_min = i
        cur_profit = stocks[i] - stocks[cur_min]
        if cur_profit > max_profit:
            buy = cur_min
            sell = i
            max_profit = cur_profit
    print("Purchased at day", buy , "@" , stocks[buy])
    print("Sell at day", sell , "@" , stocks[sell])
    return stocks[sell] - stocks[buy]

def main23():
    first = [10, 150, 6, 67, 61, 16, 86, 6, 67, 78, 150, 3, 28, 143 ]
    print("Profit:", max_profit(first))

main23()
"""
Purchased at day 2 @ 6
Sell at day 10 @ 150
Profit: 144
"""

def get_median(arr):
    size = len(arr)
    arr.sort()
    return arr[size // 2]

def find_median(first, second):
    size_first = len(first)
    size_second = len(second)
    median_index = (size_first + size_second)//2
    i ,j, count = 0, 0, 0
    while count < median_index - 1:
        if i < size_first - 1 and first[i] < second[j]:
            i += 1
        else:
            j += 1
        count += 1
    if first[i] < second[j]:
        return first[i]
    else:
        return second[j]


def main24():
    first = [1, 5, 6, 6, 6, 6, 6, 6, 7, 8, 10, 13, 20, 30 ]
    second = [1, 5, 6, 6, 6, 6, 6, 6, 7, 8, 10, 13, 20, 30 ]
    print(get_median(first))
    print(find_median(first, second))

main24()
"""
6
6
"""

def min(a, b):
    return b if a > b else a

def max(a, b):
    return b if a < b else a

def binary_search01(arr):
    size = len(arr)
    if size == 1 and arr[0] == '1':
        return 0
    return binary_search01_util(arr, 0, size - 1)

def binary_search01_util(arr, start, end):
    if end < start:
        return -1
    mid = (start + end) // 2
    
    if '1' == arr[mid] and '0' == arr[mid - 1]:
        return mid
    if '0' == arr[mid]:
        return binary_search01_util(arr, mid + 1, end)
    else:
        return binary_search01_util(arr, start, mid - 1)

def main25():
    first = "000000001111"
    print(binary_search01(first))

main25()
"""
8
"""

def binary_search_rotate_array(arr, key):
    size = len(arr)
    return binary_search_rotate_array_util(arr, 0, size - 1, key)

def binary_search_rotate_array_util(arr, start, end, key):
    if end < start:
        return False
    mid = (start + end) // 2
    
    if key == arr[mid]:
        return True
    if arr[mid] > arr[start]:
        if arr[start] <= key and key < arr[mid]:
            return binary_search_rotate_array_util(arr, start, mid - 1, key)
        else:
            return binary_search_rotate_array_util(arr, mid + 1, end, key)
    else:
        if arr[mid] < key and key <= arr[end]:
            return binary_search_rotate_array_util(arr, mid + 1, end, key)
        else:
            return binary_search_rotate_array_util(arr, start, mid - 1, key)

def main26():
    first = [34, 56, 77, 1, 5, 6, 8, 10, 13, 20, 30 ]
    print(binary_search_rotate_array(first, 20))

main26()
"""
True
"""

def find_rotation_max(arr):
    size = len(arr)
    return find_rotation_max_util(arr, 0, size - 1)

def find_rotation_max_util(arr, start, end):
    # single element case.
    if end <= start:
        return start

    mid = (start + end) // 2
    if arr[mid] > arr[mid+1]:
        return mid

    if arr[start] <= arr[mid]: #increasing part.
        return find_rotation_max_util(arr, mid+1, end)
    else:
        return find_rotation_max_util(arr, start, mid-1)

def main27():
    arr = [34, 56, 77, 1, 5, 6, 6, 8, 10, 20, 30, 34 ]
    print(find_rotation_max(arr))

main27()
"""
2
"""

def count_rotation(arr):
    size = len(arr)
    maxIndex = find_rotation_max_util(arr, 0, size - 1)
    rotations = (maxIndex + 1) % size
    return rotations

def main28():
    arr = [34, 56, 77, 1, 5, 6, 6, 8, 10, 20, 30, 34 ]
    print(count_rotation(arr))

main28()
"""
3
"""


def transform_array_AB1(strval):
    arr = list(strval)
    size = len(arr)
    #N = math.floor(size // 2)
    N = (size // 2)
    i = 1
    for i in range(1, N):
        for j in range(i):
            swap(arr, N - i + 2 * j, N - i + 2 * j + 1)
    return "".join(arr)

def main29():
    print(transform_array_AB1("aaaabbbb"))

main29()
"""
abababab
"""

def check_permutation(str1, str2):
    array1 = list(str1)
    array2 = list(str2)
    size1 = len(array1)
    size2 = len(array2)
    if size1 != size2:
        return False
    array1.sort()
    array2.sort()
    for i in range(size1):
        if array1[i] != array2[i]:
            return False
    return True

def check_permutation2(str1, str2):
    size1 = len(str1)
    size2 = len(str2)
    if size1 != size2:
        return False
    al = []
    for i in range(size1):
        al.append(str1[i])

    for i in range(size2):
        if al.count(str2[i]) == 0:
            return False
        al.remove(str2[i])
    return True

def main30():
    print(check_permutation("aaaabbbb", "bbaaaabb"))
    print(check_permutation2("aaaabbbb", "bbaaaabb"))

main30()
"""
True
True
"""

def remove_duplicates(array):
    size = len(array)
    if size == 0:
        return 0
    array.sort()
    j = 0
    for i in range(size):
        if array[i] != array[j]:
            j += 1
            array[j] = array[i]
    array[j:size - 1] = []
    return array

def remove_duplicates2(arr) :
    size = len(arr)
    hm =  dict()
    j = 0
    i = 0
    while (i < size) :
        if (not (arr[i] in hm.keys())) :
            arr[j] = arr[i]
            j += 1
            hm[arr[i]] = 1
        i += 1
    ret = arr[:j]
    return  ret

def main31():
    first = [1, 7, 6, 4, 8, 3, 8, 2, 6, 9]
    print(remove_duplicates(first))
    print(remove_duplicates2(first))

main31()
"""
[1, 2, 3, 4, 6, 7, 8, 9]
[1, 2, 3, 4, 6, 7, 8, 9]
"""

def find_missing_number(arr, upper_range):
    size = len(arr)
    for i in range(1, upper_range):
        found = 0
        for j in range(size):
            if arr[j] == i:
                found = 1
                break
        if found == 0:
            return i
    return sys.maxsize

def find_missing_number2(arr) :
    size = len(arr)
    arr.sort()
    for i in range(size) :
        if (arr[i] != i + 1) :
            return  i + 1
    return  size

def find_missing_number3(arr) :
    size = len(arr)
    hm =  dict()
    for i in range(size) :
        hm[arr[i]] = 1    

    for i in range(1, size+1) :
        if (not (i in hm.keys())) :
                return  i    

    return  sys.maxsize

def find_missing_number4(arr) :
    size = len(arr)
    count = [-1] * (size + 1)
    for i in range(size) :
        count[arr[i] - 1] = 1    
    for i in range(size+1) :
        if (count[i] == -1) :
            return  i + 1    
    return  sys.maxsize

def find_missing_number5(arr) :
    size = len(arr)
    sum = 0
    #  Element value range is from 1 to size+1.
    for i in range(1, (size + 2)) :
        sum += i    
    for i in range(size) :
        sum -= arr[i]    
    return  sum

def find_missing_number6(arr) :
    size = len(arr)
    for i in range(size) :
        arr[arr[i] % (size) - 1] += size + 1    

    for i in range(size) :
        if (arr[i] < size + 1) :
            return  i + 1    

    return  sys.maxsize

def find_missing_number7(arr, upper_range):
    size = len(arr)
    i = 1
    xor_sum = 0
    for i in range(1, upper_range+1):
        xor_sum ^= i

    for i in range(size):
        xor_sum ^= arr[i]

    return xor_sum


def find_missing_number8(arr, upper_range):
    size = len(arr)
    mset = set()
    for i in range(size) :
        mset.add(arr[i])

    for i in range(1, upper_range+1):
        if (i in mset) == False:
            return i
    return sys.maxsize


def main32():
    first = [1, 5, 4, 3, 2, 7, 8, 9, 10]
    print(find_missing_number(first, 10))
    print(find_missing_number2(first))
    print(find_missing_number3(first))
    print(find_missing_number4(first))
    print(find_missing_number5(first))
    print(find_missing_number7(first, 10))
    print(find_missing_number8(first, 10))
    print(find_missing_number6(first)) # Changes the input


main32()
"""
6
6
6
6
6
6
6
6
"""

def find_element_in_2dArray(arr, r, c, value):
    row = 0
    column = c - 1
    while row < r and column >= 0:
        if arr[row][column] == value:
            return True
        elif arr[row][column] > value:
            column -= 1
        else:
            row += 1
    return False


def pair_minimum_sum(arr):
    size = len(arr)
    start = 0
    stop = size -1
    minimum = sys.maxsize
    maximum = -sys.maxsize
    arr.sort()
    print("Pairs are:",end=" ")
    while start < stop:
        minimum = min(minimum, arr[stop] + arr[start])
        maximum = max(maximum, arr[stop] + arr[start])
        start += 1
        stop -= 1
        print("(",arr[start] , arr[stop], ")", end=" ")
    print("Maximum:", maximum, "Minimum:", minimum)
    return maximum - minimum

def main33():
    arr = [1, 4, 3, 2]
    print(pair_minimum_sum(arr))

main33()
"""
Pairs are: ( 2 3 ) ( 3 2 ) Maximum: 5 Minimum: 5
0
"""

def is_ap(arr):
    size = len(arr)
    if (size <= 1): 
        return True

    arr.sort()
    diff = arr[1] - arr[0]
    for i in range(2, size):
        if (arr[i] - arr[i-1] != diff):
            return False
    return True

def is_ap2(arr):
    size = len(arr)
    first = sys.maxsize
    second = sys.maxsize
    hs = {}
    for i in range(size):
        if arr[i] < first:
            second = first
            first = arr[i]
        elif arr[i] < second:
            second = arr[i]
        
    diff = second - first

    for i in range(size):
        if arr[i] in hs:
            return False
        hs[arr[i]] = 1
    
    for i in range(size):
        value = first + i * diff
        if value not in hs or hs[value] != 1:
            return False
    return True

def is_ap3(arr):
    size = len(arr)
    first = sys.maxsize
    second = sys.maxsize
    count = [0]*size
    for i in range(size):
        if arr[i] < first:
            second = first
            first = arr[i]
        elif arr[i] < second:
            second = arr[i]
    
    diff = second - first

    for i in range(size):
        index = (arr[i] - first )// diff
        if index > size - 1 or count[index] != 0:
            return False
        count[index] = 1
    
    for i in range(size):
        if count[i] != 1:
            return False
    return True

def main34():
    arr = [ 20, 25, 15, 5, 0, 10, 35, 30 ]
    print(is_ap(arr))
    arr = [ 20, 25, 15, 5, 0, 10, 35, 30 ]
    print(is_ap2(arr))
    arr = [ 20, 25, 15, 5, 0, 10, 35, 30 ]
    print(is_ap3(arr))

main34()
"""
True
True
True
"""

def ap_triplets(arr):
    size = len(arr)
    for i in range(1, size - 1): 
        j = i - 1
        k = i + 1
        while j >= 0 and k < size : 
            # triplet found
            if arr[j] + arr[k] == 2 * arr[i]:
                print(arr[j], arr[i], arr[k])
                k += 1
                j -= 1
            elif arr[j] + arr[k] < 2 * arr[i]:
                k += 1
            else:
                j -= 1          

def main35():
    arr = [ 2, 4, 10, 12, 14, 18, 36]
    ap_triplets(arr)

main35()
"""
2 10 18
10 12 14
10 14 18
"""

def gp_triplets(arr):
    size = len(arr)
    for i in range(1, size - 1):
        j = i - 1
        k = i + 1
        while j >= 0 and k < size :
            # triplet found
            if arr[j] * arr[k] == arr[i] * arr[i]:
                print(arr[j], arr[i], arr[k])
                k += 1
                j -= 1
            elif arr[j] + arr[k] < 2 * arr[i]:
                k += 1
            else:
                j -= 1
          
def main36():
    arr = [ 1, 2, 4, 8, 16 ]
    gp_triplets(arr)

main36()
"""
1 2 4
2 4 8
1 4 16
4 8 16
"""

def number_of_triangles(arr):
    size = len(arr)
    count = 0

    for i in range(0,size - 2):
        for j in range(i+1, size - 1):
            for k in range(j+1, size):
                if arr[i] + arr[j] > arr[k] and arr[i] + arr[k] > arr[j] and arr[k] + arr[j] > arr[i]:
                    count += 1
    return count

def number_of_triangles2(arr):
    size = len(arr)
    arr.sort()
    count = 0

    for i in range(0,size - 2):
        k = i + 2
        for j in range(i+1, size - 1):
            # if sum of arr[i] & arr[j] is greater arr[k] 
            # then sum of arr[i] & arr[j+1] is also greater than arr[k]
            # this improvement make algo O(n2)
            while k < size and arr[i] + arr[j] > arr[k]:
                k += 1

            count += k - j - 1
    return count

def main37():
    arr = [1, 2, 3, 4, 5]
    print(number_of_triangles(arr))
    print(number_of_triangles2(arr))

main37()
"""
3
3
"""


def find_balanced_point(arr):
    size = len(arr)
    first = 0
    second = 0
    for i in range(1, size):
        second += arr[i]
    
    for i in range(size):
        if first == second :
            print(i, end=' ')
        if i < size - 1:
            first += arr[i]
            second -= arr[i+1]

def main38(): 
    arr = [-7, 1, 5, 2, -4, 3, 0]
    find_balanced_point(arr)

main38()
"""
3 6
"""

def find_floor(arr, value):
    size = len(arr)
    start = 0
    stop = size -1
    while start <= stop:
        mid = (start + stop)//2
        # search value is equal to arr[mid] value..
        # search value is grater then mid index value and less then mid+1 index value.
        # value is grater then arr[size-1] then floor is arr[size-1]
        if arr[mid] == value or ( arr[mid] < value and (mid == size-1 or arr[mid + 1] > value)):
            return arr[mid]
        elif arr[mid] < value:
            start = mid+1
        else:
            stop = mid-1
    return -1

def find_ceil(arr, value):
    size = len(arr)
    start = 0
    stop = size -1
    
    while start <= stop:
        mid = (start + stop)//2
        # search value is equal to arr[mid] value..
        # search value is less then mid index value and grater then mid-1 index value.
        # value is less then arr[0] then ceil is arr[0]
        if arr[mid] == value or ( arr[mid] > value and (mid == 0 or arr[mid - 1] < value)):
            return arr[mid]
        elif arr[mid] < value:
            start = mid+1
        else:
            stop = mid-1
    return -1

def main39():
    arr = [2, 4, 8, 16]
    for i in range(2,6):
        print(i , find_ceil(arr, i), find_floor(arr, i))

main39()
"""
2 2 2
3 4 2
4 4 4
5 8 4

"""

def closest_number(arr, num):
    size = len(arr)
    start = 0
    stop = size - 1
    output = -1
    min_dist = 9999
    while start <= stop:
        mid = (start + stop )//2
        if min_dist > abs(arr[mid] - num):
            min_dist = abs(arr[mid] - num)
            output = arr[mid]
        
        if arr[mid] == num:
            break
        elif arr[mid] > num:
            stop = mid - 1
        else:
            start = mid + 1
    return output

def main39():
    arr = [2, 5, 8, 8, 9]
    for i in range(6):
        print(i, "is closest to:", closest_number(arr, i))

main39()
"""
0 is closest to: 2
1 is closest to: 2
2 is closest to: 2
3 is closest to: 2
4 is closest to: 5
5 is closest to: 5

"""

def duplicate_Kdistance(arr, k):
    size = len(arr)
    hs = {}
    for i in range(size):
        if arr[i] in hs and i - hs[arr[i]] <= k:
            print(arr[i], "appear in index", hs[arr[i]], "&",  i, end=' ')
            return True
        else :
            hs[arr[i]] = i
    return False

def main40():
    arr = [1, 2, 3, 1, 4, 5]
    duplicate_Kdistance(arr, 3)

main40()
"""
1 appear in index 0 & 3
"""

def find_triplet(arr, value):
    size = len(arr) 
    for i in range(size-2):
        for j in range(i+1, size-1): 
            for k in range(j + 1, size):
                if arr[i] + arr[j] + arr[k] == value:
                    print(arr[i], arr[j], arr[k])

def find_triplet2(arr, value):
    size = len(arr)
    arr.sort()
    for i in range(size-2):
        start = i+1
        stop = size-1

        while start < stop:
            if arr[i] + arr[start] + arr[stop] == value:
                print(arr[i], arr[start], arr[stop])
                start += 1
                stop -= 1
            elif arr[i] + arr[start] + arr[stop] > value:
                stop -= 1
            else:
                start += 1

def main41():
    arr = [1, 5, 15, 6, 9, 8]
    find_triplet(arr, 22)
    find_triplet2(arr, 22)

main41()
"""
1 15 6
5 9 8
1 6 15
5 8 9
"""

def abc_triplet(arr):
    size = len(arr)
    arr.sort()
    for i in range(size):
        start = 0
        stop = size-1
        while start < stop:
            if arr[i] == arr[start] + arr[stop]:
                print(arr[i], arr[start], arr[stop])
                start += 1
                stop -= 1
            elif arr[i] < arr[start] + arr[stop]:
                stop -= 1
            else:
                start += 1

def main42():
    arr = [1, 5, 15, 6, 9, 8]
    abc_triplet(arr)

main42()
"""
6 1 5
9 1 8
15 6 9
"""

def smaller_then_triplet_count(arr, value):
    size = len(arr)
    arr.sort()
    count = 0
    for i in range(size-2):
        start = i+1
        stop = size - 1
        while start < stop:
            if arr[i] + arr[start] + arr[stop] >= value:
                stop -= 1
            else:
                count += stop - start 
                start += 1
    print(count)
        
def main43():
    arr = [-2, -1,  0, 1]
    smaller_then_triplet_count(arr, 2)

main43()
"""
4
"""


def frequency_counts(arr):
    size = len(arr)
    for i in range(size):
        while arr[i] > 0:
            index = arr[i] - 1
            if arr[index] > 0:
                arr[i] = arr[index]
                arr[index] = -1
            else:
                arr[index] -= 1
                arr[i] = 0
 
    for i in range(size):
        print(i+1, " : ", abs(arr[i]))
    print("")

def main44(): 
    arr1 = [1, 2, 2, 2, 1]
    frequency_counts(arr1)

main44()
"""
1  :  2
2  :  3
3  :  0
4  :  0
5  :  0
"""

def klargest_elements(arrIn, k):
    size = len(arrIn)
    arr = list(arrIn)
    arr.sort()
    for i in range(size):
        if arrIn[i] >= arr[size - k]:
            print(arrIn[i], end=' ')


def quick_select_util(arr, lower, upper, k):
    if upper <= lower:
        return
    pivot = arr[lower]
    start = lower
    stop = upper
    while lower < upper:
        while arr[lower] <= pivot and lower < upper:
            lower += 1
        while arr[upper] > pivot and lower <= upper:
            upper -= 1
        if lower < upper:
            arr[upper], arr[lower] = arr[lower], arr[upper]
    arr[upper], arr[start] = arr[start], arr[upper]    # upper is the pivot position
    
    if k < upper: 
        quick_select_util(arr, start, upper - 1, k)
    
    if k > upper:
        quick_select_util(arr, upper + 1, stop, k)   
          
def klargest_elements2(arrIn, k):
    size = len(arrIn)
    arr = list(arrIn)
    quick_select_util(arr, 0, size-1, size - k)
    for i in range(size):
        if arrIn[i] >= arr[size - k]:
            print(arrIn[i], end=' ')

def main45():
    arr = [10, 50, 30, 60, 15]
    klargest_elements(arr, 2)
    print("")
    klargest_elements2(arr, 2)


main45()
"""
50 60 
50 60 
"""

def ksmallest_elements(arrIn, k):
    size = len(arrIn)
    arr = list(arrIn)
    arr.sort()
    for i in range(size):
        if arrIn[i] <= arr[k-1]:
            print(arrIn[i], end=' ')

def ksmallest_elements2(arrIn, k):
    size = len(arrIn)
    arr = list(arrIn)
    quick_select_util(arr, 0, size-1, k)
    for i in range(size):
        if arrIn[i] <= arr[k-1]:
            print(arrIn[i], end=' ')

def main46():
    arr = [4, 2, 6, 1, 5]
    ksmallest_elements(arr, 3)
    print("")
    ksmallest_elements2(arr, 3)
    print("")
    arr = [ 1, 5, 8, 9, 6, 7, 3, 4, 2, 0]
    ksmallest_elements(arr, 5)
    print("")
    ksmallest_elements2(arr, 5)
    print("")

main46()
"""
4 2 1 
4 2 1 
1 3 4 2 0 
1 3 4 2 0 
"""

def is_majority(arr):
    size = len(arr)
    majority = arr[size//2]
    i = first_index(arr, 0, size - 1, majority)
    # we are using majority element form array so 
    # we will get some valid index always.

    if ((i + size//2) <= (size - 1)) and arr[i + size//2] == majority:
        return True
    else:
        return False

# Using binary search method. 
def first_index(arr, low, high, value):
    if high >= low:
        mid = (low + high)//2 

        """ 
        Find first occurrence of value, either it should be the first element of the array or 
        the value before it is smaller then it.
        """ 
        if (mid == 0 or arr[mid-1] < value ) and (arr[mid] == value):
            return mid
        elif arr[mid] < value:
            return first_index(arr, mid + 1, high, value)
        else:
            return first_index(arr, low, mid -1, value)
    return -1

def main47():
    arr = [3, 3, 3, 3, 4, 5, 10]
    if (is_majority(arr)):
        print("Majority found::", arr[len(arr)//2])
    else:
        print ("Majority not found")

main47()
"""
Majority found:: 3
"""

def max_con_sub(A):
    sizeA = len(A)
    curr_max = 0
    maximum =0
    for i in range(sizeA):
        curr_max = max(A[i], curr_max+A[i])
        if curr_max < 0:
            curr_max = 0
        if maximum < curr_max:
            maximum = curr_max
    print(maximum)


def max_con_sub_arr(A, B):
    sizeA = len(A)
    sizeB = len(B)
    hs = {}
    for i in range(sizeB):
        hs[B[i]] = 1
    
    curr_max = 0
    maximum =0
    for i in range(sizeA):
        if A[i] in hs:
            curr_max = 0
        else :
            curr_max = max(A[i], curr_max+A[i])
            if curr_max < 0:
                curr_max = 0
            if maximum < curr_max:
                maximum = curr_max
    print(maximum)

def binary_search(arr, value):
    size = len(arr)
    start = 0 
    stop = size - 1
    while start <= stop:
        mid = (start + stop)//2
        if value == arr[mid]:
            return True
        elif value > arr[mid]:
            start = mid+1
        else:
            stop = mid-1
    return False

def max_con_sub_arr2(A,  B) :
    sizeA = len(A)
    sizeB = len(B)
    B.sort()
    currMax = 0
    maximum = 0
    i = 0
    while (i < sizeA) :
        if (binary_search(B, A[i])) : 
            currMax = 0
        else :
            currMax = currMax + A[i]
            if (currMax < 0) : currMax = 0
            if (maximum < currMax) : maximum = currMax
        i += 1
    print(maximum)
    return  maximum

def main48() :
    arr = [1, 2, -3, 4, 5, -10, 6, 7]
    max_con_sub(arr)
    arr2 = [1, 2, 3, 4, 5, -10, 6, 7, 3]
    arr3 = [1, 3]
    max_con_sub_arr(arr2, arr3)
    max_con_sub_arr2(arr2, arr3)

main48()
"""
13
13
13
"""

def repeated_missing(arr):
    size = len(arr)
    # xor of all elements in arr[]
    # even occurrence will cancel each other.
    # sum will contain sum of two odd elements.
    
    xor_sum = 0
    for i in range(size):
        xor_sum = xor_sum ^ (i+1)
        xor_sum = xor_sum ^ arr[i]
    
    # Rightmost set bit.
    set_bit = xor_sum & ~(xor_sum - 1)
    
    # Dividing elements in two group: 
    # Elements having set_bit bit as 1.
    # Elements having set_bit bit as 0.
    # Even elements cancelled themself if group and we get our numbers.
    first, second = 0, 0
    for i in range(size):
        if(arr[i] & set_bit):
            first = first ^ arr[i]
        else:
            second = second ^ arr[i]

        if((i+1) & set_bit):
            first = first ^ (i+1)
        else:
            second = second ^ (i+1) 
    found = False
    for i in range(size):
        if(first == arr[i]):
            found = True
            break

    if found == True:
        print("Repeated element::", first)
        print("Missing element::", second)
    else:
        print("Repeated element ::", second)
        print("Missing element ::", first)

def main50():    
    arr = [1, 3, 6, 5, 4, 1]
    repeated_missing(arr)

main50()
"""
Repeated element:: 1
Missing element:: 2
"""

def sorted_insert(arr, value):
    arr.append(value)
    size = len(arr)
    while size > 0:
        if arr[size - 1] >= arr[size - 2]:
            break
        arr[size -1], arr[size - 2] = arr[size - 2], arr[size - 1] 
        size -= 1

def main51():
    arr = [1, 9, 2, 8, 3, 7, 4, 6, 5]
    arr.sort()
    print(binary_search(arr, 4))
    print(binary_search(arr, 10))
    sorted_insert(arr, 11)
    sorted_insert(arr, 7)
    print(arr)

main51()
"""
True
False
[1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 11]
"""

#linear search method
def fix_point(arr):
    size = len(arr)
    for i in range(size):
        if arr[i] == i:
            return i
    # fix point not found so return invalid index
    return -1

# Binary search method
def fix_point2(arr):
    size = len(arr)
    low = 0
    high = size - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == mid:
            return mid
        elif arr[mid] < mid:
            low = mid + 1
        else:
            high = mid - 1
    # fix point not found so return invalid index
    return -1

def main52():
    arr = [-10, -2, 0, 3, 11, 12, 35, 51, 200]
    print(fix_point(arr))
    print(fix_point2(arr))

main52()
"""
3
3
"""

def find_maxima(arr):
    size = len(arr)
    for i in range(size):
        if ((i == 0) or arr[i-1] < arr[i]) and ((i == size -1 ) or arr[i] > arr[i+1]):
            print(arr[i], end=' ')
    print("")


def main53():
    arr = [10, 20, 30, 40, 50]
    find_maxima(arr)
    arr = [50, 40, 30, 20, 10]
    find_maxima(arr)
    arr = [10, 30, 20, 1, 25, 90, 60]
    find_maxima(arr)
    arr = [10, 20, 40, 30]
    find_maxima(arr)

main53()
"""
50 
50 
30 90 
40 
"""

def sub_array_sums(arr, value):
    size = len(arr)
    first = 0
    second = 0
    sum = arr[first]
    while second < size and first < size:
        if sum == value:
            print(first , second)

        if sum < value:
            second += 1
            if second < size :
                sum += arr[second]
        else :
            sum -= arr[first]
            first += 1

def sub_array_sum(arr, value):
    size = len(arr)
    first = 0
    second = 0
    sum = arr[first]
    while second < size and first < size:
        if sum == value:
            print(first , second)
            return True
        if sum < value:
            second += 1
            if second < size :
                sum += arr[second]
        else :
            sum -= arr[first]
            first += 1
    return False

def main54():
    arr = [15, 5, 5, 20, 10, 5, 5, 20, 10, 10]
    sub_array_sum(arr, 20)
    sub_array_sums(arr, 20)

main54()
"""
0 1

0 1
3 3
4 6
7 7
8 9
"""

def rain_water(arr):
    size = len(arr)
    left_high = [0]*size
    left_high[0] = max = arr[0]
    for i in range(1,size):
        if max < arr[i]:
            max = arr[i]
        left_high[i] = max
    
    right_high = [0]*size
    right_high[size - 1] = max = arr[size - 1]
    for i in reversed(list(range(size-1))):
        if max < arr[i]:
            max = arr[i]
        right_high[i] = max
    water = 0
    for i in range(size):
        water += min(left_high[i], right_high[i]) - arr[i]
    print(water)


def rain_water2(arr):
    size = len(arr)
    water = 0
    left_max, right_max = 0, 0
    left = 0
    right = size-1
      
    while(left <= right): 
        if(arr[left] < arr[right]):
            if(arr[left] > left_max):
                left_max = arr[left]
            else:
                water += left_max - arr[left]
            left += 1
        else:
            if(arr[right] > right_max):
                right_max = arr[right]
            else:
                water += right_max - arr[right]
            right -= 1
    print(water)

def main55():
    arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    rain_water(arr)
    rain_water2(arr)

main55()
"""
6
6
"""