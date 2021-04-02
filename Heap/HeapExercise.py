def is_max_heap2(arr):
    size = len(arr)
    parent = (size//2 - 1)
    while parent >= 0:
        left_child = parent*2 + 1
        right_child = parent*2 + 2
        # heap property check.
        # right_child can overflow.
        if ( arr[parent] < arr[left_child] ) or ( right_child < size - 1 and arr[parent] < arr[right_child]):
            return False
        parent -= 1
    return True

def is_max_heap(arr):
    size = len(arr)
    parent = 0
    #last element index size - 1
    for parent in range(size//2 + 1):
        left_child = parent*2 + 1
        right_child = parent*2 + 2
        # heap property check.
        if ((left_child < size) and (arr[parent] < arr[left_child])) or ((right_child < size) and (arr[parent] < arr[right_child])) :
            return False
    return True

def is_min_heap(arr):
    size = len(arr)
    parent = 0
    #last element index size - 1
    for parent in range(size//2 + 1):
        left_child = parent*2 + 1
        right_child = parent*2 + 2
        # heap property check.
        if ((left_child < size) and (arr[parent] > arr[left_child])) or ((right_child < size) and (arr[parent] > arr[right_child])) :
            return False
    return True

def is_min_heap2(arr):
	size = len(arr)
	parent = 0
	#last element index size - 1
	while(parent <= size//2):
		if 2*parent + 1 < size:
			if arr[parent] > arr[2*parent + 1]:
				return False
		if 2*parent + 2 < size:
			if arr[parent] > arr[2*parent +2]:
				return False
		parent += 1
	return True

def test1():
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    print (is_min_heap(arr))
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    print (is_min_heap2(arr))
    arr = [8, 7, 6, 5, 4, 3, 2, 1]
    print (is_max_heap(arr))
    arr = [8, 7, 6, 5, 4, 3, 2, 1]
    print (is_max_heap2(arr))

# test1()

"""
True
True
True
True
"""

"""
Given an array of size n containing positive integers. 
Absolute of difference between values of array is calculated.
We are asked to print the kth smallest absolute difference.

for array [1, 2, 3, 4]
absolute differences are [1,2,3,1,2,1]
after sorting [1,1,1,2,2,3]
K = 5 is 2
K = 3 is 1
"""

"""
Most simple approach is to find all the possible diffrences and store them in an array. 
Then sort the array to find first k sorted values.
total = n(n-1)/2 entries of differences. 
Then sorting will take n2log(n2) 
So final time complexity. n2logn
space complexity will be n2
"""
def kth_abs_diff(arr, k):
    size = len(arr)
    arr.sort()
    diff = []
    for i in range(size-1):
        for j in range(i+1,size, 1):
            diff.append(abs(arr[i] - arr[j]))

    diff.sort()
    return diff[k-1]

"""
Efficient solution is to use a heap. Sort the given array in nlogn time.
Find all the consequitive values abs difference and store it in a heap in O(n) time.
With each value we will store is corresponding indices call them src and dst.
We pop smallest difference values from heap one by one. 
We read its src and dst of popped value and insert new diffrence with src, dst+1 
if valid.

Since the array is sorted so difference of array value at indices src, dst is always 
less then difference of array values at indices src,dst+1.

O(nlogn) for sorting.
O(n) for heap creation.
Klogn for K deletion and insertion.
Over all complexity will be O(nlogn)
"""
import heapq

def kth_abs_diff2(arr, k):
    size = len(arr)
    arr.sort()
    hp = []
    value = 0
    
    for i in range(size-1):
        hp.append((abs(arr[i] - arr[i+1]), i, i+1))
    heapq.heapify(hp)

    for i in range(k):
        tp = heapq.heappop(hp)
        value = tp[0]
        src = tp[1]
        dst = tp[2]
        if dst + 1 < size :
            heapq.heappush(hp, (abs(arr[src] - arr[dst+1]), src, dst+1))
    return value

def test2():
    arr = [1, 2, 3, 4]
    print(kth_abs_diff(arr, 5))

    arr = [1, 2, 3, 4]
    print(kth_abs_diff2(arr, 5))

# test2()
"""
2
2
"""

def k_smallest_product(arr, k):
    size = len(arr)
    arr.sort()
    
    product = 1
    for i in range(k):
        product *= arr[i]
    return product


def k_smallest_product2(arr, k) :
    size = len(arr)
    hp = []    
    for i in range(size):
        hp.append(arr[i])
    heapq.heapify(hp)
    product = 1
    i = 0
    while (i < size and i < k) :
        product *= heapq.heappop(hp)      
        i += 1
    return product

def swap(arr, first, second):
    arr[first], arr[second] = arr[second], arr[first]

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

def k_smallest_product3(arr, k) :
    size = len(arr)
    quick_select_util(arr, 0, size - 1, k)
    product = 1
    for i in range(k):
        product *= arr[i]
    return product

def test3():
    arr = [8, 7, 6, 5, 7, 5, 2, 1]
    print("Kth Smallest product::", k_smallest_product(arr, 3))
    arr2 = [8, 7, 6, 5, 7, 5, 2, 1]
    print("Kth Smallest product::", k_smallest_product2(arr2, 3))
    arr3 = [8, 7, 6, 5, 7, 5, 2, 1] 
    print("Kth Smallest product::", k_smallest_product3(arr3, 3))

# test3()

"""
Kth Smallest product:: 10
Kth Smallest product:: 10
Kth Smallest product:: 10
"""

def print_larger_half(arr) :
    size = len(arr)
    arr.sort()
    i = size // 2
    while i < size:
        print(arr[i], end=" ")
        i += 1
    print()

def print_larger_half2(arr) :
    size = len(arr)
    hp = []    
    for i in range(size):
        hp.append(arr[i])
    heapq.heapify(hp)

    for i in range(size // 2):
        heapq.heappop(hp)
    print(hp)


def print_larger_half3(arr):
    size = len(arr)
    quick_select_util(arr, 0, size - 1, size // 2)
    i = size // 2
    while i < size :
        print(arr[i], end=" ")
        i += 1
    print()

def test4():
    arr = [8, 7, 6, 5, 7, 5, 2, 1]
    print_larger_half(arr)
    arr2 = [8, 7, 6, 5, 7, 5, 2, 1]
    print_larger_half2(arr2)
    arr3 = [8, 7, 6, 5, 7, 5, 2, 1]
    print_larger_half3(arr3)

# test4()

"""
6 7 7 8 
[6, 7, 8, 7]
6 7 7 8 
"""

import heapq

def kth_largest_stream(k):
    hp = []
    size = 0
    while 1:
        data = eval(input("Enter data: ")) 
        size = len(hp)
        if size < k - 1:
            hp.append(data)
        else:
            if size == k - 1:
                hp.append(data)
                heapq.heapify(hp)
            elif hp[0] < data :
                heapq1.heappush(hp, data)
                heapq.heappop(hp)
            print(hp)
            print("Kth larges element is :: ", hp[0])
        size += 1

# kth_largest_stream(3)

"""

"""


"""
Find kth smallest elements in an unsorted array.
"""
def kth_smallest(arr, k):
    arr.sort()
    return arr[k-1]

import heapq

def kth_smallest2(arr, k):
    size = len(arr)
    heapq.heapify(arr)
    i = 0
    value = 0
    while i < size and i < k:
        value = heapq.heappop(arr)
        i += 1
    return value

"""
Quick select method
"""
def quick_select(array, k):
    arr = array
    size = len(arr)
    quick_select_util(arr, 0, size-1, k)
    return arr[k-1]

def test5():
    first = [1, 7, 5, 4, 8, 3, 9, 2, 6, 10]
    print(kth_smallest(first, 5))
    first = [1, 7, 5, 4, 8, 3, 9, 2, 6, 10]
    print(kth_smallest2(first, 5))
    first = [1, 7, 5, 4, 8, 3, 9, 2, 6, 10]
    print(quick_select(first, 5))

# test5()

"""
5
5
5
"""

import math

def chota_bhim(cup):
    cups = cup
    size = len(cups)
    time = 60
    cups.sort(reverse=True)
    value = 0
    while time > 0:
        #print(cups)
        value += cups[0]
        cups[0] = math.ceil(cups[0]/2.0)
        index = 0
        temp = cups[0]
        while index < size-1 and temp < cups[index + 1]:
            cups[index] = cups[index + 1]
            index += 1
        cups[index] = temp

        #cups.sort(reverse=True)
        time -= 1
    print(value)

def chota_bhim2(cups):
    time = 60
    size = len(cups)
    cups.sort(reverse=True)
    value = 0
    while time > 0:
        value += cups[0]
        cups[0] = math.ceil(cups[0]/2.0)
        i = 0
        # Insert into proper location.
        while i < size-1 :
            if(cups[i] > cups[i+1]):
                break
            temp = cups[i]
            cups[i] = cups[i+1]
            cups[i+1] = temp
            i += 1
        time -= 1
    print(value)

"""
This performance can be further improved by using a heap to store the cups. 
Each deletion will take logK time and each insertion will again take logK time 
so the final time complexity will be N.LogK
"""
def test6():
    cups = [2,1,7,4,2]
    chota_bhim(cups)
    cups = [2,1,7,4,2]
    chota_bhim2(cups)

test6()

"""
76
76
"""

def join_rope(ropes):
    ropes.sort(reverse=True)
    total = 0
    value = 0
    while len(ropes) >= 2:
        value = ropes.pop() + ropes.pop()
        ropes.append(value)
        total += value 
        index = len(ropes) - 1
        temp = ropes[-1]
        while index > 0 and ropes[index] < ropes[index - 1]:
            ropes[index] = ropes[index - 1]
            index -= 1
        ropes[index] = temp
        #ropes.sort(reverse=True)
    print(total)

"""
Performance of join_rope can be improved by using insertion into proper possition approach.
so by doing this the complexity of the algorithm will O(n2)

Performance can be improved by using a heap to store values. Deletion and Insertion will take
O(LogN) time and finally the whole algorithm will be over in O(NlogN)
"""
import heapq

def join_rope2(ropes):
    heapq.heapify(ropes)
    total = 0
    value = 0
    while len(ropes) > 1:
        value = heapq.heappop(ropes)
        value += heapq.heappop(ropes)
        heapq.heappush(ropes, value)
        total += value
    print(total)

def test7():
    ropes = [4, 3, 2, 6]
    join_rope(ropes)
    ropes = [4, 3, 2, 6]
    join_rope2(ropes)

test7()

"""
29
29
"""
