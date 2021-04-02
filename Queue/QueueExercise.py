"""
Their are N number of petrol pumps. Each petrol pump have 
some limited amount of petrol and they also their distance from each other is provided.
Find if their is a circular tour possible to visit all the petrol pumps.
"""
import sys
from collections import deque

def circular_tour(arr, n):
    que = deque([])
    next_pump = 0
    count = 0
    petrol = 0

    while len(que) != n:
        while petrol >= 0 and len(que) != n :
            que.append(next_pump)
            petrol += (arr[next_pump][0] - arr[next_pump][1])
            next_pump = (next_pump + 1) % n
            
        while petrol < 0 and len(que) > 0:
            prev_pump = que.popleft()
            petrol -= (arr[prev_pump][0] - arr[prev_pump][1])
        
        count += 1
        if count == n:
            return -1

    if petrol >= 0:
        return que.popleft()
    else:
        return -1


def main1():
    tour = [[8, 6], 
    [1, 4], 
    [7, 6]]
    print(circular_tour(tour, 3))

"""
2
"""

def convert_XY(src, dst):
    que = deque([])
    visited = {}
    que.append((src, 0))
    while len(que) != 0:
        node = que.popleft()
        visited[node[0]] = 1
        value = node[0]
        steps = node[1]
        if value == dst:
            return steps
        if value < dst and (value*2) not in visited:
            que.append((value*2, steps+1))
        if value > 0 and (value - 1) not in visited:
            que.append((value-1, steps+1))
    return -1

def main2():   
    print("3 to ", 4 ," : ", convert_XY(3, 4))
    print("3 to ", 5 ," : ", convert_XY(3, 5))
    print("3 to ", 6 ," : ", convert_XY(3, 6))

"""
3 to  4  :  2
3 to  5  :  2
3 to  6  :  1
"""

# Given an array of integer, find maximum in all the sliding windows of length.k.

def max_sliding_windows(arr, k):
    size = len(arr)
    que = deque()
    for i in range(size):
        # Remove out of range elements
        if que and que[0] <= i - k:
            que.popleft()
        # Remove smaller values at left.
        while que and arr[que[-1]] <= arr[i] :
            que.pop()
        que.append(i)
        # window of size k
        if i >= (k - 1):
            print(arr[que[0]], end=" ")

def main3():
    arr = [11, 2, 75, 92, 59, 90, 55]
    k = 3
    max_sliding_windows(arr, k)

"""
75 92 92 92 90
"""

def first_neg_sliding_windows(arr, k):
    size = len(arr)
    que = deque()
    for i in range(size):
        # Remove out of range elements
        if que and que[0] <= i - k:
            que.popleft()
        if arr[i] < 0:
            que.append(i)
        # window of size k
        if i >= (k - 1) :
            if len(que) > 0:
                print(arr[que[0]], end=" ")
            else:
                print("NAN", end=" ") 

def main4():
    arr3 = [13, -2, -6, 10, -14, 50, 14, 21]
    first_neg_sliding_windows(arr3, 3)

"""
-2 -2 -6 -14 -14 NAN
"""

def minofmax_sliding_windows(arr, k):
    size = len(arr)
    que = deque()
    min_val = 999999
    for i in range(size):
        # Remove out of range elements
        if que and que[0] <= i - k:
            que.popleft()
        # Remove smaller values at left.
        while que and arr[que[-1]] <= arr[i] :
            que.pop()
        que.append(i)
        # window of size k
        if i >= (k - 1) and min_val > arr[que[0]] :
            min_val = arr[que[0]]
    print("Min of max is : ", min_val)

def main5():
    arr = [11, 2, 75, 92, 59, 90, 55]
    minofmax_sliding_windows(arr, 3)

"""
Min of max is :  75
"""

def maxofmin_sliding_windows(arr, k):
    size = len(arr)
    que = deque()
    max_val = -999999
    for i in range(size):
        # Remove out of range elements
        if que and que[0] <= i - k:
            que.popleft()
        # Remove smaller values at left.
        while que and arr[que[-1]] >= arr[i] :
            que.pop()
        que.append(i)
        # window of size k
        if i >= (k - 1) and max_val < arr[que[0]] :
            max_val = arr[que[0]]
    print("Max of min is : ", max_val)


def main6():
    arr = [10, 20, 30, 50, 10, 70, 30]
    maxofmin_sliding_windows(arr, 3)

"""     
Max of min is :  20
"""

main1()
main2()
main3()
main4()
main5()
main6()




