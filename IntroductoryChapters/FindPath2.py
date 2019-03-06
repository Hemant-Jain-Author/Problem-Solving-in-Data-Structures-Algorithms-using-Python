#!/usr/bin/env python
"""
find path

"""
def findMaxPathUtil2(arr, maxCol, maxRow, currCol, currRow, value, traversed, tempVal):
    if currCol < 0 or currCol >= maxCol or currRow < 0 or currRow >= maxRow :
        return
    if traversed[currCol][currRow] == 1 or arr[currCol][currRow] != value:
        return
    traversed[currCol][currRow] = 1
    tempVal[0] += 1
    # each line corresponding to 8 direction.
    findMaxPathUtil2(arr, maxCol, maxRow, currCol-1, currRow-1, value, traversed, tempVal)
    findMaxPathUtil2(arr, maxCol, maxRow, currCol-1, currRow, value, traversed, tempVal)
    findMaxPathUtil2(arr, maxCol, maxRow, currCol-1, currRow+1, value, traversed, tempVal)
    findMaxPathUtil2(arr, maxCol, maxRow, currCol, currRow-1, value, traversed, tempVal)
    findMaxPathUtil2(arr, maxCol, maxRow, currCol, currRow+1, value, traversed, tempVal)
    findMaxPathUtil2(arr, maxCol, maxRow, currCol+1, currRow-1, value, traversed, tempVal)
    findMaxPathUtil2(arr, maxCol, maxRow, currCol+1, currRow, value, traversed, tempVal)
    findMaxPathUtil2(arr, maxCol, maxRow, currCol+1, currRow+1, value, traversed, tempVal)
    return

def findMaxPathUtil(arr, maxCol, maxRow, currCol, currRow, value, traversed):
    if currCol < 0 or currCol >= maxCol or currRow < 0 or currRow >= maxRow :
        return 0
    if traversed[currCol][currRow] == 1 or arr[currCol][currRow] != value:
        return 0
    traversed[currCol][currRow] = 1
    # each call corresponding to 8 direction.
    return 1 + findMaxPathUtil(arr, maxCol, maxRow, currCol-1, currRow-1, value, traversed) + findMaxPathUtil(arr, maxCol, maxRow, currCol-1, currRow, value, traversed) + findMaxPathUtil(arr, maxCol, maxRow, currCol-1, currRow+1, value, traversed) + findMaxPathUtil(arr, maxCol, maxRow, currCol, currRow-1, value, traversed) + findMaxPathUtil(arr, maxCol, maxRow, currCol, currRow+1, value, traversed) + findMaxPathUtil(arr, maxCol, maxRow, currCol+1, currRow-1, value, traversed) + findMaxPathUtil(arr, maxCol, maxRow, currCol+1, currRow, value, traversed) + findMaxPathUtil(arr, maxCol, maxRow, currCol+1, currRow+1, value, traversed)


def findMaxPath(arr, maxCol, maxRow):
    maxVal = 0
    traversed = [[0]*maxCol for i in range(maxRow)]
    for i in range(maxCol):
        for j in range(maxRow):
            temp = findMaxPathUtil(arr, maxCol, maxRow, i, j, arr[i][j], traversed)
            if(temp > maxVal):
                maxVal = temp
    return maxVal

def main():
    arr = [
        [ 1 , 0 , 1, 1 , 0], 
        [ 1 , 0 , 0, 1 , 0], 
        [ 0 , 0 , 1, 1 , 1], 
        [ 0 , 1 , 0, 0 , 0], 
        [ 1 , 1 , 0, 0 , 1]]
    print(arr)
    print(findMaxPath(arr, 5, 5))

    arr = [
        [ 1 , 0 , 1, 1 , 0], 
        [ 1 , 1 , 0, 3 , 0], 
        [ 3 , 3 , 1, 1 , 3], 
        [ 0 , 3 , 3, 0 , 3], 
        [ 1 , 1 , 0, 3 , 3]]    
    print(arr)
    print(findMaxPath(arr, 5, 5))
    

main()