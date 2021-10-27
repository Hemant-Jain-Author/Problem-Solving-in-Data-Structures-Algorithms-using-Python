import sys
import math

def partition01(arr):
    size = len(arr)
    left = 0
    right = size - 1
    while left < right:
        while arr[left] == 0 :
            left += 1
        while arr[right] == 1 :
            right -= 1
        if left < right :
            arr[left] = 0
            arr[right] = 1

def partition012(arr):
    size = len(arr)
    left = 0
    right = size - 1
    i = 0
    while i <= right:
        if arr[i] == 0 :
            arr[i], arr[left] = arr[left], arr[i]
            i += 1
            left += 1
        elif arr[i] == 2 :
            arr[i], arr[right] = arr[right], arr[i]
            right -= 1
        else :
            i += 1

def partition012_(self, arr,  size) :
    zero = 0
    one = 0
    two = 0
    i = 0
    while (i < size) :
        if (arr[i] == 0) :
            zero += 1
        elif (arr[i] == 1) :
            one += 1
        else :
            two += 1
        i += 1
    index = 0
    while (zero > 0) :
        arr[index] = 0
        index += 1
        zero -= 1
    while (one > 0) :
        arr[index] = 1
        index += 1
        one -= 1
    while (two > 0) :
        arr[index] = 2
        index += 1
        two -= 1


def test1():
    arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
    partition012(arr)
    print(arr)

    arr = [0, 1, 0, 1, 1, 1]
    partition01(arr)
    print(arr)

"""
[0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]
[0, 0, 1, 1, 1, 1]
"""

def abs_cmp(value1, value2, ref):
    return abs(value1 - ref) > abs(value2 - ref)

def abs_sort(arr, ref):
    size = len(arr)
    for i in range(size - 1):
        for j in range(size - i - 1):
            if abs_cmp(arr[j], arr[j + 1], ref):
                #  Swapping
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def test2():
    array = [9, 1, 8, 2, 7, 3, 6, 4, 5]
    ref = 5
    abs_sort(array, ref)
    print(array)

"""
[5, 6, 4, 7, 3, 8, 2, 9, 1]
"""

def eq_cmp(value1, value2, A):
    value1 = A*value1*value1
    value2 = A*value2*value2
    return value1 > value2

def equation_sort(arr, A):
    size = len(arr)
    for i in range(size - 1):
        for j in range(size - i - 1):
            if eq_cmp(arr[j], arr[j + 1], A):
                #  Swapping
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
 
def test3():
    array = [-1, 0, 1, 2, 3, 4]
    A = 1
    equation_sort(array, A)
    print(array)

"""
[0, -1, 1, 2, 3, 4]
"""

def swap(arr, left, right):
    arr[left], arr[right] = arr[right], arr[left]

def separate_even_odd(arr):
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

def test4():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    separate_even_odd(array)
    print(array)

"""
[8, 2, 6, 4, 5, 3, 7, 1, 9]
"""

def array_reduction(arr) :
    size = len(arr)
    arr.sort()
    count = 1
    reduction = arr[0]

    for i in range(size) :
        if (arr[i] - reduction > 0) :
            print((size - i), end=' ')
            reduction = arr[i]
            count += 1

    print("Total number of reductions", count, end=' ')

def test5():
    arr = [ 5, 1, 1, 1, 2, 3, 5 ]
    array_reduction(arr)

"""
Total number of reductions 4 
"""

def sort_frequency(arr):
    mp = {}
    size = len(arr)
    for i in range(size):
        if arr[i] in mp:
            mp[arr[i]] += 1
        else:
            mp[arr[i]] = 1
    
    """ 
    User is recommended to write his own sorting function.
    for convinenance author is using inbuilt functions. 
    """
    for key, value in reversed(sorted(iter(mp.items()), key = lambda k_v: (k_v[1], k_v[0]))):
        for i in range(value):
            print(key, end=' ')

def test6():
    arr = [2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12]
    sort_frequency(arr)

"""
3 3 3 3 2 2 2 12 12 5 4 
"""

def Sort_by_order(arr, arr2):
    mp = {}
    size = len(arr)
    for i in range(size):
        if arr[i] in mp:
            mp[arr[i]] += 1
        else:
            mp[arr[i]] = 1
    
    for key in arr2:
        if key in mp:
            for i in range(mp[key]):
                print(key, end=' ')
            del mp[key]

    for key in mp:
        for i in range(mp[key]):
            print(key, end=' ')


def test7():
    print("")
    arr = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8]
    arr2 = [2, 1, 8, 3]
    Sort_by_order(arr, arr2)

"""
2 2 1 1 8 8 3 5 7 9 6
"""

def merge(arr1, arr2):
    size1 = len(arr1)
    size2 = len(arr2)
    first = 0
    while first < size1:
        if arr1[first] <= arr2[0]:
            first += 1
        else:
            # always first element of arr2 is compared.
            arr1[first], arr2[0] = arr2[0], arr1[first]
            first += 1
            # After swap arr2 may be unsorted.
            # Insertion of Oth element in proper sorted position.
            for i in range(size2 - 1):
                if arr2[i] < arr2[i+1]:
                    break
                arr2[i], arr2[i+1] = arr2[i+1], arr2[i]

# Testing code.
def test8():
    arr1 = [1, 5, 9, 10, 15, 20]
    arr2 = [2, 3, 8, 13]
    merge(arr1, arr2)
    print(arr1, arr2)

"""
[1, 2, 3, 5, 8, 9] [10, 13, 15, 20]
"""

def min_abs_pair_differences(arr):
    size = len(arr)
    minimum = sys.maxsize
    for i in range(size):
        for j in range(i+1, size):
            minimum = min(abs(arr[i] - arr[j]), minimum)
    return minimum 

def min_abs_pair_differences2(arr):
    size = len(arr)
    arr.sort()
    minimum = min(abs(arr[0] - arr[1]), abs(arr[size-2] - arr[size-1]))
    for i in range(1, size - 1):
        temp = min(abs(arr[i] - arr[i - 1]), abs(arr[i] - arr[i + 1]))
        minimum = min(temp, minimum)
    return minimum 

# Driver code
def test9():
    arr = [5, 101, 11, 14, 18, 71]
    print(min_abs_pair_differences(arr))
    print(min_abs_pair_differences2(arr))

"""
3
3
"""

def min_abs_sum(arr):
    size = len(arr)
    arr.sort()
    minSum = sys.maxsize
    low = 0
    high = size - 1

    while low < high:
        sum = arr[low] + arr[high]
        absSum = abs(sum)
        if absSum < minSum:
            minSum = absSum
        if sum < 0:
            low += 1
        else :
            high -= 1
    return minSum

def test10():
    arr = [1, 60, -10, 70, -80, 85]
    print(min_abs_sum(arr))

"""
5
"""

def find_min_diff(arr):
    size = len(arr)
    arr.sort()
    diff = sys.maxsize
 
    for i in range(size - 1):
        if arr[i+1] - arr[i] < diff:
            diff = arr[i+1] - arr[i]

    return diff
 
def test11():
    arr = [1, 6, 4, 19, 17, 20]
    print(find_min_diff(arr))

"""
1
"""

def min_diff_pair(arr1, arr2):
    size1 = len(arr1)
    size2 = len(arr2)
    minDiff = sys.maxsize
    arr1.sort()
    arr2.sort()
    first = 0
    second = 0
    output = [0, 0]
    while first < size1 and second < size2:
        diff = abs(arr1[first] - arr2[second])
        if minDiff > diff:
            minDiff = diff
            output[0] = arr1[first]
            output[1] = arr2[second]
        if arr1[first] < arr2[second]:
            first += 1
        else:
            second += 1
    print(output)
    print(minDiff)
    return minDiff

def test12():
    arr1 = [1, 4, 12, 10, 2]
    arr2 = [20, 128, 2354, 18, 7]
    min_diff_pair(arr1, arr2)

"""
[4, 7]
3
"""

def min_swaps(arr):
    size = len(arr)
    start = 0
    end = size -1
    count = 0
    while start < end:
        if arr[start] == 0:
            start += 1
        elif arr[end] == 1:
            end -= 1
        else:
            arr[start], arr[end] = arr[end], arr[start]
            count += 1
    return count

def test13():
    arr = [0, 1, 0, 1, 0]
    print(min_swaps(arr))

"""
1
"""

def missing_values(arr):
    size = len(arr)
    arr.sort()
    value = arr[0]
    missing = []
    i = 0
    while i < size:
        if value == arr[i]:
            value += 1
            i += 1
        else:
            missing.append(value)
            value += 1
    print(missing)


def missing_values2(arr):
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
    print(missing)

def test14():
    arr = [4, 5, 3, 8, 6,10]
    missing_values(arr)
    missing_values2(arr)

"""
[7, 9]
[7, 9]
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
            # if sum of arr[i] & arr[j] is grater arr[k] 
            # then sum of arr[i] & arr[j+1] is also grater then arr[k]
            # this improvement make algo O(n2)
            while k < size and arr[i] + arr[j] > arr[k]:
                k += 1
            count += k - j - 1
    return count

def test15():
    arr = [1, 2, 6, 4, 5, 3, 7, 8]
    print(number_of_triangles(arr))
    print(number_of_triangles2(arr))

"""
22
22
"""

def range_partition(arr, lower, higher):
    size = len(arr)
    left = 0
    right = size - 1
    i = 0
    while i <= right:
        if arr[i] < lower :
            arr[i], arr[left] = arr[left], arr[i]
            i += 1
            left += 1
        elif arr[i] > higher :
            arr[i], arr[right] = arr[right], arr[i]
            right -= 1
        else :
            i += 1

def test16():
    arr = [1,21,2,20,3,19,4,18,5,17,6,16,7,15,8,14,9,13,10,12,11]
    range_partition(arr, 8, 12)
    print(arr)

"""
[1, 2, 3, 4, 5, 6, 7, 9, 11, 8, 10, 12, 15, 16, 14, 17, 13, 18, 19, 20, 21]
"""

def sort_AB(A, B):
    size = len(A)
    for i in range(size-1):
        for j in range(size-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                if B[j] == 0:
                    return False
    return True

def test17():
    A = [1, 2, 4, 3, 6, 5]
    B = [0, 0, 1, 1, 1]
    print(sort_AB(A, B))

    A = [5, 3, 1, 4, 2, 6]
    B = [0, 1, 1, 1, 1]
    print(sort_AB(A, B))

"""
True
False
"""

def sub_array_zero_sum(arr):
    size = len(arr)
    max_length = -1
    start, stop = -1, -1
    hs = {}
    hs[0] = -1
    sum = 0
    for i in range(size):
        sum += arr[i]
        if sum in hs:
            curr_length = i - hs[sum]
            if curr_length > max_length :
                max_length = curr_length
                start = hs[sum]
                stop = i
        else :
            hs[sum] = i
    print(start+1, stop, max_length)

def test18():
    arr = [4, 1, 1, -5, 1, 3, 0, -2, 6]
    sub_array_zero_sum(arr)

"""
2 6 5
"""

def sub_array_zero_one_equal(arr):
    size = len(arr)
    max_length = -1
    start, stop = -1, -1
    hs = {}
    hs[0] = -1
    sum = 0
    for i in range(size):
        if arr[i] == 1:
            sum += 1
        else :
            sum -= 1
        
        if sum in hs:
            curr_length = i - hs[sum]
            if curr_length > max_length :
                max_length = curr_length
                start = hs[sum]
                stop = i
        else :
            hs[sum] = i
    print(start+1, stop, max_length)

def test19():
    arr = [0, 0, 0, 1, 0, 1, 0]
    sub_array_zero_one_equal(arr)

"""
2 5 4
"""

def sum_pair_rest_array(arr):
    size = len(arr)
    arr.sort()
    total = 0
    for i in range(size):
        total += arr[i]
    value = total / 2
    low = 0
    high = size - 1
    while low < high:
        curr = arr[low] + arr[high]
        if curr == value:
            print(arr[low] , arr[high], end=' ')
            return True
        elif curr < value:
            low += 1
        else :
            high -= 1
    return False
    
def test20():
    arr = [1, 2, 4, 8, 16, 15]
    print(sum_pair_rest_array(arr))

"""
8 15 True
"""

def check_reverse(arr):
    size = len(arr)
    start = -1
    stop = -1
    for i in range(size-1):
        if arr[i] > arr[i+1] :
            start = i
            break

    if start == -1:
        return True
 
    for i in range(start, size-1):
        if arr[i] < arr[i+1]:
            stop = i
            break

    if stop == -1:
        return True

    #increasing property
    # after reversal the sub array should fit in the array.
    if arr[start - 1] > arr[stop] or arr[stop + 1] < arr[start]:
        return False
 
    for i in range(stop+1, size-1):
        if arr[i] > arr[i+1]:
            return False

    return True

def test21():
    arr =[1,2,3,6,5,4,7,8,9]
    print(check_reverse(arr))
    arr =[1,2,3,6,5,4]
    print(check_reverse(arr))
    arr =[1,2,3,7,5,4,6,8,9]
    print(check_reverse(arr))
    arr =[1,2,3,4,5,6,7]
    print(check_reverse(arr))
    arr =[7,6,5,4,3,2,1]
    print(check_reverse(arr))

"""
True
True
False
True
True
"""

def union_intersection_sorted(arr1, arr2):
    size1 = len(arr1)
    size2 = len(arr2)
    first, second = 0, 0
    union = []
    inter = []
    while first < size1 and second < size2 :
        if arr1[first] == arr2[second]:
            union.append(arr1[first])
            inter.append(arr1[first])
            first += 1
            second += 1
        elif arr1[first] < arr2[second]:
            union.append(arr1[first])
            first += 1
        else:
            union.append(arr2[second])
            second += 1

    while first < size1 :
        union.append(arr1[first])
        first += 1
        
    while second < size2 :
        union.append(arr2[second])
        second += 1
    print(union)
    print(inter)

def test22():
    arr1 = [1, 2, 3, 5, 6, 8, 9]
    arr2 = [2, 4, 5, 7, 8, 10]
    union_intersection_sorted(arr1, arr2)

"""
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[2, 5, 8]
"""

def union_intersection_unsorted(arr1, arr2):
    arr1.sort()
    arr2.sort()
    union_intersection_sorted(arr1, arr2)

def test23():
    arr1 = [1, 11, 2, 3, 14, 5, 6, 8, 9]
    arr2 = [2, 4, 5, 12, 7, 8, 13, 10]
    union_intersection_unsorted(arr1, arr2)

"""
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
[2, 5, 8]
"""

def print_unique(arr):
    size = len(arr)
    print(" Unique elements are ::", end=' ')
    for i in range(size):
        for j in range(i+1):
            if arr[i] == arr[j]:
                break
        if j == i:
            print(arr[i], end=' ')

def print_unique2(arr):
    size = len(arr)
    arr.sort()
    print(" Unique elements are ::", end=' ')
    for i in range(size):
        if arr[i] != arr[i - 1]:
            print(arr[i], end=' ')

def print_unique3(arr):
    size = len(arr)
    hs = set()
    print(" Unique elements are ::", end=' ') 
    for i in range(size):
        if arr[i] not in hs:
            hs.add(arr[i])
            print(arr[i], end=' ')

def print_unique4(arr, valrange):
    size = len(arr)
    count = [0] * valrange
    print(" Unique elements are ::", end=' ')
    for i in range(size):
        if count[arr[i]] == 0:
            print(arr[i], end=' ')
        count[arr[i]] += 1

def test24():
    first = [1, 3, 5, 3, 9, 1, 30]
    print_unique(first)
    print("")
    print_unique2(first)
    print("")
    print_unique3(first)
    print("")
    print_unique4(first, 50)


"""
 Unique elements are :: 1 3 5 9 30 
 Unique elements are :: 1 3 5 9 30 
 Unique elements are :: 1 3 5 9 30 
 Unique elements are :: 1 3 5 9 30 
"""

test1()
test2()
test3()
test4()
test5()
test6()
test7()
test8()
test9()
test10()
test11()
test12()
test13()
test14()
test15()
test16()
test17()
test18()
test19()
test20()
test21()
test22()
test23()
test24()