"""
Given an interger array A of N elements and a boolean array B of N-1 elements.
You need to sort array A by swapping, element at A[i] can be swapped with A[i+1] if B[i] is 1 
The function should return true if sorting is possible else return false.
"""

def SortAB(A, B):
    size = len(A)
    for i in range(size-1):
        for j in range(size-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                if B[j] == 0:
                    return False
    return True

A = [1, 2, 4, 3, 6, 5]
B = [0, 0, 1, 1, 1]
print SortAB(A, B)

A = [5, 3, 1, 4, 2, 6]
B = [0, 1, 1, 1, 1]
print SortAB(A, B)