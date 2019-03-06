"""
Given an array of N non-negative integers. Each element of array represents a bar of histogram. 
Considering that each bar is one unit wide. You need to find how much water can be accomodate in 
the structure.

For example : [4, 0, 1, 5] will contain 7 units of water.

   B
BwwB
BwwB
BwwB
BwBB

"""
def RainWater(arr):
    size = len(arr)
    leftHigh = [0]*size
    leftHigh[0] = max = arr[0]
    for i in range(1,size):
        if max < arr[i]:
            max = arr[i]
        leftHigh[i] = max
    
    rightHigh = [0]*size
    rightHigh[size - 1] = max = arr[size - 1]
    for i in reversed(range(size-1)):
        if max < arr[i]:
            max = arr[i]
        rightHigh[i] = max
    water = 0
    for i in range(size):
        water += min(leftHigh[i], rightHigh[i]) - arr[i]
    print water


def RainWater2(arr):
    size = len(arr)
    water = 0
    leftMax, rightMax = 0, 0
    left = 0
    right = size-1
      
    while(left <= right): 
        if(arr[left] < arr[right]):
            if(arr[left] > leftMax):
                leftMax = arr[left]
            else:
                water += leftMax - arr[left]
            left += 1
        else:
            if(arr[right] > rightMax):
                rightMax = arr[right]
            else:
                water += rightMax - arr[right]
            right -= 1
    print water

arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
RainWater(arr)
RainWater2(arr)