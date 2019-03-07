"""
Given an array arr[], find maximum distance of index j and i, such that arr[j] > arr[i]

first solution : Brute force, for each index call it i find index j such that arr[j] > arr[i]
We will need two loops one to select index i and another to traverse index i+1 to size of array.


always keep decreasing array index. 

Second solution is done using preprocessing and creating two auxilarry arrays. 
"""
def ArrayIndexMaxDiff(arr):
    size = len(arr)
    maxDiff = -1
    for i in range(size):
        j = size - 1
        while(j > i):
            if arr[j] > arr[i] :
                maxDiff = max(maxDiff, j-i)
                break
            j -= 1
    return maxDiff


def ArrayIndexMaxDiff2(arr):
    size = len(arr)
    leftMin = [0]*size
    rightMax = [0]*size
    leftMin[0] = arr[0]
    for i in range(1, size, 1):
        if leftMin[i-1] < arr[i]:
            leftMin[i] = leftMin[i-1]
        else:
            leftMin[i] = arr[i] 

    rightMax[size - 1] = arr[size - 1]
    for i in reversed(list(range(size - 1))):
        if rightMax[i+1] > arr[i]:
            rightMax[i] = rightMax[i+1]
        else:
            rightMax[i] = arr[i] 
    i = 0
    j = 0
    maxDiff = -1
    while j < size and i < size :
        if leftMin[i] < rightMax[j] : 
            maxDiff = max(maxDiff, j-i)
            j = j + 1
        else:
            i = i+1
    return maxDiff

def ArrayIndexMaxDiff3(arr):
    size = len(arr)
    leftMin = []
    rightMax = []
    leftMin.append(0)
    for i in range(1, size, 1):
        if arr[leftMin[-1]] > arr[i]:
            leftMin.append(i)

    rightMax.append(size - 1)
    for i in reversed(list(range(size - 1))):
        if arr[rightMax[-1]] < arr[i]:
            rightMax.append(i)

    i = 0
    j = len(rightMax) - 1
    maxDiff = -1
    firstSize = len(leftMin)

    while i < firstSize and j >= 0 :
        if arr[leftMin[i]] < arr[rightMax[j]] :
            maxDiff = max(maxDiff, rightMax[j]-leftMin[i])
            j -= 1
        else:
            i += 1
    return maxDiff


arr = [33, 9, 10, 3, 2, 60, 30, 33, 1]
print(ArrayIndexMaxDiff(arr))
arr = [33, 9, 10, 3, 2, 60, 30, 33, 1]
print(ArrayIndexMaxDiff2(arr))
arr = [33, 9, 10, 3, 2, 60, 30, 33, 1]
print(ArrayIndexMaxDiff3(arr))

arr = [9, 2, 3, 4, 5, 6, 7, 8, 1]
print(ArrayIndexMaxDiff(arr))
arr = [9, 2, 3, 4, 5, 6, 7, 8, 1]
print(ArrayIndexMaxDiff2(arr))
arr = [9, 2, 3, 4, 5, 6, 7, 8, 1]
print(ArrayIndexMaxDiff3(arr))