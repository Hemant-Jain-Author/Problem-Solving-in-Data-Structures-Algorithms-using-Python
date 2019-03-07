"""
Find second largest element in an array.
"""
def print2ndLargest(arr):
    size = len(arr)
    if size < 2:
        print("Invalid Input")
        return

    if arr[0] > arr[1]:
        first = arr[0]
        second = arr[1]
    else :
        second = arr[0]
        first = arr[1]
    
    for i in range(2, size):
        # first is always largest.
        if arr[i] <= first:
            second = first
            first = arr[i]
        elif (arr[i] < second ):
            second = arr[i]

    print("second largest value : ", second)

"""
Find third largest element in an array.
"""
def print3rdLargest(arr):
    size = len(arr)
    if size < 3:
        print("Invalid Input")
        return

    first = second = third = -9999999

    for i in range(size):
        # first is always largest.
        if arr[i] <= first:
            third = second
            second = first
            first = arr[i]
        elif arr[i] < second :
            third = second
            second = arr[i]
        elif arr[i] < third :
            third = arr[i]

    print("third largest value : ", third)


"""
Find Kth largest element in an array.
Use heap in this case. Min heap.
"""