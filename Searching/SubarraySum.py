def subArraySums(arr, value):
    size = len(arr)
    first = 0
    second = 0
    sum = arr[first]
    while second < size and first < size:
        if sum == value:
            print(first , second)

        if sum < value:
            second += 1
            if second < size :
                sum += arr[second]
        else :
            sum -= arr[first]
            first += 1


def subArraySum(arr, value):
    size = len(arr)
    first = 0
    second = 0
    sum = arr[first]
    while second < size and first < size:
        if sum == value:
            print(first , second)
            return True
        if sum < value:
            second += 1
            if second < size :
                sum += arr[second]
        else :
            sum -= arr[first]
            first += 1
    return False

arr = [15, 5, 5, 20, 10, 5, 5, 20, 10, 10]
subArraySum(arr, 20)
print("")
subArraySums(arr, 20)