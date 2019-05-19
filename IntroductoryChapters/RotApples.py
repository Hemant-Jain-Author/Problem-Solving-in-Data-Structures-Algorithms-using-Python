
def RottenFruitUtil(arr, maxCol, maxRow, currCol, currRow, traversed, day):
    # Range check
    if currCol < 0 or currCol >= maxCol or currRow < 0 or currRow >= maxRow :
        return
    # Traversable and rot if not already rotten.
    if traversed[currCol][currRow] <= day or arr[currCol][currRow] == 0:
        return
    # Update rot time.
    traversed[currCol][currRow] = day
    # each line corresponding to 4 direction.
    RottenFruitUtil(arr, maxCol, maxRow, currCol-1, currRow, traversed, day+1)
    RottenFruitUtil(arr, maxCol, maxRow, currCol+1, currRow, traversed, day+1)
    RottenFruitUtil(arr, maxCol, maxRow, currCol, currRow+1, traversed, day+1)
    RottenFruitUtil(arr, maxCol, maxRow, currCol, currRow-1, traversed, day+1)

infi = 99999
def RottenFruit(arr, maxCol, maxRow):
    traversed = [[infi]*maxCol for i in range(maxRow)]
    for i in range(0, maxCol-1, 1):
        for j in range(0, maxRow-1, 1):
            if arr[i][j] == 2:
                RottenFruitUtil(arr, maxCol, maxRow, i, j, traversed, 0)
    maxDay = 0
    for i in range(0, maxCol, 1):
        for j in range(0, maxRow, 1):
            if arr[i][j] == 1 : 
                if traversed[i][j] == infi :
                    return -1
                if maxDay < traversed[i][j]:
                    maxDay = traversed[i][j]
    return maxDay

def main():
    arr = [
        [ 1 , 0 , 1, 1 , 0], 
        [ 1 , 1, 0, 1 , 0], 
        [ 0 , 0 , 0, 2 , 1], 
        [ 0 , 2 , 0, 0 , 1], 
        [ 1 , 1 , 0, 0 , 1]]
    print(arr)
    print(RottenFruit(arr, 5, 5))

#main()


def DistNearestFillUtil(arr, maxCol, maxRow, currCol, currRow, traversed, dist):
    # Range check
    if currCol < 0 or  currCol >= maxCol or currRow < 0 or currRow >= maxRow :
        return
    # Traversable if their is a better distance.
    if traversed[currCol][currRow] <= dist :
        return
    # Update distance.
    traversed[currCol][currRow] = dist
    # each line corresponding to 4 direction.
    DistNearestFillUtil(arr, maxCol, maxRow, currCol-1, currRow, traversed, dist+1)
    DistNearestFillUtil(arr, maxCol, maxRow, currCol+1, currRow, traversed, dist+1)
    DistNearestFillUtil(arr, maxCol, maxRow, currCol, currRow+1, traversed, dist+1)
    DistNearestFillUtil(arr, maxCol, maxRow, currCol, currRow-1, traversed, dist+1)

infi = 99999
def DistNearestFill(arr, maxCol, maxRow):
    traversed = [[infi]*maxCol for i in range(maxRow)]
    for i in range(0, maxCol, 1):
        for j in range(0, maxRow, 1):
            if arr[i][j] == 1:
                DistNearestFillUtil(arr, maxCol, maxRow, i, j, traversed, 0)
    print(traversed)

def main2():
    arr = [
        [ 1 , 0 , 1, 1 , 0], 
        [ 1 , 1, 0, 1 , 0], 
        [ 0 , 0 , 0, 0 , 1], 
        [ 0 , 0 , 0, 0 , 1], 
        [ 0 , 0 , 0, 0 , 1]]
    print(arr)
    DistNearestFill(arr, 5, 5)

main2()

def StepsOfKnightUtil(size, currCol, currRow, traversed, dist):
    # Range check
    if currCol < 0 or currCol >= size or currRow < 0 or currRow >= size :
        return
    # Traversable and rot if not already rotten.
    if traversed[currCol][currRow] <= dist :
        return
    # Update rot time.
    traversed[currCol][currRow] = dist
    # each line corresponding to 4 direction.
    StepsOfKnightUtil(size, currCol-2, currRow-1, traversed, dist+1)
    StepsOfKnightUtil(size, currCol-2, currRow+1, traversed, dist+1)
    StepsOfKnightUtil(size, currCol+2, currRow-1, traversed, dist+1)
    StepsOfKnightUtil(size, currCol+2, currRow+1, traversed, dist+1)
    StepsOfKnightUtil(size, currCol-1, currRow-2, traversed, dist+1)
    StepsOfKnightUtil(size, currCol+1, currRow-2, traversed, dist+1)
    StepsOfKnightUtil(size, currCol-1, currRow+2, traversed, dist+1)
    StepsOfKnightUtil(size, currCol+1, currRow+2, traversed, dist+1)

infi = 99999
def StepsOfKnight(size, srcX, srcY, dstX, dstY):
    traversed = [[infi]*size for _ in range(size)]
    StepsOfKnightUtil(size, srcX - 1, srcY - 1, traversed, 0)
    for i in range(size):
        print(traversed[i])
    return traversed[dstX - 1][dstY - 1]

#print StepsOfKnight(20,10,10,20,20)



def findLargestIslandUtil(arr, maxCol, maxRow, currCol, currRow, value, traversed) :
    if currCol < 0 or currCol >= maxCol or currRow < 0 or currRow >= maxRow :
        return 0
    if traversed[currCol][currRow] == 1 or arr[currCol][currRow] != value :
        return 0
    traversed[currCol][currRow] = 1

    # each call corresponding to 8 direction.
    return 1 + findLargestIslandUtil(arr, maxCol, maxRow, currCol - 1, currRow - 1, value, traversed) + findLargestIslandUtil(arr, maxCol, maxRow, currCol - 1, currRow, value, traversed) + findLargestIslandUtil(arr, maxCol, maxRow, currCol - 1, currRow + 1, value, traversed) + findLargestIslandUtil(arr, maxCol, maxRow, currCol, currRow - 1, value, traversed) + findLargestIslandUtil(arr, maxCol, maxRow, currCol, currRow + 1, value, traversed) + findLargestIslandUtil(arr, maxCol, maxRow, currCol + 1, currRow - 1, value, traversed) + findLargestIslandUtil(arr, maxCol, maxRow, currCol + 1, currRow, value, traversed) + findLargestIslandUtil(arr, maxCol, maxRow, currCol + 1, currRow + 1, value, traversed)

def findLargestIsland(arr, maxCol, maxRow):
    maxVal = 0
    currVal = 0
    traversed = [[infi]*maxCol for i in range(maxRow)]

    for i in range(maxCol):
        for j in range(maxRow):
            currVal = findLargestIslandUtil(arr, maxCol, maxRow, i, j, arr[i][j], traversed)
            if currVal > maxVal :
                maxVal = currVal

    return maxVal

def main19():
    arr = [[1, 0, 1, 1, 0], [1, 0, 0, 1, 0], [0, 1, 1, 1, 1 ], [ 0, 1, 0, 0, 0], [1, 1, 0, 0, 1]]
    print("Largest Island : " , findLargestIsland(arr, 5, 5))

main19()

