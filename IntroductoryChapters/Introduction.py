#!/usr/bin/env python

def increment1(var):
    """ Source for method increment """
    var += 1

def main1():
    """ Source for method main """
    var = 1
    print("Value before increment :" , var)
    increment1(var)
    print("Value after increment :" , var)
    
class MyInt(object):
    def __init__(self):
        self.value = 1

def increment2(value):
    """ Source for method increment """
    value.value += 1   
    
def main2():
    """ Source for method main """
    var = MyInt()
    print("Value before increment :" , var.value)
    increment2(var)
    print("Value after increment :" , var.value)  
        

def swap(arr, x, y):
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp


def permutation(arr, i, length):
    if length == i:
        print(arr)
        return
    j = i
    while j < length:
        swap(arr, i, j)
        permutation(arr, i + 1, length)
        swap(arr, i, j)
        j += 1


def main3():
    arr = [None] * 5
    for i in range(5):
        arr[i] = i
    permutation(arr, 0, 5)


def GCD(m, n):
    if m < n:
        return (GCD(n, m))
    if m % n == 0:
        return (n)
    return (GCD(n, m % n))


def main4():
    print(GCD(5, 2))


def towerOfHanoi(num, src, dst, temp):
    if num < 1:
        return
    towerOfHanoi(num - 1, src, temp, dst)
    print("Move " , num , " disk  from peg " , src , " to peg " , dst)
    towerOfHanoi(num - 1, temp, dst, src)


def main5():
    num = 4
    print("The sequence of moves involved in the Tower of Hanoi are :")
    towerOfHanoi(num, 'A', 'C', 'B')


def function2():
    print("fun2 line 1")


def function1():
    print("fun1 line 1")
    function2()
    print("fun1 line 2")


def main6():
    print("main line 1")
    function1()
    print("main line 2")


def maxSubArraySum(arr):
    size = len(arr)
    maxSoFar = 0
    maxEndingHere = 0
    for i in range(size):
        maxEndingHere = maxEndingHere + arr[i]
        if maxEndingHere < 0:
            maxEndingHere = 0
        if maxSoFar < maxEndingHere:
            maxSoFar = maxEndingHere
    return maxSoFar



def main7():
    arr = [1, -2, 3, 4, -4, 6, -4, 8, 2]
    print(maxSubArraySum(arr))


def variableExample():
    var1 = 100
    var2 = 200
    var3 = var1 + var2
    print("Adding" , var1 , "and" , var2 , "will give" , var3)


def arrayExample():
    arr = [0] * 10
    for i in range(10):
        arr[i] = i
    printArray1(arr)
    return arr


def printArray1(arr):
    count = len(arr)
    for i in range(count):
        print(arr[i])#, end=' ')


def main8():
    twoDArrayExample()


def twoDArrayExample():
    first = 4
    second = 4
    arr = [[0 for x in range(first)] for y in range(second) ]
    count = 0
    for i in range(first):
        for j in range(second):
            arr[i][j] = count
            count += 1
    print2DArray(arr, first, second)


def print2DArray(arr, row, col):
    i = 0
    for i in range(row):
        for j in range(col):
            print(arr[i][j])#, end=' ')

def main9():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(SumArray(arr))

def SumArray(arr):
    size = len(arr)
    total = 0
    for index in range(size):
        total = total + arr[index]
    return total


def SequentialSearch(arr, value):
    size = len(arr)
    for i in range(size):
        if value == arr[i]:
            return True
    return False


def BinarySearch(arr, value):
    size = len(arr)
    low = 0
    high = size - 1
    while low <= high:
        mid = low + (high - low) / 2
        if arr[mid] == value:
            return True
        else:
            if arr[mid] < value:
                low = mid + 1
            else:
                high = mid - 1
    return False


def main10():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(BinarySearch(arr, 6))


def rotateArray(arr, k):
    n = len(arr)
    reverseArray(arr, 0, k - 1)
    reverseArray(arr, k, n - 1)
    reverseArray(arr, 0, n - 1)


def reverseArray(arr, start, end):
    i = start
    j = end
    while i < j:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i += 1
        j -= 1


def reverseArray_0(a):
    start = 0
    end = len(a)
    i = start
    j = end
    while i < j:
        temp = a[i]
        a[i] = a[j]
        a[j] = temp
        i += 1
        j -= 1


def main11():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    rotateArray(arr, 3)
    print(arr)


class coord(object):
    x = int()
    y = int()

def main12():
    point = coord()
    point.x = 10
    point.y = 10
    print("X axis coord value is  " , point.x)
    print("Y axis coord value is  " , point.y)


class student(object):
    rollNo = int()
    firstName = str()
    lastName = str()

def main13():
    stud = student()
    refStud = stud
    refStud.rollNo = 1
    refStud.firstName = "john"
    refStud.lastName = "smith"
    print("Roll No:   Student Name:  " , refStud.rollNo , refStud.firstName , refStud.lastName)


def main14():
    x = 10
    y = 20
    result = sum(x, y)
    print("Sum is : " , result)


def sum(num1, num2):
    result = num1 + num2
    return result


def factorial(i):
    if i <= 1:
        return 1
    return i * factorial(i - 1)


def main15():
    print(factorial(5))


def printInt(number):
    conversion = "0123456789"
    digit = number % 10
    number = number / 10
    temp = ""
    if number != 0:
        temp += printInt(number)
    temp += conversion[digit]
    return temp


def main16():
    print(printInt2(50, 2))
    

def printInt2(number, base):
    conversion = "0123456789ABCDEF"
    digit = number % base
    number = number / base
    temp = ""
    if number != 0:
        temp += printInt2(number, base)
    temp += conversion[digit]
    return temp


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def main17():
    print(fibonacci(6))


def BinarySearchRecursive(arr, low, high, value):
    mid = low + (high - low) / 2
    if arr[mid] == value:
        return mid
    elif arr[mid] < value:
        return BinarySearchRecursive(arr, mid + 1, high, value)
    else:
        return BinarySearchRecursive(arr, low, mid - 1, value)


def main18():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(BinarySearch(arr, 6))
    print(BinarySearch(arr, 16))

        
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
