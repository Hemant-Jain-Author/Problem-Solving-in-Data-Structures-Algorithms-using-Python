"""
given two sorted array. You need to print all possible sorted array by picking alternate elements from both the array.
The first elemetn of the arrays should be from the first array. 
and last element of the output arrays should be from the second array.
"""
def sortedArrayUtil(first, fSize, fIndex, second, sSize, sIndex,arr, index, flag):
    # print arr # all alternate sorted array. 
    if flag == 0:
        for i in range(fIndex, fSize):
            # first element should be from first.
            if (len(arr) == 0 or first[i] > arr[-1]):
                arr.append(first[i])
                sortedArrayUtil(first, fSize, i+1, second, sSize, sIndex,arr, index+1, not flag)
                arr.pop()

    if flag == 1:
        for i in range(sIndex, sSize):
            if second[i] > arr[-1]:
                arr.append(second[i])
                print(arr) # last element should be from second.
                sortedArrayUtil(first, fSize, fIndex, second, sSize, i+1,arr, index+1, not flag)
                arr.pop()

def sortedArray(first, second):
    fSize = len(first)
    sSize = len(second)
    arr=[]
    sortedArrayUtil(first, fSize, 0, second, sSize, 0, arr, 0, 0)

first = [1, 5, 10]
second = [2, 4, 12]
sortedArray(first, second)