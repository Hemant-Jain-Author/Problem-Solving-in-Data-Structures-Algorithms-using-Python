"""
Given an array of positive integers representing edges of triangles.
Find the number of triangles that can be formed from these elements 
representing sides of triangles.
For a triangle sum of two edges is always grater then third edge.
"""
def numberOfTriangles(arr):
    size = len(arr)
    count = 0
 
    for i in range(0,size - 2):
        for j in range(i+1, size - 1):
            for k in range(j+1, size):
                if arr[i] + arr[j] > arr[k]:
                    count += 1
    return count



def numberOfTriangles2(arr):
    size = len(arr)
    arr.sort()
    count = 0
 
    for i in range(0,size - 2):
        k = i + 2
        for j in range(i+1, size - 1):
            # if sum of arr[i] & arr[j] is grater arr[k] 
            # then sum of arr[i] & arr[j+1] is also grater then arr[k]
            # this improvement make algo O(n2)
            while k < size and arr[i] + arr[j] > arr[k]:
                k += 1

            count += k - j - 1
    return count

arr = [1, 2, 3, 4, 5]
print(numberOfTriangles(arr))
print(numberOfTriangles2(arr))
# (2,3,4)(2,4,5)(3,4,5)
# three triangles