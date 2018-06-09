#!/usr/bin/env python
import math
import sys

def linearSearchUnsorted(arr, size, value):
    for i in range(size):
        if value == arr[i]:
            return True
    return False


def linearSearchSorted(arr, size, value):
    for i in range(size):
        if value == arr[i]:
            return True
        elif value < arr[i]:
            return False
    return False

def main1():
    first = [1, 3, 5, 7, 9, 25, 30]
    print(linearSearchSorted(first, 7, 8))

    
#  Binary Search Algorithm - Iterative Way
def Binarysearch(arr, size, value):
    low = 0
    high = size - 1
    while low <= high:
        mid = (low + high) / 2
        if arr[mid] == value:
            return True
        elif arr[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return False


def BinarySearchRecursive(arr, value):
    return BinarySearchRecursiveUtil(arr, 0, len(arr) - 1, value)


#  Binary Search Algorithm - Recursive Way
def BinarySearchRecursiveUtil(arr, low, high, value):
    if low > high:
        return False
    # mid = math.floor((low + high) / 2)
    mid = ((low + high) / 2)
    if arr[mid] == value:
        return True
    elif arr[mid] < value:
        return BinarySearchRecursiveUtil(arr, mid + 1, high, value)
    else:
        return BinarySearchRecursiveUtil(arr, low, mid - 1, value)


def main2():
    first = [1, 3, 5, 7, 9, 25, 30]
    print(BinarySearchRecursive(first, 3))  


def printRepeating(arr):
    size = len(arr)
    print(" Repeating elements :: ")#, end=' ')
    for i in range(size):
        for j in range(i+1, size):
            if arr[i] == arr[j]:
                print(arr[i])#, end=' ')


def printRepeating2(arr):
    size = len(arr)
    arr.sort()
    print(" Repeating elements are :: ")#, end=' ')
    for i in range(size):
        if arr[i] == arr[i - 1]:
            print(arr[i])#, end=' ')


def printRepeating3(arr):
    size = len(arr)
    hs = set()
    print(" Repeating elements are ::")#, end=' ')
    for i in range(size):
        if arr[i] in hs:
            print(arr[i])#, end=' ')
        else:
            hs.add(arr[i])


def printRepeating4(arr, valrange):
    size = len(arr)
    count = [0] * valrange
    print(" Repeating elements are :: ")#, end=' ')
    for i in range(size):
        if count[arr[i]] == 1:
            print(arr[i])#, end=' ')
        else:
            count[arr[i]] += 1


def main3():
    first = [1, 3, 5, 3, 9, 1, 30]
    printRepeating(first)
    printRepeating2(first)
    printRepeating3(first)
    printRepeating4(first, 50)


def getMax(arr):
    size = len(arr)
    maxval = arr[0]
    count = 1
    maxCount = 1
    for i in range(size):
        count = 1
        for j in range(i+1, size):
            if arr[i] == arr[j]:
                count += 1
        if count > maxCount:
            maxval = arr[i]
            maxCount = count
    return maxval


def getMax2(arr):
    size = len(arr)
    maximum = arr[0]
    maxCount = 1
    curr = arr[0]
    currCount = 1
    arr.sort()
    for i in range(size):
        if arr[i] == arr[i - 1]:
            currCount += 1
        else:
            currCount = 1
            curr = arr[i]
        if currCount > maxCount:
            maxCount = currCount
            maximum = curr
    return maximum


def getMax3(arr, valuerange):
    size = len(arr)
    maximum = arr[0]
    maxCount = 1
    count = [0] * valuerange
    for i in range(size):
        count[arr[i]] += 1
        if count[arr[i]] > maxCount:
            maxCount = count[arr[i]]
            maximum = arr[i]
    return maximum


def main4():
    first = [1, 30, 5, 13, 9, 31, 5] 
    print(getMax(first))
    print(getMax2(first))
    print(getMax3(first, 50))

"""
majority in an unsorted array is this problem , if array is sorted then majority candidate will be at 
n/2 index.
"""
def getMajority(arr):
    size = len(arr)
    maximum = 0
    count = 0
    maxCount = 0
    for i in range(size):
        for j in range(i+1, size):
            if arr[i] == arr[j]:
                count += 1
        if count > maxCount:
            maximum = arr[i]
            maxCount = count
    if maxCount > size / 2:
        return maximum
    else:
        return sys.maxint # can also raised exception.


def getMajority2(arr):
    size = len(arr)
    #majIndex = math.floor(size / 2)
    majIndex = (size / 2)
    arr.sort()
    candidate = arr[majIndex]
    count = 1
    for i in range(size):
        if arr[i] == candidate:
            count += 1
    if count > size / 2:
        return arr[majIndex]
    else:
        return sys.maxint # can also raised exception.


def getMajority3(arr):
    size = len(arr)
    majIndex = 0
    count = 1
    for i in range(1, size):
        if arr[majIndex] == arr[i]:
            count += 1
        else:
            count -= 1
        if count == 0:
            majIndex = i
            count = 1
    candidate = arr[majIndex]
    count = 0

    for i in range(size):
        if arr[i] == candidate:
            count += 1
    
    if count > size / 2:
        return arr[majIndex]
    else:
        return sys.maxint  # can also raised exception.


def main5():
    first = [1, 5, 5, 13, 5, 31, 5]
    print(getMajority(first))
    print(getMajority2(first))
    print(getMajority3(first))

        
def findMissingNumber(arr, upperRange):
    size = len(arr)
    i = 1
    found = 0
    while i <= upperRange:
        found = 0
        j = 0
        while j < size:
            if arr[j] == i:
                found = 1
                break
            j += 1
        if found == 0:
            return i
        i += 1
    return sys.maxint


def findMissingNumber2(arr, upperRange):
    size = len(arr)
    i = 1
    xorSum = 0
    while i <= upperRange:
        xorSum ^= i
        i += 1
    i = 0
    while i < size:
        xorSum ^= arr[i]
        i += 1
    return xorSum


def findMissingNumber3(arr, upperRange):
    size = len(arr)
    mSet = set()
    i = 0
    while i < size:
        mSet.add(arr[i])
        i += 1
    i = 1
    while i <= upperRange:
        if (i in mSet) == False:
            return i
        i += 1
    return sys.maxint


def main6():
    first = [1, 5, 4, 3, 2, 7, 8, 9, 10]
    # print(findMissingNumber(first, 9))
    print(findMissingNumber3(first, 9))
        

def FindPair(arr, value):
    size = len(arr)
    for i in range(size):
        for j in range(i+1, size):
            if (arr[i] + arr[j]) == value:
                print("The pair is::", arr[i], "&" , arr[j])
                return True
    return False


def FindPair2(arr, value):
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


def FindPair3(arr, value):
    size = len(arr)
    hs = set()
    for i in range(size):
        if (value - arr[i]) in hs:
            print("The pair is::", arr[i] , "&" , (value - arr[i]))
            return True
        hs.add(arr[i])
    return False


def main7():
    first = [1, 5, 4, 3, 2, 7, 8, 9, 6]
    print(FindPair(first, 8))
    print(FindPair2(first, 8))
    print(FindPair3(first, 8))


def minabsSumPair(arr):
    size = len(arr)
    if size < 2:
        print("Invalid Input")
        return
    minFirst = 0
    minSecond = 1
    minSum = abs(arr[0] + arr[1])
    for i in range(size - 1):
        for j in range(i+1, size):
            currsum = abs(arr[i] + arr[j])
            if currsum < minSum:
                minSum = currsum
                minFirst = i
                minSecond = j
    print(" The two elements with minimum sum are : ", arr[minFirst], "&", arr[minSecond])


def minabsSumPair2(arr):
    size = len(arr)
    if size < 2:
        print("Invalid Input")
        return
    arr.sort()
    minFirst = 0
    minSecond = size - 1
    minSum = abs(arr[minFirst] + arr[minSecond])        
    l = 0
    r = size - 1
    while l < r:
        currsum = (arr[l] + arr[r])
        if abs(currsum) < minSum:
            minSum = currsum
            minFirst = l
            minSecond = r
        if currsum < 0:
            l += 1
        elif currsum > 0:
            r -= 1
        else:
            break
    print(" The two elements with minimum sum are : ", arr[minFirst], "&" , arr[minSecond])


def main8():
    first = [1, 5, -10, 3, 2, -6, 8, 9, 6] 
    print(minabsSumPair2(first))
    print(minabsSumPair(first))
    # print(minabsSumPair(first))


def SearchBotinicArrayMax(arr):
    size = len(arr)
    start = 0
    end = size - 1
    mid = (start + end) / 2
    maximaFound = 0
    if size < 3:
        print("error")
        return 0
    while start <= end:
        #mid = math.floor((start + end) / 2)
        mid = ((start + end) / 2)
        if arr[mid - 1] < arr[mid] and arr[mid + 1] < arr[mid]:
            maximaFound = 1
            break
        elif arr[mid - 1] < arr[mid] and arr[mid] < arr[mid + 1]:
            start = mid + 1
        elif arr[mid - 1] > arr[mid] and arr[mid] > arr[mid + 1]:
            end = mid - 1
        else:
            break
    if maximaFound == 0:
        print("error")
        return sys.maxint
    return arr[mid]


def SearchBitonicArray(arr, key):
    size = len(arr)
    maxval = FindMaxBitonicIndex(arr, size)
    k = BinarySearch(arr, 0, maxval, key, True)
    if k == True:
        return True
    else:
        return BinarySearch(arr, maxval + 1, size - 1, key, False)


def FindMaxBitonicIndex(arr, size):
    start = 0
    end = size - 1
    if size < 3:
        print("error")
        return -1
    while start <= end:
        #mid = math.floor((start + end) / 2)
        mid = ((start + end) / 2)
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

def main9():
    first = [1, 5, 10, 13, 20, 30, 8, 7, 6]
    
    print(SearchBotinicArrayMax(first))
    print(SearchBitonicArray(first, 32))
    # print(minabsSumPair(first))
    
def BinarySearch(arr, start, end, key, isInc):
    if end < start:
        return False
    #mid = math.floor((start + end) / 2)
    mid = ((start + end) / 2)
    if key == arr[mid]:
        return True
    if isInc != False and key < arr[mid] or isInc == False and key > arr[mid]:
        return BinarySearch(arr, start, mid - 1, key, isInc)
    else:
        return BinarySearch(arr, mid + 1, end, key, isInc)


def findKeyCount(arr, key):
    size = len(arr)
    count = 0
    for i in range(size):
        if arr[i] == key:
            count += 1
    return count

def findFirstIndex(arr, start, end, key):
    if end < start:
        return -1
    #mid = math.floor((start + end) / 2)
    mid = ((start + end) / 2)
    if key == arr[mid] and (mid == start or arr[mid - 1] != key):
        return mid
    if key <= arr[mid]:
        return findFirstIndex(arr, start, mid - 1, key)
    else:
        return findFirstIndex(arr, mid + 1, end, key)

def findLastIndex(arr, start, end, key):
    if end < start:
        return -1
    #mid = math.floor((start + end) / 2)
    mid = ((start + end) / 2)
    if key == arr[mid] and (mid == end or arr[mid + 1] != key):
        return mid
    if key < arr[mid]:
        return findLastIndex(arr, start, mid - 1, key)
    else:
        return findLastIndex(arr, mid + 1, end, key)

def findKeyCount2(arr, key):
    size = len(arr)
    firstIndex = findFirstIndex(arr, 0, size - 1, key)
    lastIndex = findLastIndex(arr, 0, size - 1, key)
    return (lastIndex - firstIndex + 1)

def main10():
    first = [1, 5, 10, 13, 20, 30, 8, 7, 6]
    
    print(findKeyCount(first, 6))
    print(findKeyCount2(first, 6))
    # print(minabsSumPair(first))

def main11():
    first = [1, 5, 6, 6, 6, 6, 6, 6, 7, 8, 10, 13, 20, 30 ]
    print(findKeyCount(first, 6))
    print(findKeyCount2(first, 6))
    # print(minabsSumPair(first))



def swap(arr, first, second):
    temp = arr[first]
    arr[first] = arr[second]
    arr[second] = temp

def seperateEvenAndOdd(arr):
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


def main12():
    first = [1, 5, 6, 6, 6, 6, 6, 6, 7, 8, 10, 13, 20, 30 ]
    print(seperateEvenAndOdd(first))
    # print(findKeyCount2(first, 6))
    # print(minabsSumPair(first))

def main13():
    first = [10, 150, 6, 67, 61, 16, 86, 6, 67, 78, 150, 3, 28, 143 ]
    print(maxProfit(first))
    # print(findKeyCount2(first, 6))
    # print(minabsSumPair(first)

def maxProfit(stocks):
    size = len(stocks)
    buy = 0
    sell = 0
    curMin = 0
    currProfit = 0
    maxProfit = 0
    for i in range(size):
        if stocks[i] < stocks[curMin]:
            curMin = i
        currProfit = stocks[i] - stocks[curMin]
        if currProfit > maxProfit:
            buy = curMin
            sell = i
            maxProfit = currProfit
    print("Purchase day is - ", buy , " at price " , stocks[buy])
    print("Sell day is - " , sell , " at price " , stocks[sell])


def main14():
    # first = [10, 150, 6,67,61,16,86,6,67,78,150, -3, 28, 143 ]
    first = [1, 5, 6, 6, 6, 6, 6, 6, 7, 8, 10, 13, 20, 30 ]
    second = [1, 5, 6, 6, 6, 6, 6, 6, 7, 8, 10, 13, 20, 30 ]
    print(findMedian(first, second))
    # print(findKeyCount2(first, 6))
    # print(minabsSumPair(first))

def getMedian(arr):
    size = len(arr)
    arr.sort()
    return arr[size / 2]

def findMedian(arrFirst, arrSecond):
    sizeFirst = len(arrFirst)
    sizeSecond = len(arrSecond)
    medianIndex = ((sizeFirst + sizeSecond) + (sizeFirst + sizeSecond) % 2) / 2
    i = 0
    j = 0
    count = 0
    while count < medianIndex - 1:
        if i < sizeFirst - 1 and arrFirst[i] < arrSecond[j]:
            i += 1
        else:
            j += 1
        count += 1
    if arrFirst[i] < arrSecond[j]:
        return arrFirst[i]
    else:
        return arrSecond[j]


def min(a, b):
    return b if a > b else a


def max(a, b):
    return b if a < b else a


def main15():
    # first = [10, 150, 6,67,61,16,86,6,67,78,150, -3, 28, 143 ]
    # first = [1, 5, 6,6,6,6,6,6,7,8,10, 13, 20, 30 ]
    # second = [1, 5, 6,6,6,6,6,6,7,8,10, 13, 20, 30 ]
    first = "000000001111"
    print(BinarySearch01(first))
    # print(findKeyCount2(first, 6))
    # print(minabsSumPair(first))


def BinarySearch01(arr):
    size = len(arr)
    if size == 1 and arr[0] == '1':
        return 0
    return BinarySearch01Util(arr, 0, size - 1)


def BinarySearch01Util(arr, start, end):
    if end < start:
        return -1
    #mid = math.floor((start + end) / 2)
    mid = ((start + end) / 2)
    
    if '1' == arr[mid] and '0' == arr[mid - 1]:
        return mid
    if '0' == arr[mid]:
        return BinarySearch01Util(arr, mid + 1, end)
    else:
        return BinarySearch01Util(arr, start, mid - 1)


def main16():
    # first = [10, 150, 6,67,61,16,86,6,67,78,150, -3, 28, 143 ]
    first = [34, 56, 77, 1, 5, 6, 6, 6, 6, 6, 6, 7, 8, 10, 13, 20, 30 ]
    # second = [1, 5, 6,6,6,6,6,6,7,8,10, 13, 20, 30 ]
    print(BinarySearchRotateArray(first, 20))
    # print(findKeyCount2(first, 6))
    # print(minabsSumPair(first))


def BinarySearchRotateArray(arr, key):
    size = len(arr)
    return BinarySearchRotateArrayUtil(arr, 0, size - 1, key)


def BinarySearchRotateArrayUtil(arr, start, end, key):
    if end < start:
        return False
    #mid = math.floor((start + end) / 2)
    mid = ((start + end) / 2)
    
    if key == arr[mid]:
        return True
    if arr[mid] > arr[start]:
        if arr[start] <= key and key < arr[mid]:
            return BinarySearchRotateArrayUtil(arr, start, mid - 1, key)
        else:
            return BinarySearchRotateArrayUtil(arr, mid + 1, end, key)
    else:
        if arr[mid] < key and key <= arr[end]:
            return BinarySearchRotateArrayUtil(arr, mid + 1, end, key)
        else:
            return BinarySearchRotateArrayUtil(arr, start, mid - 1, key)



def main17():
    # first = [10, 150, 6,67,61,16,86,6,67,78,150, -3, 28, 143 ]
    first = [34, 56, 77, 1, 5, 6, 6, 6, 6, 6, 6, 7, 8, 10, 34, 20, 30 ]
    # second = [1, 5, 6,6,6,6,6,6,7,8,10, 13, 20, 30 ]    
    print(FirstRepeated(first))
    # print(findKeyCount2(first, 6))
    # print(minabsSumPair(first))


def FirstRepeated(arr):
    size = len(arr)
    for i in range(size):
        for j in range(i+1, size):
            if arr[i] == arr[j]:
                return arr[i]
    return sys.maxint  # can raise exception.


def main18():
    # [10, 150, 6,67,61,16,86,6,67,78,150, -3, 28, 143 ]
    # first = [34, 56, 77, 1, 5, 6, 6, 6, 6, 6, 6, 7, 8, 10, 34, 20, 30 ]
    # second = [1, 5, 6,6,6,6,6,6,7,8,10, 13, 20, 30 ]    
    print(transformArrayAB1("aaaabbbb"))


def transformArrayAB1(strval):
    arr = list(strval)
    size = len(arr)
    #N = math.floor(size / 2)
    N = (size / 2)
    i = 1
    for i in range(1, N):
        for j in range(i):
            swap(arr, N - i + 2 * j, N - i + 2 * j + 1)
    return "".join(arr)


def main19():
    print(checkPermutation2("aaaabbbb", "bbaaaabb"))


def checkPermutation(str1, str2):
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


def checkPermutation2(array1, array2):
    size1 = len(array1)
    size2 = len(array2)        
    if size1 != size2:
        return False
    al = []
    for i in range(size1):
        al.append(array1[i])

    for i in range(size2):
        if al.count(array2[i]) == 0:
            return False
        al.remove(array2[i])
    return True


def main20():
    first = [1, 7, 6, 4, 8, 3, 8, 2, 6, 9]
    print(removeDuplicates(first))


def removeDuplicates(array):
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


def FindElementIn2DArray(arr, r, c, value):
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


main1()
main2()
main3()
main4()
main5()
main6()
main7()
main8()
main9()
main10()
main11()
main12()
main13()
main14()
main15()
main16()
main17()
main18()
main19()
main20()
