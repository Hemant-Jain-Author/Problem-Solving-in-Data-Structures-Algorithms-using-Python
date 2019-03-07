def printUnique(arr):
    size = len(arr)
    print(" Unique elements are ::", end=' ')
    for i in range(size):
        for j in range(i+1):
            if arr[i] == arr[j]:
                break
        if j == i:
            print(arr[i], end=' ')


def printUnique2(arr):
    size = len(arr)
    arr.sort()
    print(" Unique elements are ::", end=' ')
    for i in range(size):
        if arr[i] != arr[i - 1]:
            print(arr[i], end=' ')


def printUnique3(arr):
    size = len(arr)
    hs = set()
    print(" Unique elements are ::", end=' ') 
    for i in range(size):
        if arr[i] not in hs:
            hs.add(arr[i])
            print(arr[i], end=' ')

def printUnique4(arr, valrange):
    size = len(arr)
    count = [0] * valrange
    print(" Unique elements are ::", end=' ')
    for i in range(size):
        if count[arr[i]] == 0:
            print(arr[i], end=' ')
        count[arr[i]] += 1

first = [1, 3, 5, 3, 9, 1, 30]
printUnique(first)
print("")
printUnique2(first)
print("")
printUnique3(first)
print("")
printUnique4(first, 50)