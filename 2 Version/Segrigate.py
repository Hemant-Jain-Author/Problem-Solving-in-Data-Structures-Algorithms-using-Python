"""Segregate even odd.
"""
def SegregateEvenOdd(arr):
    first = 0
    second = len(arr) - 1
    while first < second:
        if arr[first] % 2 == 0:
            first += 1
        elif arr[second] % 2 != 0:
            second -= 1
        else:
            arr[first], arr[second] = arr[second], arr[first]


"""
Segregate possitive ans negative.
"""
def SegregatePossitiveNegative(arr):
    first = 0
    second = len(arr) - 1
    while first < second:
        if arr[first] <= 0:
            first += 1
        elif arr[second] > 0:
            second -= 1
        else:
            arr[first], arr[second] = arr[second], arr[first]

"""
Segrigate possitive and negative , order of appearence should be maintained.
Just Segregate like insertion sort.
Use an array.
"""
def SegregatePossitiveNegative2(arr):
    index = 0
    size = len(arr)
    arr2 = list(arr)
    for i in range(size) :
        if arr2[i] <= 0:
            arr[index] = arr2[i]
            index += 1
    for i in range(size) :
        if arr2[i] > 0:
            arr[index] = arr2[i]
            index += 1

"""
Segrigate Even number at even index and odd numbers at odd index. 
If possible then return true else return false.
"""
def SegregateEvenOdd2(arr):
    odd = 1
    even = 0
    size = len(arr)
    while odd <= size or even <= size:
        if arr[even] % 2 == 0:
            even += 2
        elif arr[odd] % 2 != 0:
            odd += 2
        else:
            arr[odd], arr[even] = arr[even], arr[odd]
    if odd - even > 1:
        return False
    else :
        return True

