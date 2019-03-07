"""
Given two sorted arrays. Sort the elements of these arrays so that first half of 
sorted elements will lie in first array and second half lies in second array. 
Extra space allowed is O(1). 

Time complexity will M*N where M is length of first array and N is length of second array.
"""
def merge(arr1, arr2):
    size1 = len(arr1)
    size2 = len(arr2)
    first = 0
    while first < size1:
        if arr1[first] <= arr2[0]:
            first += 1
        else:
            # always first element of arr2 is compared.
            arr1[first], arr2[0] = arr2[0], arr1[first]
            first += 1
            # After swap arr2 may be unsorted.
            # Insertion of Oth element in proper sorted possition.
            for i in range(size2 - 1):
                if arr2[i] < arr2[i+1]:
                    break
                arr2[i], arr2[i+1] = arr2[i+1], arr2[i]

# Testing code.
arr1 = [1, 5, 9, 10, 15, 20]
arr2 = [2, 3, 8, 13]
merge(arr1, arr2)
print(arr1, arr2)