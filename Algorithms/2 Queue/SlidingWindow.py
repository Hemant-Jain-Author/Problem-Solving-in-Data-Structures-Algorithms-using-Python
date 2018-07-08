# Given an array of integer, 
# find maximum in all the sliding windows of length.k.

from collections import deque

def maxSlidingWindows(arr, k):
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
            print(arr[que[0]])


def firstNegSlidingWindows(arr, k):
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
                print(arr[que[0]])
            else:
                print("NAN") 



def minOfMaxSlidingWindows(arr, k):
    size = len(arr)
    que = deque()
    minVal = 999999
    for i in range(size):
        # Remove out of range elements
        if que and que[0] <= i - k:
            que.popleft()
        # Remove smaller values at left.
        while que and arr[que[-1]] <= arr[i] :
            que.pop()
        que.append(i)
        # window of size k
        if i >= (k - 1) and minVal > arr[que[0]] :
            minVal = arr[que[0]]
    print("Min of max is : ", minVal)

def maxOfMinSlidingWindows(arr, k):
    size = len(arr)
    que = deque()
    maxVal = -999999
    for i in range(size):
        # Remove out of range elements
        if que and que[0] <= i - k:
            que.popleft()
        # Remove smaller values at left.
        while que and arr[que[-1]] >= arr[i] :
            que.pop()
        que.append(i)
        # window of size k
        if i >= (k - 1) and maxVal < arr[que[0]] :
            maxVal = arr[que[0]]
    print("Max of min is : ", maxVal)


arr = [11,2,75,92,59,90,55]
k = 3
maxSlidingWindows(arr, k)
minOfMaxSlidingWindows(arr, k)

arr2 = [10, 20, 30, 50, 10, 70, 30]
for i in range(1,8):
    maxOfMinSlidingWindows(arr2, i)
    
arr3 = [13, -2, -6, 10, -14, 50, 14, 21]
firstNegSlidingWindows(arr3, 3)
