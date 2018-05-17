#!/usr/bin/env python

def findMaxPathUtil(arr, maxCol, maxRow, currCol, currRow, traversed, tempVal):
    if currCol < 0 or currCol >= maxCol or currRow < 0 or currRow >= maxRow :
        return
    if traversed[currCol][currRow] == 1 or arr[currCol][currRow] == 0:
        return
    traversed[currCol][currRow] = 1
    tempVal[0] += 1
    # each line corresponding to 8 direction.
    findMaxPathUtil(arr, maxCol, maxRow, currCol-1, currRow-1, traversed, tempVal)
    findMaxPathUtil(arr, maxCol, maxRow, currCol-1, currRow, traversed, tempVal)
    findMaxPathUtil(arr, maxCol, maxRow, currCol-1, currRow+1, traversed, tempVal)
    findMaxPathUtil(arr, maxCol, maxRow, currCol, currRow-1, traversed, tempVal)
    findMaxPathUtil(arr, maxCol, maxRow, currCol, currRow+1, traversed, tempVal)
    findMaxPathUtil(arr, maxCol, maxRow, currCol+1, currRow-1, traversed, tempVal)
    findMaxPathUtil(arr, maxCol, maxRow, currCol+1, currRow, traversed, tempVal)
    findMaxPathUtil(arr, maxCol, maxRow, currCol+1, currRow+1, traversed, tempVal)
    return

def findMaxPath(arr, maxCol, maxRow):
    maxVal = 0
    traversed = [[0]*maxCol for i in range(maxRow)]
    tempVal = [0]
    for i in range(0, maxCol-1, 1):
        for j in range(0, maxRow-1, 1):
            tempVal[0] = 0
            findMaxPathUtil(arr, maxCol, maxRow, i, j, traversed, tempVal)
            if(tempVal[0] > maxVal):
                maxVal = tempVal[0]
    return maxVal

def main():
    arr = [
        [ 1 , 0 , 1, 1 , 0], 
        [ 1 , 0 , 0, 1 , 0], 
        [ 0 , 1 , 1, 1 , 1], 
        [ 0 , 1 , 0, 0 , 0], 
        [ 1 , 1 , 0, 0 , 1]]    
    print(findMaxPath(arr, 5, 5))
    print(arr)

main()