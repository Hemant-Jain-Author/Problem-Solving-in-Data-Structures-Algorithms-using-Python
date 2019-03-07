def findTriplet(arr, value):
    size = len(arr) 
    for i in range(size-2):
        for j in range(i+1, size-1): 
            for k in range(j + 1, size):
                if arr[i] + arr[j] + arr[k] == value:
                    print((arr[i], arr[j], arr[k]))

def findTriplet2(arr, value):
    size = len(arr)
    arr.sort()
    for i in range(size-2):
        start = i+1
        stop = size-1

        while start < stop:
            if arr[i] + arr[start] + arr[stop] == value:
                print((arr[i], arr[start], arr[stop]))
                start += 1
                stop -= 1
            elif arr[i] + arr[start] + arr[stop] > value:
                stop -= 1
            else:
                start += 1


arr = [1, 5, 15, 6, 9, 8]
print(arr)
findTriplet(arr, 22)
print(arr)
findTriplet2(arr, 22)

def ZeroSumTriplets(arr):
    size = len(arr) 
    for i in range(size-2):
        for j in range(i+1, size-1): 
            for k in range(j + 1, size):
                if arr[i] + arr[j] + arr[k] == 0:
                    print((arr[i], arr[j], arr[k]))

def ZeroSumTriplets2(arr):
    size = len(arr)
    arr.sort()
    for i in range(size-2):
        start = i+1
        stop = size-1

        while start < stop:
            if arr[i] + arr[start] + arr[stop] == 0:
                print((arr[i], arr[start], arr[stop]))
                start += 1
                stop -= 1
            elif arr[i] + arr[start] + arr[stop] > 0:
                stop -= 1
            else:
                start += 1

arr = [0, -1, 2, -3, 1]
print(arr)
ZeroSumTriplets(arr)
print(arr)
ZeroSumTriplets2(arr)




def ABCTriplet(arr):
    size = len(arr)
    arr.sort(reverse = True)
    
    for i in range(size-2):
        start = i+1
        stop = size-1
        while start < stop:
            if arr[i] == arr[start] + arr[stop]:
                print((arr[i], arr[start], arr[stop]))
                start += 1
                stop -= 1
            elif arr[i] > arr[start] + arr[stop]:
                stop -= 1
            else:
                start += 1


arr = [1, 5, 15, 6, 9, 8]
ABCTriplet(arr)



def SmallerThenTripletCount(arr, value):
    size = len(arr)
    arr.sort()
    count = 0
    for i in range(size-2):
        start = i+1
        stop = size - 1
        while start < stop:
            if arr[i] + arr[start] + arr[stop] >= value:
                stop -= 1
            else:
                count += stop - start 
                start += 1
    print(count)
        

arr = [-2, -1,  0, 1]
print(arr)
SmallerThenTripletCount(arr, 2)
