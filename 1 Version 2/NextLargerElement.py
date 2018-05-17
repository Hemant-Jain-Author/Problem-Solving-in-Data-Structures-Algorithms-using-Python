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
        if stk.isEmpty() == True or arr[stk.top()] > curr :
            stk.push(i)
            continue
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
        # stack always have values in increasing order.
        if stk.isEmpty() == True or arr[stk.top()] <= curr :
            stk.push(i)
            continue
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
nextLargerElement2(arr)
nextLargerElement3(arr)
nextSmallerElement(arr)
nextSmallerElement3(arr)