"""
Given two sorted arrays find union and intersection of these two arrays.

Another problem:
Given two unsorted arrays find union and intersection of these two arrays.
Use sorting then use th above algorithm.

"""

def UnionIntersectionSorted(arr1, arr2):
    size1 = len(arr1)
    size2 = len(arr2)
    first, second = 0, 0
    union = []
    inter = []
    while first < size1 and second < size2 :
        if arr1[first] == arr2[second]:
            union.append(arr1[first])
            inter.append(arr1[first])
            first += 1
            second += 1
        elif arr1[first] < arr2[second]:
            union.append(arr1[first])
            first += 1
        else:
            union.append(arr2[second])
            second += 1

    while first < size1 :
        union.append(arr1[first])
        first += 1
        
    while second < size2 :
        union.append(arr2[second])
        second += 1
    print union
    print inter

"""
arr1 = [1, 2, 3, 5, 6, 8, 9]
arr2 = [2, 4, 5, 7, 8, 10]
UnionIntersectionSorted(arr1, arr2)
"""

def UnionIntersectionUnsorted(arr1, arr2):
    arr1.sort()
    arr2.sort()
    UnionIntersectionSorted(arr1, arr2)



arr1 = [1, 11, 2, 3, 14, 5, 6, 8, 9]
arr2 = [2, 4, 5, 12, 7, 8, 13, 10]
UnionIntersectionUnsorted(arr1, arr2)