"""
Start from index+1 if you updating index in original array. Keep adding this value 
for next node till you reach outside range of tree
"""
def updateUtil(binaryIndexedTree, val, index):
    size = len(binaryIndexedTree)
    while index < size:
        binaryIndexedTree[index] += val
        index = getNext(index)

def update(binaryIndexedTree, diff, index):
    updateUtil(binaryIndexedTree, diff, index+1)

"""
Start from index+1 if you want prefix sum 0 to index. Keep adding value
till you reach 0
"""
def getSum(binaryIndexedTree, index):
    index = index + 1
    sum = 0
    while index > 0 :
        sum += binaryIndexedTree[index]
        index = getParent(index)
    return sum

def getRangeSum(binaryIndexedTree, first, second):
    index = first
    firstSum = 0
    while index > 0 :
        firstSum += binaryIndexedTree[index]
        index = getParent(index)
        
    index = second + 1
    secondSum = 0
    while index > 0 :
        secondSum += binaryIndexedTree[index]
        index = getParent(index)
    return (secondSum - firstSum)

"""
Creating tree is like updating Fenwick tree for every value in array
"""
def createTree(input):
    size = len(input)
    binaryIndexedTree = [0]*(size+1)
    for i in range(size) :
        updateUtil(binaryIndexedTree, input[i], i+1)
    return binaryIndexedTree

"""
To get parent
1) Boolean AND (2's complement of index) with index
2) Subtract the result from index
"""
def getParent(index):
    return index - (index & -index)

"""
To get next
1) Boolean AND (2's complement of index) with index
2) Add the result to index
"""
def getNext(index):
    return index + (index & -index)

input = [1, 2, 3, 4, 5, 6, 7, 8, 9]
binaryIndexedTree = createTree(input)
for i in range(len(input)):
    print(getSum(binaryIndexedTree, i))
    print(getRangeSum(binaryIndexedTree, 0, i))

print(getRangeSum(binaryIndexedTree, 8, 8))