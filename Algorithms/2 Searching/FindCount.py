"""
Given an array of size N, which contain integers from 1 to N. 
Elements can appear any number of times. 
Print frequency of all elements in the array also print the missing elements frequency as 0

Input:
arr1 = [1, 2, 2, 2, 1]

Output:
1  :  2
2  :  3
3  :  0
4  :  0
5  :  0
"""

def frequencyCounts(arr):
    size = len(arr)
    for i in range(size):
        while arr[i] > 0:
            index = arr[i] - 1
            if arr[index] > 0:
                arr[i] = arr[index]
                arr[index] = -1
            else:
                arr[index] -= 1
                arr[i] = 0
 
    for i in range(size):
        print i+1, " : ", abs(arr[i])
    print ""
 
arr1 = [1, 2, 2, 2, 1]
frequencyCounts(arr1)
 
arr2 = [2, 2, 2, 2]
frequencyCounts(arr2)
 
arr3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
frequencyCounts(arr3)
 
arr4 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
frequencyCounts(arr4)