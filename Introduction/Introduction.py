def increment1(var):
    """ Source for method increment """
    var += 1

def test1():
    """ Source for method # test """
    var = 1
    print("Value before increment :", var)
    increment1(var)
    print("Value after increment :", var)

"""
Value before increment : 1
Value after increment : 1
"""

class MyInt(object):
    def __init__(self):
        self.value = 1


def increment2(value):
    """ Source for method increment """
    value.value += 1

def test2():
    """ Source for method # test """
    var = MyInt()
    print("Value before increment :", var.value)
    increment2(var)
    print("Value after increment :", var.value)


"""
Value before increment : 1
Value after increment : 2
"""

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

def test3():
    arr = list(range(3))
    permutation(arr, 0, 3)

"""
[0, 1, 2]
[0, 2, 1]
[1, 0, 2]
[1, 2, 0]
[2, 1, 0]
[2, 0, 1]
"""

def gcd(m, n):
    if m < n:
        return (gcd(n, m))
    if m % n == 0:
        return (n)
    return (gcd(n, m % n))

def test4():
    print("Gcd is::", gcd(5, 2))

"""
Gcd is:: 1
"""

def tower_of_hanoi(num, src, dst, temp):
    if num < 1:
        return
    tower_of_hanoi(num - 1, src, temp, dst)
    print("Move ", num, " disk  from peg ", src, " to peg ", dst)
    tower_of_hanoi(num - 1, temp, dst, src)

def toh(num):  
    print("The sequence of moves involved in the Tower of Hanoi are :")
    tower_of_hanoi(num, 'A', 'C', 'B')

toh(3)

"""
Move  1  disk  from peg  A  to peg  C
Move  2  disk  from peg  A  to peg  B
Move  1  disk  from peg  C  to peg  B
Move  3  disk  from peg  A  to peg  C
Move  1  disk  from peg  B  to peg  A
Move  2  disk  from peg  B  to peg  C
Move  1  disk  from peg  A  to peg  C
"""


def function2():
    print("fun2 line 1")

def function1():
    print("fun1 line 1")
    function2()
    print("fun1 line 2")

def test5():
    print("test line 1")
    function1()
    print("test line 2")

"""
test line 1
fun1 line 1
fun2 line 1
fun1 line 2
test line 2
"""

def max_subarray_sum(arr):
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


def test6():
    arr = [1, -2, 3, 4, -4, 6, -4, 8, 2]
    print(max_subarray_sum(arr))

# 15

def variable_example():
    var1 = 100
    var2 = 200
    var3 = var1 + var2
    print("Adding", var1, "and", var2, "will give", var3)

def array_example():
    arr = [0] * 10
    for i in range(10):
        arr[i] = i
    print_array1(arr)
    return arr

def print_array1(arr):
    count = len(arr)
    for i in range(count):
        print(arr[i], end=' ')

def twoD_array_example():
    first = 4
    second = 4
    arr = [[0 for x in range(first)] for y in range(second)]
    count = 0
    for i in range(first):
        for j in range(second):
            arr[i][j] = count
            count += 1
    print_2d_array(arr, first, second)


def print_2d_array(arr, row, col):
    i = 0
    for i in range(row):
        for j in range(col):
            print(arr[i][j] , end=' ')

def test7():
    twoD_array_example()


"""
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 12
"""

def sum_array(arr):
    size = len(arr)
    total = 0
    for index in range(size):
        total += arr[index]
    return total

def test8():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(sum_array(arr))


#45

def sequential_search(arr, value):
    size = len(arr)
    for i in range(size):
        if value == arr[i]:
            return True
    return False


def binary_search(arr, value):
    size = len(arr)
    low = 0
    high = size - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == value:
            return True
        else:
            if arr[mid] < value:
                low = mid + 1
            else:
                high = mid - 1
    return False

def binary_search_recursive(arr, low, high, value):
    if low > high:
        return False

    mid = (low + high )// 2
    if arr[mid] == value:
        return True
    elif arr[mid] < value:
        return binary_search_recursive(arr, mid + 1, high, value)
    else:
        return binary_search_recursive(arr, low, mid - 1, value)

def binary_search2(arr, value):
    size = len(arr)
    low = 0
    high = size - 1
    return binary_search_recursive(arr, low, high, value)

def test9():
    arr = [1, 2, 3, 4, 5, 7, 8, 9]
    """
    print(sequential_search(arr, 5))
    print(sequential_search(arr, 6))

    print(binary_search(arr, 5))
    print(binary_search(arr, 6))
    """
    print(binary_search(arr, 6))
    print(binary_search(arr, 16))
    print(binary_search2(arr, 6))
    print(binary_search2(arr, 16))


"""
True
False
True
False

True
False
True
False
"""

def rotate_array(arr, k):
    n = len(arr)
    reverse_array(arr, 0, k - 1)
    reverse_array(arr, k, n - 1)
    reverse_array(arr, 0, n - 1)

def reverse_array(arr, start, end):
    i = start
    j = end
    while i < j:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i += 1
        j -= 1

def reverse_array2(a):
    i = 0 # Start index
    j = len(a) -1 # End index
    while i < j:
        temp = a[i]
        a[i] = a[j]
        a[j] = temp
        i += 1
        j -= 1

def test10():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    rotate_array(arr, 3)
    print(arr)
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    reverse_array2(arr)
    print(arr)


"""
[4, 5, 6, 7, 8, 9, 1, 2, 3]
[9, 8, 7, 6, 5, 4, 3, 2, 1]
"""

class coord(object):
    x = int()
    y = int()

def test11():
    point = coord()
    point.x = 10
    point.y = 10
    print("X axis coord value is:", point.x)
    print("Y axis coord value is:", point.y)


"""
X axis coord value is: 10
Y axis coord value is: 10
"""

class Student(object):
    rollNo = int()
    firstName = str()
    lastName = str()


def test12():
    stud = Student()
    ref = stud
    ref.rollNo = 1
    ref.firstName = "john"
    ref.lastName = "smith"
    print("Roll No:", ref.rollNo, "Student Name: ", ref.lastName)


"""
Roll No: 1 Student Name:  smith
"""

def sum(num1, num2):
    result = num1 + num2
    return result

def test13():
    x = 10
    y = 20
    result = sum(x, y)
    print("Sum is :", result)


"""
Sum is : 30
"""

def factorial(i):
    if i <= 1:
        return 1
    return i * factorial(i - 1)

def test14():
    print("Factorial:", factorial(5))


"""
Factorial: 120
"""

def print_int(number):
    conversion = "0123456789"
    digit = number % 10
    number = number // 10
    temp = ""
    if number != 0:
        temp += print_int(number)
    temp += conversion[digit]
    return temp

def print_int2(number, base):
    conversion = "0123456789ABCDEF"
    digit = number % base
    number = number // base
    temp = ""
    if number != 0:
        temp += print_int2(number, base)
    temp += conversion[digit]
    return temp

def test15():
    print(print_int(50))
    print(print_int2(50, 2))


"""
50
110010
"""

def fibonacci(n):
    if n == 1 or n == 0:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def test16():
    for i in range(7):
        print(fibonacci(i), end=" ")


"""
0 1 1 2 3 5 8
"""

"""
Given array of size N, containing elements from 0 to N-1. 
All values from O to N-1 are present in array and if they 
are not there then -1 is there to take its place.
Arrange values of array so that value i is stored at arr[i].
arr = [ 8, -1, 6, 1, 9, 3, 2, 7, 4, -1 ]

"""
def index_array( arr):
    size = len(arr)
    for i in range(size):
        curr = i
        value = -1

        # swaps to move elements in proper position.
        while arr[curr] != -1 and arr[curr] != curr:
            temp = arr[curr]
            arr[curr] = value
            value = curr = temp

        # if some swaps happened.
        if value != -1: 
            arr[curr] = value


def index_array2(arr):
    size = len(arr)
    for i in range(size):
        while arr[i] != -1 and arr[i] != i:
            # swap arr[i] and arr[arr[i]]
            temp = arr[i]
            arr[i] = arr[temp]
            arr[temp] = temp

def test17():
    arr = [ 8, -1, 6, 1, 9, 3, 2, 7, 4, -1 ]
    index_array( arr)
    print(arr)

    arr = [20, 11, 10, 9, 5, 13, 16, 2, 14, 17,19, 7, 0, 3, 18, 15, 12, 6, 1, 8, 4]
    index_array2( arr)
    print(arr)


"""
[-1, 1, 2, 3, 4, -1, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
"""

"""
Given an unsorted array , find smallest positive number missing in the array.
"""
def smallest_positive_missing_number(arr):
    size = len(arr)
    for i in range(1, size+1, 1):
        found = False
        for j in range(size):
            if arr[j] == i:
                found = True
                break
        if found == False:
            return i
    return -1

def smallest_positive_missing_number2(arr):
    size = len(arr)
    hs = {}
    for i in range(size):
        hs[arr[i]] = 1
    
    for i in range(1, size+1, 1):
        if i not in hs:
            return i
    return -1


def smallest_positive_missing_number3(arr):
    size = len(arr)
    aux = [-1]*size
    for i in range(size):
        if arr[i] > 0 and arr[i] <= size:
            aux[arr[i] - 1] = arr[i]

    for i in range(size):
        if aux[i] != i+1 :
            return i+1
    return -1

def smallest_positive_missing_number4(arr):
    size = len(arr)
    for i in range(size):
        curr = i
        value = -1
        if arr[curr] > 0 :
            # swaps to move elements in proper position.
            while curr >= 0 and curr < size and arr[curr] != curr+1 :
                next = arr[curr]
                arr[curr] = value
                value = next
                curr = next - 1

    for i in range(size):
        if arr[i] != i+1 :
            return i+1
    return -1

def smallest_positive_missing_number5(arr):
    size = len(arr)
    for i in range(size):
        while arr[i] != i+1 and arr[i] > 0 and arr[i] <= size:
            temp = arr[i]
            arr[i] = arr[temp - 1]
            arr[temp - 1] = temp

    for i in range(size):
        if arr[i] != i+1 :
            return i+1
    return -1

def test18():
    arr = [2, 3, 7, 6, 8, -1, -10, 15]
    print(smallest_positive_missing_number(arr))
    print(smallest_positive_missing_number2(arr))
    print(smallest_positive_missing_number3(arr))
    print(smallest_positive_missing_number4(arr))
    print(smallest_positive_missing_number5(arr))
    arr = [2, 3, 7, 6, 8, 1, 4, 5]
    print(smallest_positive_missing_number(arr))
    print(smallest_positive_missing_number2(arr))
    print(smallest_positive_missing_number3(arr))
    print(smallest_positive_missing_number4(arr))
    print(smallest_positive_missing_number5(arr))


"""
1
1
1
1
1
-1
-1
-1
-1
-1
"""


"""
Given an array of length N. It contains unique elements from 1 to N. 
Sort the elements of the array.
"""

def sort_1toN(arr):
    size = len(arr)
    for i in range(size):
        curr = i
        value = -1
        # swaps to move elements in proper position.
        while curr >= 0 and curr < size and arr[curr] != curr+1 :
            next = arr[curr]
            arr[curr] = value
            value = next
            curr = next - 1

def sort_1toN2(arr):
    size = len(arr)
    for i in range(size):
        while arr[i] != i+1 and arr[i] > 1:
            temp = arr[i]
            arr[i] = arr[temp - 1]
            arr[temp - 1] =  temp

def test19():
    arr = [10, 7, 9, 2, 8, 3, 5, 4, 6, 1]
    sort_1toN(arr)
    print(arr)
    arr = [10, 7, 9, 2, 8, 3, 5, 4, 6, 1]
    print(arr)
    sort_1toN2(arr)
    print(arr)


"""
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""

"""Given a sorted array rearrange it in maximum minimum form.
Input  : [1, 2, 3, 4, 5, 6, 7]
Output : [7, 1, 6, 2, 5, 3, 4]
"""
def max_min_array(arr):
    size = len(arr)
    aux = list(arr)
    start = 0
    stop = size - 1
    for i in range(size):
        if i % 2 == 0 :
            arr[i] = aux[stop]
            stop -= 1
        else :
            arr[i] = aux[start]
            start += 1


"""
Without using any auxiliary array.
1, 2, 3, 4, 5, 6, 7
7, 6, 5, 4, 3, 2, 1
7, 1, 2, 3, 4, 5, 6
7, 1, 6, 5, 4, 3, 2
7, 1, 6, 2, 3, 4, 5
7, 1, 6, 2, 5, 4, 3
7, 1, 6, 2, 5, 3, 4
"""
def reverse_array(arr, start, stop):
    while start < stop:
        arr[start], arr[stop] = arr[stop], arr[start]
        start += 1
        stop -= 1

def max_min_array2(arr):
    size = len(arr)
    for i in range(size-1):
        reverse_array(arr, i, size-1)

def test20():
    arr = [1, 2, 3, 4, 5, 6, 7]
    max_min_array(arr)
    print(arr)
    arr = [1, 2, 3, 4, 5, 6, 7]
    max_min_array2(arr)
    print(arr)


"""
[7, 1, 6, 2, 5, 3, 4]
[7, 1, 6, 2, 5, 3, 4]
"""

def find_max_path_util(arr, max_column, max_row, curr_column, curr_row, traversed, temp):
    if curr_column < 0 or curr_column >= max_column or curr_row < 0 or curr_row >= max_row :
        return
    if traversed[curr_column][curr_row] == 1 or arr[curr_column][curr_row] == 0:
        return
    traversed[curr_column][curr_row] = 1
    temp[0] += 1
    # each line corresponding to 8 direction.
    find_max_path_util(arr, max_column, max_row, curr_column-1, curr_row-1, traversed, temp)
    find_max_path_util(arr, max_column, max_row, curr_column-1, curr_row, traversed, temp)
    find_max_path_util(arr, max_column, max_row, curr_column-1, curr_row+1, traversed, temp)
    find_max_path_util(arr, max_column, max_row, curr_column, curr_row-1, traversed, temp)
    find_max_path_util(arr, max_column, max_row, curr_column, curr_row+1, traversed, temp)
    find_max_path_util(arr, max_column, max_row, curr_column+1, curr_row-1, traversed, temp)
    find_max_path_util(arr, max_column, max_row, curr_column+1, curr_row, traversed, temp)
    find_max_path_util(arr, max_column, max_row, curr_column+1, curr_row+1, traversed, temp)
    return

def find_max_path(arr, max_column, max_row):
    max_value = 0
    traversed = [[0]*max_column for i in range(max_row)]
    temp = [0]
    for i in range(0, max_column-1, 1):
        for j in range(0, max_row-1, 1):
            temp[0] = 0
            find_max_path_util(arr, max_column, max_row, i, j, traversed, temp)
            if(temp[0] > max_value):
                max_value = temp[0]
    return max_value

def test21():
    arr = [
        [ 1 , 0 , 1, 1 , 0], 
        [ 1 , 0 , 0, 1 , 0], 
        [ 0 , 1 , 1, 1 , 1], 
        [ 0 , 1 , 0, 0 , 0], 
        [ 1 , 1 , 0, 0 , 1]]    
    print(find_max_path(arr, 5, 5))


"""
12
"""

def find_max_path_util2(arr, max_column, max_row, curr_column, curr_row, value, traversed, temp):
    if curr_column < 0 or curr_column >= max_column or curr_row < 0 or curr_row >= max_row :
        return
    if traversed[curr_column][curr_row] == 1 or arr[curr_column][curr_row] != value:
        return
    traversed[curr_column][curr_row] = 1
    temp[0] += 1
    # each line corresponding to 8 direction.
    find_max_path_util2(arr, max_column, max_row, curr_column-1, curr_row-1, value, traversed, temp)
    find_max_path_util2(arr, max_column, max_row, curr_column-1, curr_row, value, traversed, temp)
    find_max_path_util2(arr, max_column, max_row, curr_column-1, curr_row+1, value, traversed, temp)
    find_max_path_util2(arr, max_column, max_row, curr_column, curr_row-1, value, traversed, temp)
    find_max_path_util2(arr, max_column, max_row, curr_column, curr_row+1, value, traversed, temp)
    find_max_path_util2(arr, max_column, max_row, curr_column+1, curr_row-1, value, traversed, temp)
    find_max_path_util2(arr, max_column, max_row, curr_column+1, curr_row, value, traversed, temp)
    find_max_path_util2(arr, max_column, max_row, curr_column+1, curr_row+1, value, traversed, temp)
    return

def find_max_path_util(arr, max_column, max_row, curr_column, curr_row, value, traversed):
    if curr_column < 0 or curr_column >= max_column or curr_row < 0 or curr_row >= max_row :
        return 0
    if traversed[curr_column][curr_row] == 1 or arr[curr_column][curr_row] != value:
        return 0
    traversed[curr_column][curr_row] = 1
    # each call corresponding to 8 direction.
    return 1 + find_max_path_util(arr, max_column, max_row, curr_column-1, curr_row-1, value, traversed) + find_max_path_util(arr, max_column, max_row, curr_column-1, curr_row, value, traversed) + find_max_path_util(arr, max_column, max_row, curr_column-1, curr_row+1, value, traversed) + find_max_path_util(arr, max_column, max_row, curr_column, curr_row-1, value, traversed) + find_max_path_util(arr, max_column, max_row, curr_column, curr_row+1, value, traversed) + find_max_path_util(arr, max_column, max_row, curr_column+1, curr_row-1, value, traversed) + find_max_path_util(arr, max_column, max_row, curr_column+1, curr_row, value, traversed) + find_max_path_util(arr, max_column, max_row, curr_column+1, curr_row+1, value, traversed)


def find_max_path(arr, max_column, max_row):
    max_value = 0
    traversed = [[0]*max_column for i in range(max_row)]
    for i in range(max_column):
        for j in range(max_row):
            temp = find_max_path_util(arr, max_column, max_row, i, j, arr[i][j], traversed)
            if(temp > max_value):
                max_value = temp
    return max_value

def test22():
    arr = [
        [ 1 , 0 , 1, 1 , 0], 
        [ 1 , 0 , 0, 1 , 0], 
        [ 0 , 0 , 1, 1 , 1], 
        [ 0 , 1 , 0, 0 , 0], 
        [ 1 , 1 , 0, 0 , 1]]
    print(find_max_path(arr, 5, 5))

    arr = [
        [ 1 , 0 , 1, 1 , 0], 
        [ 1 , 1 , 0, 3 , 0], 
        [ 3 , 3 , 1, 1 , 3], 
        [ 0 , 3 , 3, 0 , 3], 
        [ 1 , 1 , 0, 3 , 3]]    
    print(find_max_path(arr, 5, 5))


"""
11
9
"""

from collections import deque

INFI = 99999
def rotten_fruit(arr, max_column, max_row):
    que = deque([])
    max_day = 0
    traversed = [[INFI]*max_column for i in range(max_row)]
    for i in range(0, max_column-1):
        for j in range(0, max_row-1):
            if arr[i][j] == 2:
                que.append((i,j, 0))

    while len(que) != 0:
        (curr_column, curr_row, day) = que.popleft()
        if traversed[curr_column][curr_row] > day and arr[curr_column][curr_row] != 0:
            
            traversed[curr_column][curr_row] = day
            if day > max_day :
                max_day = day

            if curr_column > 0:
                que.append((curr_column-1, curr_row, day+1))
            if curr_column < max_column - 1:
                que.append((curr_column+1, curr_row, day+1))
            if curr_row > 0 :
                que.append((curr_column, curr_row-1, day+1))
            if curr_row < max_row - 1 :
                que.append((curr_column, curr_row+1, day+1))
        
    return max_day

def test23():   
    arr = [
        [ 1 , 0 , 1, 1 , 0], 
        [ 1 , 2, 0, 1 , 0], 
        [ 0 , 0 , 0, 2 , 1], 
        [ 0 , 2 , 0, 0 , 1], 
        [ 1 , 1 , 0, 0 , 1]]
    print(rotten_fruit(arr, 5, 5))


"""
3
"""

"""
Given an array arr[], find maximum distance of index j and i, such that arr[j] > arr[i]

first solution : Brute force, for each index call it i find index j such that arr[j] > arr[i]
We will need two loops one to select index i and another to traverse index i+1 to size of array.
always keep decreasing array index. 
Second solution is done using preprocessing and creating two auxilarry arrays. 
"""
def array_index_max_diff(arr):
    size = len(arr)
    max_diff = -1
    for i in range(size):
        j = size - 1
        while(j > i):
            if arr[j] >= arr[i] :
                max_diff = max(max_diff, j-i)
                break
            j -= 1
    return max_diff


def array_index_max_diff2(arr):
    size = len(arr)
    left_min = [0]*size
    right_max = [0]*size
    left_min[0] = arr[0]
    for i in range(1, size, 1):
        if left_min[i-1] <= arr[i]:
            left_min[i] = left_min[i-1]
        else:
            left_min[i] = arr[i] 

    right_max[size - 1] = arr[size - 1]
    for i in reversed(list(range(size - 1))):
        if right_max[i+1] >= arr[i]:
            right_max[i] = right_max[i+1]
        else:
            right_max[i] = arr[i] 
    i = 0
    j = 0
    max_diff = -1
    while j < size and i < size :
        if left_min[i] <= right_max[j] : 
            max_diff = max(max_diff, j-i)
            j = j + 1
        else:
            i = i+1
    return max_diff

def array_index_max_diff3(arr):
    size = len(arr)
    left_min = []
    right_max = []
    left_min.append(0)
    for i in range(1, size, 1):
        if arr[left_min[-1]] >= arr[i]:
            left_min.append(i)

    right_max.append(size - 1)
    for i in reversed(list(range(size - 1))):
        if arr[right_max[-1]] <= arr[i]:
            right_max.append(i)

    i = 0
    j = len(right_max) - 1
    max_diff = -1
    firstSize = len(left_min)

    while i < firstSize and j >= 0 :
        if arr[left_min[i]] <= arr[right_max[j]] :
            max_diff = max(max_diff, right_max[j]-left_min[i])
            j -= 1
        else:
            i += 1
    return max_diff

def test24():
    arr = [33, 9, 10, 3, 2, 60, 30, 33, 1]
    print(array_index_max_diff(arr))
    arr = [33, 9, 10, 3, 2, 60, 30, 33, 1]
    print(array_index_max_diff2(arr))
    arr = [33, 9, 10, 3, 2, 60, 30, 33, 1]
    print(array_index_max_diff3(arr))

    arr = [9, 2, 3, 4, 5, 6, 7, 8, 1]
    print(array_index_max_diff(arr))
    arr = [9, 2, 3, 4, 5, 6, 7, 8, 1]
    print(array_index_max_diff2(arr))
    arr = [9, 2, 3, 4, 5, 6, 7, 8, 1]
    print(array_index_max_diff3(arr))


"""
7
7
7
6
6
6
"""

"""
Largest Increasing subsequence
"""
def largest_increasing_subseq(arr ):
    max_value = 0
    size = len(arr)
    lis = [1]*size
    for i in range(size):
        for j in range(i):
            if arr[j] < arr[i] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

        if max_value < lis[i]:
            max_value = lis[i]
    return max_value

def test25():
    arr = [10 , 12 , 9 , 23 , 25 , 55 , 49 , 70]
    print(largest_increasing_subseq(arr))


"""
6
"""

def longest_bitonic_subsequence(arr ):
    max_value = 0
    size = len(arr)
    lis = [1]*size
    lds = [1]*size
    for i in range(size):
        for j in range(i):
            if arr[j] < arr[i] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    for i in reversed(list(range(size))):
        for j in reversed(list(range(i, size))):
            if arr[j] < arr[i] and lds[i] < lds[j] + 1:
                lds[i] = lds[j] + 1

    for i in range(size):
        max_value = max((lis[i] + lds[i] - 1), max_value)
    return max_value

def test26():
    arr = [1 , 6 , 3, 11, 1, 9 , 5 , 12 , 3 , 14 , 6 , 17, 3, 19 , 2 , 19]
    print(longest_bitonic_subsequence(arr))


"""
8
"""

def max_circular_sum(arr):
    sum_all = 0
    curr_value = 0
    n = len(arr)
 
    for i in range(n):
        sum_all += arr[i]
        curr_value += (i*arr[i])
 
    max_value = curr_value
    for i in range(1, n, 1):
        curr_value = ( curr_value + sum_all ) - ( n * arr[n-i] )
        #print curr_value
        if curr_value > max_value:
            max_value = curr_value
            
    return max_value

def test27():
    arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(max_circular_sum(arr))


"""
290
"""

def max_profit(price):
    size = len(price)
    profit = [0]*size
     
    max_price=price[size - 1]
    for i in range( size-2, -1 ,-1):
        if price[i]> max_price:
            max_price = price[i]
             
        profit[i] = max(profit[i+1], max_price - price[i])
    print(profit)
    return profit[0]

def max_profit2(price):
    size = len(price)
    profit = [0]*size
    
    min_price=price[0]
    for i in range(1,size):
        if price[i] < min_price:
            min_price = price[i]

        profit[i] = max(profit[i-1], profit[i]+(price[i]-min_price))
    print(profit)
    return profit[size-1]

def test28():
    price = [2, 30, 15, 10, 8, 25, 80]
    print("Maximum profit is", max_profit(price))
    print("Maximum profit is", max_profit2(price))



"""
[78, 72, 72, 72, 72, 55, 0]
Maximum profit is 78
[0, 28, 28, 28, 28, 28, 78]
Maximum profit is 78
"""

# Find maximum contiguous subarray
def max_subarray_sum(arr):
    size = len(arr)
    maximum = 0
    max_curr = 0
      
    for i in range(size):
        max_curr = max_curr + arr[i]
        if max_curr < 0:
            max_curr = 0
        elif (maximum < max_curr):
            maximum = max_curr
 
    return maximum

def test29():
    a = [-1, -3, 4, -1, -2, 1, 5]
    print(max_subarray_sum(a))


"""
7
"""

def max_path_sum(arr1, arr2):
    i, j, result, sum1, sum2 = 0, 0, 0, 0, 0
    size1 = len(arr1)
    size2 = len(arr2)

    while i < size1 and j < size2:
        if arr1[i] < arr2[j] :
            sum1 += arr1[i]
            i += 1
        elif arr1[i] > arr2[j] :
            sum2 += arr2[j]
            j += 1
        else :
            result += max(sum1, sum2)
            result = result + arr1[i]
            sum1 = 0
            sum2 = 0
            i += 1
            j += 1
 
    while i < size1 :
        sum1  +=  arr1[i]
        i += 1
 
    while j < size2:
        sum2 +=  arr2[j]
        j += 1
 
    result +=  max(sum1, sum2)
    return result

def test30():
    arr1 = [12, 13, 18, 20, 22, 26, 70]
    arr2 = [11, 15, 18, 19, 20, 26, 30, 31]
    print(max_path_sum(arr1, arr2))


# 201


"""
Given an array and two numbers X and Y, 
find the minimum distance between X and Y in array.
"""
import sys

def min_dist(arr, first, second):
    size = len(arr)
    min_dist = sys.maxsize
    for i in range(size):
        for j in range(i + 1, size):
            if ((arr[i] == first and arr[j] == second) or (arr[i] == second and arr[j] == first)) and min_dist > (j - i):
                min_dist = (j - i)
        return min_dist

def min_dist2(arr, first, second):
    size = len(arr)
    min_dist = sys.maxsize
    prev = -1
    for i in range(size):
        if arr[i] == first or arr[i] == second :
            if prev == -1 :
                prev = i
            elif arr[prev] != arr[i] and (i - prev) < min_dist :
                min_dist = (i - prev)
                prev = i
            else :
                prev = i
    return min_dist

def test31():
    arr = [3, 5, 4, 2, 6, 5, 6, 6, 5, 4, 8, 3]
    first = 3
    second = 6
    print(min_dist(arr, first, second))
    print(min_dist2(arr, first, second))


"""
4
4
"""

"""
Given an array of positive elements. Find minimum product of k elements in array.
"""
def ksmallest_product(arr, k):
    arr.sort()
    product = 1
    for i in range(k):
        product *= arr[i]
    return product

import heapq
def ksmallest_product2(arr, k):
    size = len(arr)
    heapq.heapify(arr)
    i = 0
    product = 1
    while i < size and i < k:
        product *= heapq.heappop(arr)
        i += 1
    return product

"""
Quick select method
"""
def ksmallest_product3(array, k):
    arr = array
    size = len(arr)
    quick_select_util(arr, 0, size-1, k)
    product = 1
    for i in range(k):
        product *= arr[i]
    return product

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
            swap(arr, upper, lower)
    swap(arr, upper, start)    # upper is the pivot position
    
    if k < upper: 
        # pivot -1 is the upper for left sub array.
        quick_select_util(arr, start, upper - 1, k)
    
    if k > upper:
        #  pivot + 1 is the lower for right sub array.
        quick_select_util(arr, upper + 1, stop, k)   
          
def swap(arr, first, second):
    arr[first], arr[second] = arr[second], arr[first]

def test32():
    first = [1, 7, 5, 4, 8, 3, 9, 2, 6, 10]
    print(ksmallest_product(first, 5))
    first = [1, 7, 5, 4, 8, 3, 9, 2, 6, 10]
    print(ksmallest_product2(first, 5))
    first = [1, 7, 5, 4, 8, 3, 9, 2, 6, 10]
    print(ksmallest_product3(first, 5))


"""
120
120
120
"""

def print_larger_half(arr):
    arr.sort()
    size = len(arr)
    for i in range(size//2, size):
        print(arr[i], end=' ')

import heapq
def print_larger_half2(arr):
    size = len(arr)
    heapq.heapify(arr)
    for _ in range(size//2) :
        heapq.heappop(arr)
    print(arr)

"""
Quick select method
"""
def print_larger_half3(array):
    arr = array
    size = len(arr)
    quick_select_util(arr, 0, size-1, size//2)
    for i in range(size//2, size):
        print(arr[i], end=' ')

def test33():
    first = [1, 7, 5, 4, 8, 3, 9, 2, 6, 10]
    print_larger_half(first)
    first = [1, 7, 5, 4, 8, 3, 9, 2, 6, 10]
    print_larger_half2(first)
    first = [1, 7, 5, 4, 8, 3, 9, 2, 6, 10]
    print_larger_half3(first)


"""
6 7 8 9 10 
[6, 7, 9, 10, 8]
6 7 9 8 10
"""

"""
Minimum swaps required to bring all elements less than given value together at the start of array. 

Use quick sort kind of technique by taking two index from both end 
and try to use the given value as key.

Count the number of swaps that is answer.
"""

def min_swaps(arr, val):
    swap_count = 0
    first = 0
    second = len(arr) - 1
    while first < second:
        if arr[first] <= val:
            first += 1
        elif arr[second] > val:
            second -= 1
        else:
            arr[first], arr[second] = arr[second], arr[first]
            swap_count += 1
    return swap_count

def test34():
    arr = [2, 1, 5, 6, 3]
    k = 3
    print(min_swaps(arr, k))
    
    arr1 = [2, 7, 9, 5, 8, 7, 4]
    k = 5
    print(min_swaps(arr1, k))


"""
1
2
"""

"""
Now in the above problem we dont want all the elements in start of array.
We want to find a window for which minimum number of swaps are requered to 
bring all the elements less then the than given value together.
"""
def min_swaps_window(arr, val):
    count = 0
    size = len(arr)
    for i in range(size):
        if arr[i] <= val:
            count += 1

    curr_count = 0
    for i in range(count):
        if arr[i] <= val:
            curr_count += 1
    
    max_count = curr_count
    first = 0
    while first < size - count:
        if arr[first] < val:
            curr_count -= 1
        
        if arr[first + count] < val:
            curr_count += 1

        if curr_count > max_count:
            max_count = curr_count
        first += 1
    return count - max_count

def test35():
    arr = [2, 1, 5, 6, 3]
    k = 3
    print(min_swaps_window(arr, k))
    
    arr1 = [2, 7, 9, 5, 8, 7, 4]
    k = 5
    print(min_swaps_window(arr1, k))


"""
1
2
"""

"""
Given an array of positive integers indicates maximum number of steps jump that can be taken forward.
Write a function to return the minimum number of jumps needed to reach from start of array
to its end.

Use an auxiliary array to store how many steps needed to reach some index.
O(nk)
"""
import sys
def min_jumps(arr):
    size = len(arr)
    jumps = [sys.maxsize]*size
    jumps[0] = 0
 
    for i in range(size):
        steps = arr[i]
        # error checks can be added hear.
        j = i + 1
        while j <= i + steps and j < size:
            jumps[j] = min(jumps[j], jumps[i] + 1)
            j += 1
        #print(jumps)
    return jumps[size-1]

def test36():
    arr = [1, 4, 3, 7, 6, 1, 0, 3, 5, 1, 10]
    print(min_jumps(arr))


"""
3
"""

"""
Given a nearly sorted array, in which an element is at max k units away from its sorted position.

If you use sorting then it will take O(NlogN) time 

There is one algorithm by which it can be done in O(NlogK) time.
You can create a min Heap of size K+1 from first K+1 elements of input array.
pop an elements from heap and store it into output array. 
push next element from array to heap.
repeat this process till all the elements of array are consumed and heap is empty.
In the end you have sorted array.
"""
import heapq

def sortK(arr, k):
    size = len(arr)
    heap = arr[0:k+1]
    heapq.heapify(heap)
    output = []
    for i in range(k+1, size, 1):
        output.append( heapq.heappop(heap))
        heapq.heappush(heap, arr[i])
    
    while len(heap) > 0:
        output.append( heapq.heappop(heap))
    print(output)

def sortK2(arr, k):
    size = len(arr)
    heap = arr[0:k+1]
    heapq.heapify(heap)
    index = 0
    for i in range(k+1, size, 1):
        arr[index] = heapq.heappop(heap)
        index += 1
        heapq.heappush(heap, arr[i])
    
    while len(heap) > 0:
        arr[index] = heapq.heappop(heap)
        index += 1

def test37():
    k = 3
    arr = [1, 5, 4, 10, 50, 9]
    sortK2(arr, k)
    print(arr)


"""
[1, 4, 5, 9, 10, 50]
"""

"""
Find second largest element in an array.
"""
def print_2nd_largest(arr):
    size = len(arr)
    if size < 2:
        print("Invalid Input")
        return

    if arr[0] > arr[1]:
        first = arr[0]
        second = arr[1]
    else :
        second = arr[0]
        first = arr[1]
    
    for i in range(2, size):
        # first is always largest.
        if arr[i] <= first:
            second = first
            first = arr[i]
        elif (arr[i] < second ):
            second = arr[i]

    print("second largest value : ", second)

"""
Find third largest element in an array.
"""
def print_3rd_largest(arr):
    size = len(arr)
    if size < 3:
        print("Invalid Input")
        return

    first = second = third = -9999999

    for i in range(size):
        # first is always largest.
        if arr[i] <= first:
            third = second
            second = first
            first = arr[i]
        elif arr[i] < second :
            third = second
            second = arr[i]
        elif arr[i] < third :
            third = arr[i]

    print("third largest value : ", third)

"""
Find Kth largest element in an array.
Use heap in this case. Min heap.
"""

def rotten_fruit_util(arr, max_column, max_row, curr_column, curr_row, traversed, day):
    # Range check
    if curr_column < 0 or curr_column >= max_column or curr_row < 0 or curr_row >= max_row :
        return
    # Traversable and rot if not already rotten.
    if traversed[curr_column][curr_row] <= day or arr[curr_column][curr_row] == 0:
        return
    # Update rot time.
    traversed[curr_column][curr_row] = day
    # each line corresponding to 4 direction.
    rotten_fruit_util(arr, max_column, max_row, curr_column-1, curr_row, traversed, day+1)
    rotten_fruit_util(arr, max_column, max_row, curr_column+1, curr_row, traversed, day+1)
    rotten_fruit_util(arr, max_column, max_row, curr_column, curr_row+1, traversed, day+1)
    rotten_fruit_util(arr, max_column, max_row, curr_column, curr_row-1, traversed, day+1)

INFI = 99999
def rotten_fruit(arr, max_column, max_row):
    traversed = [[INFI]*max_column for i in range(max_row)]
    for i in range(0, max_column-1, 1):
        for j in range(0, max_row-1, 1):
            if arr[i][j] == 2:
                rotten_fruit_util(arr, max_column, max_row, i, j, traversed, 0)
    max_day = 0
    for i in range(0, max_column, 1):
        for j in range(0, max_row, 1):
            if arr[i][j] == 1 : 
                if traversed[i][j] == INFI :
                    return -1
                if max_day < traversed[i][j]:
                    max_day = traversed[i][j]
    return max_day

def test38():
    arr = [
        [ 1 , 0 , 1, 1 , 0], 
        [ 1 , 1, 1, 1 , 0], 
        [ 0 , 0 , 0, 2 , 1], 
        [ 0 , 2 , 0, 0 , 1], 
        [ 1 , 1 , 0, 0 , 1]]
    print(rotten_fruit(arr, 5, 5))


"""
5
"""
def dist_nearest_fill_util(arr, max_column, max_row, curr_column, curr_row, traversed, dist):
    # Range check
    if curr_column < 0 or  curr_column >= max_column or curr_row < 0 or curr_row >= max_row :
        return
    # Traversable if their is a better distance.
    if traversed[curr_column][curr_row] <= dist :
        return
    # Update distance.
    traversed[curr_column][curr_row] = dist
    # each line corresponding to 4 direction.
    dist_nearest_fill_util(arr, max_column, max_row, curr_column-1, curr_row, traversed, dist+1)
    dist_nearest_fill_util(arr, max_column, max_row, curr_column+1, curr_row, traversed, dist+1)
    dist_nearest_fill_util(arr, max_column, max_row, curr_column, curr_row+1, traversed, dist+1)
    dist_nearest_fill_util(arr, max_column, max_row, curr_column, curr_row-1, traversed, dist+1)

INFI = 99999
def dist_nearest_fill(arr, max_column, max_row):
    traversed = [[INFI]*max_column for i in range(max_row)]
    for i in range(0, max_column, 1):
        for j in range(0, max_row, 1):
            if arr[i][j] == 1:
                dist_nearest_fill_util(arr, max_column, max_row, i, j, traversed, 0)
    print(traversed)

def test39():
    arr = [
        [ 1 , 0 , 1, 1 , 0], 
        [ 1 , 1, 0, 1 , 0], 
        [ 0 , 0 , 0, 0 , 1], 
        [ 0 , 0 , 0, 0 , 1], 
        [ 0 , 0 , 0, 0 , 1]]
    dist_nearest_fill(arr, 5, 5)


"""
[[0, 1, 0, 0, 1], [0, 0, 1, 0, 1], [1, 1, 2, 1, 0], [2, 2, 2, 1, 0], [3, 3, 2, 1, 0]]
"""

def steps_of_knight_util(size, curr_column, curr_row, traversed, dist):
    # Range check
    if curr_column < 0 or curr_column >= size or curr_row < 0 or curr_row >= size :
        return
    # Traversable and rot if not already rotten.
    if traversed[curr_column][curr_row] <= dist :
        return
    # Update rot time.
    traversed[curr_column][curr_row] = dist
    # each line corresponding to 4 direction.
    steps_of_knight_util(size, curr_column-2, curr_row-1, traversed, dist+1)
    steps_of_knight_util(size, curr_column-2, curr_row+1, traversed, dist+1)
    steps_of_knight_util(size, curr_column+2, curr_row-1, traversed, dist+1)
    steps_of_knight_util(size, curr_column+2, curr_row+1, traversed, dist+1)
    steps_of_knight_util(size, curr_column-1, curr_row-2, traversed, dist+1)
    steps_of_knight_util(size, curr_column+1, curr_row-2, traversed, dist+1)
    steps_of_knight_util(size, curr_column-1, curr_row+2, traversed, dist+1)
    steps_of_knight_util(size, curr_column+1, curr_row+2, traversed, dist+1)

INFI = 99999
def steps_of_knight(size, srcX, srcY, dstX, dstY):
    traversed = [[INFI]*size for _ in range(size)]
    steps_of_knight_util(size, srcX - 1, srcY - 1, traversed, 0)
    return traversed[dstX - 1][dstY - 1]

print(steps_of_knight(20,10,10,20,20))

"""
8
"""

def find_largest_island_util(arr, max_column, max_row, curr_column, curr_row, value, traversed) :
    if curr_column < 0 or curr_column >= max_column or curr_row < 0 or curr_row >= max_row :
        return 0
    if traversed[curr_column][curr_row] == 1 or arr[curr_column][curr_row] != value :
        return 0
    traversed[curr_column][curr_row] = 1

    # each call corresponding to 8 direction.
    return 1 + find_largest_island_util(arr, max_column, max_row, curr_column - 1, curr_row - 1, value, traversed) + find_largest_island_util(arr, max_column, max_row, curr_column - 1, curr_row, value, traversed) + find_largest_island_util(arr, max_column, max_row, curr_column - 1, curr_row + 1, value, traversed) + find_largest_island_util(arr, max_column, max_row, curr_column, curr_row - 1, value, traversed) + find_largest_island_util(arr, max_column, max_row, curr_column, curr_row + 1, value, traversed) + find_largest_island_util(arr, max_column, max_row, curr_column + 1, curr_row - 1, value, traversed) + find_largest_island_util(arr, max_column, max_row, curr_column + 1, curr_row, value, traversed) + find_largest_island_util(arr, max_column, max_row, curr_column + 1, curr_row + 1, value, traversed)

def find_largest_island(arr, max_column, max_row):
    max_value = 0
    curr_value = 0
    traversed = [[INFI]*max_column for i in range(max_row)]

    for i in range(max_column):
        for j in range(max_row):
            curr_value = find_largest_island_util(arr, max_column, max_row, i, j, arr[i][j], traversed)
            if curr_value > max_value :
                max_value = curr_value

    return max_value

def test40():
    arr = [[1, 0, 1, 1, 0], [1, 0, 0, 1, 0], [0, 1, 1, 1, 1 ], [ 0, 1, 0, 0, 0], [1, 1, 0, 0, 1]]
    print("Largest Island :" , find_largest_island(arr, 5, 5))


"""
Largest Island : 12
"""

def rotation_max(arr):
    size = len(arr)
    return rotation_max_util(arr, 0, size - 1)

def rotation_max_util(arr, start, end):
    if end <= start:
        return arr[start]

    mid = (start + end) // 2
    if arr[mid] > arr[mid+1]:
        return arr[mid]

    if arr[start] <= arr[mid]: #increasing part.
        return rotation_max_util(arr, mid+1, end)
    else:
        return rotation_max_util(arr, start, mid-1)


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

def count_rotation(arr):
    size = len(arr)
    maxIndex =  find_rotation_max_util(arr, 0, size - 1)
    rotations = (maxIndex + 1) % size
    return rotations

def test41():
    first = [34, 56, 1, 1, 5, 6, 6, 6, 6, 6, 6, 7, 8, 10, 13, 20, 30 ]
    second = [1, 5, 6, 6, 6, 6, 6, 6, 7, 8, 10, 13, 20, 30 ]

    print(rotation_max(first))
    print(find_rotation_max(first))
    print(count_rotation(first))
    print(rotation_max(second))
    print(find_rotation_max(second))
    print(count_rotation(second))


"""
56
1
2
30
13
0
"""




"""
Segregate positive ans negative.
"""
def segregate_positive_negative(arr):
    first = 0
    second = len(arr) - 1
    while first < second:
        if arr[first] <= 0:
            first += 1
        elif arr[second] > 0:
            second -= 1
        else:
            arr[first], arr[second] = arr[second], arr[first]

"""
Segrigate positive and negative , order of appearence should be # maintained.
Just Segregate like insertion sort.
Use an array.
"""
def segregate_positive_negative2(arr):
    index = 0
    size = len(arr)
    arr2 = list(arr)
    for i in range(size) :
        if arr2[i] <= 0:
            arr[index] = arr2[i]
            index += 1
    for i in range(size) :
        if arr2[i] > 0:
            arr[index] = arr2[i]
            index += 1

"""
Segregate even odd.
"""
def segregate_even_odd(arr):
    first = 0
    second = len(arr) - 1
    while first < second:
        if arr[first] % 2 == 0:
            first += 1
        elif arr[second] % 2 != 0:
            second -= 1
        else:
            arr[first], arr[second] = arr[second], arr[first]


"""
Segregate Even number at even index and odd numbers at odd index. 
If possible then return true else return false.
"""
def segregate_even_odd2(arr):
    odd = 1
    even = 0
    size = len(arr)
    while odd <= size or even <= size:
        if arr[even] % 2 == 0:
            even += 2
        elif arr[odd] % 2 != 0:
            odd += 2
        else:
            arr[odd], arr[even] = arr[even], arr[odd]
    if odd - even > 1:
        return False
    else :
        return True

def smallest_sub_grater_sum(arr, x):
    size = len(arr)
    currSum = 0
    minLen = size + 1
    start = 0
    end = 0
    while end < size:
        if (currSum <= x and end < size):
            currSum += arr[end]
            end += 1
 
        if (currSum > x and start < size):
            if minLen > (end - start):
                minLen = end - start
            currSum -= arr[start]
            start += 1
    return minLen 

def test42():
    arr = [1, 4, 45, 6, 10, 19] 
    x = 51
    print(smallest_sub_grater_sum(arr, x)) 


"""
3
"""

"""
given two sorted array. You need to print all possible sorted array by picking alternate elements from both the array.
The first element of the arrays should be from the first array. 
and last element of the output arrays should be from the second array.
"""
def sorted_array_util(first, first_size, first_index, second, second_size, second_index,arr, index, flag):
    # print arr # all alternate sorted array. 
    if flag == 0:
        for i in range(first_index, first_size):
            # first element should be from first.
            if (len(arr) == 0 or first[i] > arr[-1]):
                arr.append(first[i])
                sorted_array_util(first, first_size, i+1, second, second_size, second_index,arr, index+1, not flag)
                arr.pop()

    if flag == 1:
        for i in range(second_index, second_size):
            if second[i] > arr[-1]:
                arr.append(second[i])
                print(arr) # last element should be from second.
                sorted_array_util(first, first_size, first_index, second, second_size, i+1,arr, index+1, not flag)
                arr.pop()

def sorted_array(first, second):
    first_size = len(first)
    second_size = len(second)
    arr=[]
    sorted_array_util(first, first_size, 0, second, second_size, 0, arr, 0, 0)

def test43():
    first = [1, 5, 10]
    second = [2, 4, 12]
    sorted_array(first, second)


"""
[1, 2]
[1, 2, 5, 12]
[1, 2, 10, 12]
[1, 4]
[1, 4, 5, 12]
[1, 4, 10, 12]
[1, 12]
[5, 12]
[10, 12]
"""


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def wave_array(arr):
    size = len(arr)
    arr.sort()
    # Swap adjacent elements in array
    for i in range(0, size - 1, 2):
        swap(arr, i, i+1)


def wave_array2(arr):
    size = len(arr)
    
    # Odd elements are lesser then even elements.
    for i in range(1, size , 2):
        if (i - 1) >= 0 and arr[i] > arr[i - 1]:
            swap(arr, i, i-1)
        if (i + 1) < size and arr[i] > arr[i + 1]:
            swap(arr, i, i+1)

def test44():
    arr = [8, 1, 2, 3, 4, 5, 6, 4, 2]
    wave_array(arr)
    print(arr)
    arr = [8, 1, 2, 3, 4, 5, 6, 4, 2]
    wave_array2(arr)
    print(arr)


"""
[2, 1, 3, 2, 4, 4, 6, 5, 8]
[8, 1, 3, 2, 5, 4, 6, 2, 4]
"""

def zero_replace(arr):
    prev = 0
    curr = 0
    size = len(arr)
    index = -1
    maximum = 0
    zero_index = -1
    for i in range(size):
        if arr[i] == 1:
            curr += 1
        elif arr[i] == 0:
            if maximum < (prev + curr + 1):
                maximum = prev + curr + 1
                if prev > 0:
                    index = zero_index
                else:
                    index = i
                zero_index = i
            prev = curr
            curr = 0
    if maximum < (prev + curr + 1):
        maximum = prev + curr + 1
        index = zero_index
    #print(index , maximum)
    return maximum

def test45():
    arr = [1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1]
    print(zero_replace(arr))


"""
6
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
test25()
test26()
test27()
test28()
test29()
test30()
test31()
test32()
test33()
test34()
test35()
test36()
test37()
test38()
test39()
test40()
test41()
test42()
test43()
test44()
test45()