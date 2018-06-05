def findTriplet(arr, value):
    size = len(arr) 
    for i in range(size-2):
        for j in range(i+1, size-1): 
            for k in range(j + 1, size):
                if arr[i] + arr[j] + arr[k] == value:
                    print(arr[i], arr[j], arr[k])
                    return True
    return False

def findTriplet2(arr, value):
    size = len(arr)
    arr.sort()
    output = []
    for i in range(size-2):
        output.append(arr[i])
        start = i+1
        stop = size-1
        pairSum = value - arr[i]

        while start < stop:
            if arr[start] + arr[stop] == pairSum:
                output.append(arr[start])
                output.append(arr[stop])
                break
            elif arr[start] + arr[stop] > pairSum:
                stop -= 1
            else:
                start += 1

        if start < stop:
            print output
            return True
        else:
            output.pop()
    return False

arr = [1, 5, 15, 6, 9, 8]
findTriplet(arr, 22)
findTriplet2(arr, 22)
