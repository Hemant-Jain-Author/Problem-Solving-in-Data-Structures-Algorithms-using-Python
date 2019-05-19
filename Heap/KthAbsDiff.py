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
def kthAbsDiff(arr, k):
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

def kthAbsDiff2(arr, k):
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

arr = [1, 2, 3, 4]
print(kthAbsDiff(arr, 5))

arr = [1, 2, 3, 4]
print(kthAbsDiff2(arr, 5))

def KSmallestProduct(arr, k):
    size = len(arr)
    arr.sort()
    
    product = 1
    for i in range(k):
        product *= arr[i]
    return product


def KSmallestProduct2(arr, k) :
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


def KSmallestProduct3(arr, k) :
    size = len(arr)
    QuickSelectUtil(arr, 0, size - 1, k)
    product = 1
    for i in range(k):
        product *= arr[i]
    return product

arr = [ 8, 7, 6, 5, 7, 5, 2, 1 ]
print("Kth Smallest product:: " , KSmallestProduct(arr, 3))
arr2 = [8, 7, 6, 5, 7, 5, 2, 1]
print("Kth Smallest product:: " , KSmallestProduct2(arr2, 3))
# arr3 = [ 8, 7, 6, 5, 7, 5, 2, 1] 
# print("Kth Smallest product:: " , KSmallestProduct3(arr3, 3))


def PrintLargerHalf(arr) :
    size = len(arr)
    arr.sort()
    i = size // 2
    while i < size:
        print(arr[i], end=" ")
        i += 1

def PrintLargerHalf2(arr) :
    size = len(arr)
    hp = []    
    for i in range(size):
        hp.append(arr[i])
    heapq.heapify(hp)

    for i in range(size // 2):
        heapq.heappop(hp)
    print(hp)


def PrintLargerHalf3(arr):
    size = len(arr)
    QuickSelectUtil(arr, 0, size - 1, size // 2)
    i = size // 2
    while i < size :
        print(arr[i])
        i += 1

arr = [8, 7, 6, 5, 7, 5, 2, 1]
PrintLargerHalf(arr)
arr2 = [8, 7, 6, 5, 7, 5, 2, 1]
PrintLargerHalf2(arr2)
# arr3 = [8, 7, 6, 5, 7, 5, 2, 1]
# PrintLargerHalf3(arr3, 8)

