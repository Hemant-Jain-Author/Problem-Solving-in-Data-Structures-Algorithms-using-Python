from collections import deque

infi = 99999
def RottenFruit(arr, maxCol, maxRow):
    que = deque([])
    maxDay = 0
    traversed = [[infi]*maxCol for i in range(maxRow)]
    for i in range(0, maxCol-1):
        for j in range(0, maxRow-1):
            if arr[i][j] == 2:
                que.append((i,j, 0))

    while len(que) != 0:
        (currCol, currRow, day) = que.popleft()
        if traversed[currCol][currRow] > day and arr[currCol][currRow] != 0:
            
            traversed[currCol][currRow] = day
            if day > maxDay :
                maxDay = day

            if currCol > 0:
                que.append((currCol-1, currRow, day+1))
            if currCol < maxCol - 1:
                que.append((currCol+1, currRow, day+1))
            if currRow > 0 :
                que.append((currCol, currRow-1, day+1))
            if currRow < maxRow - 1 :
                que.append((currCol, currRow+1, day+1))
        
    return maxDay
    
arr = [
    [ 1 , 0 , 1, 1 , 0], 
    [ 1 , 2, 0, 1 , 0], 
    [ 0 , 0 , 0, 2 , 1], 
    [ 0 , 2 , 0, 0 , 1], 
    [ 1 , 1 , 0, 0 , 1]]
print(RottenFruit(arr, 5, 5))