# Function to print next Larger element of each element of array.
def nextLargerElement(arr):
    size = len(arr)
    output = []
    for i in range(0, size, 1):
        next = -1
        for j in range(i+1, size, 1):
            if arr[i] < arr[j]:
                next = arr[j]
                break
        output.append(next)
    print(output)

class Stack(object):
    def __init__(self):
        self.data = []     

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return (len(self.data) == 0)

    def push(self, value):
        self.data.append(value)

    def top(self):
        if self.isEmpty():
            raise RuntimeError("StackEmptyException")
        return self.data[len(self.data) - 1]

    def pop(self):
        if self.isEmpty():
            raise RuntimeError("StackEmptyException")
        return self.data.pop()

def nextLargerElement2(arr):
    size = len(arr)
    stk = Stack()
    output = [-1]*size
    stk.push(arr[size - 1])
    output[size - 1] = -1
    i = size -2
    while i >= 0:
        while stk.isEmpty() == False :
            top = stk.top()
            if top <= arr[i] :
                stk.pop()
            else :
                output[i] = top
                break
        
        if stk.isEmpty() :
            output[i] = -1
        stk.push(arr[i])
        i -= 1
    print(output)

def nextLargerElement3(arr):
    size = len(arr)
    stk = Stack()
    output = [-1]*size
    for i in range(size) :
        curr = arr[i]
        # stack always have values in decreasing order.
        while stk.isEmpty() == False and arr[stk.top()] <= curr:
            index = stk.pop()
            output[index] = curr
        stk.push(i)
    
    # index which dont have any next Larger.
    while stk.isEmpty() == False :
        index = stk.pop()
        output[index] = -1
        
    print(output)

def nextSmallerElement(arr):
    size = len(arr)
    stk = Stack()
    output = [-1]*size
    stk.push(arr[size - 1])
    output[size - 1] = -1
    i = size -2
    while i >= 0:
        while stk.isEmpty() == False :
            top = stk.top()
            if top >= arr[i] :
                stk.pop()
            else :
                output[i] = top
                break
        
        if stk.isEmpty() :
            output[i] = -1
        stk.push(arr[i])
        i -= 1
    print(output)

def nextSmallerElement3(arr):
    size = len(arr)
    stk = Stack()
    output = [-1]*size
    for i in range(size) :
        curr = arr[i]
        while stk.isEmpty() == False and arr[stk.top()] > curr:
            index = stk.pop()
            output[index] = curr
        stk.push(i)
    # index which dont have any next Smaller.
    while stk.isEmpty() == False :
        index = stk.pop()
        output[index] = -1
    print(output)

# Testing code

arr = [13,21,3,6,20,3]
print(arr)
nextLargerElement(arr)
# nextLargerElement2(arr)
nextLargerElement3(arr)
"""nextSmallerElement(arr)
nextSmallerElement3(arr)
"""

def nextLargerElementCircular(arr):
    size = len(arr)
    stk = Stack()
    output = [-1]*size
    for i in range(2*size - 1) :
        curr = arr[i % size]
        # stack always have values in decreasing order.
        while stk.isEmpty() == False and arr[stk.top()] <= curr:
            index = stk.pop()
            output[index] = curr
        stk.push(i % size)
    
    # index which dont have any next Larger.
    while stk.isEmpty() == False :
        index = stk.pop()
        output[index] = -1
        
    print(output)


arr = [6, 3, 9, 8, 10, 2, 1, 15, 7]
print(arr)
nextLargerElementCircular(arr)

"""
Given an array you need to find smalles larger element for each element.
"""
import sys
def smallestLargerElementArray(arr):
    size = len(arr)
    output = []
    for i in range(size): 
        minDiff = sys.maxsize
        value = -1
        for j in range(size):
            if arr[i] < arr[j] and (arr[j] - arr[i] ) < minDiff :
                minDiff = arr[j] - arr[i]
                value = arr[j]
        output.append(value)
    print(output)

def smallestLargerElementArray2(arr):
    size = len(arr)
    output = [-1]*size
    aux = []
    for i in range(size) :
        aux.append((arr[i], i))
    aux.sort()
    
    for i in range(size-1) :
        output[aux[i][1]] = aux[i+1][0]
    output[aux[size - 1][1]] = -1
    print(output)

"""
arr = [6, 3, 9, 8, 10, 2, 1, 15, 7]
smallestLargerElementArray(arr)
smallestLargerElementArray2(arr)
"""


"""
Given an array of integers. Find leaders in this array. 
A leader is value which is grater then all the values at the right of it.
Hint:= Next largest value stack need to be output in this problem.
"""
def FindLeaders(arr):
    size = len(arr)
    stk = []
    for i in range(size) :
        curr = arr[i]
        # stack always have values in decreasing order.
        if len(stk) == 0 or stk[-1] > curr :
            stk.append(arr[i])
            continue
        while len(stk) != 0 and stk[-1] <= curr:
            stk.pop()
        stk.append(arr[i])
    print(stk)

import sys
def FindLeaders2(arr):
    size = len(arr)
    largest = -sys.maxsize
    i = size -1
    output = []
    while i >= 0 :
        curr = arr[i]
        if largest < curr:
            largest = curr
            output.append(curr)
        i -= 1
    print(output)

"""
arr = [16, 17, 4, 3, 5, 2]
FindLeaders(arr)
FindLeaders2(arr)
"""