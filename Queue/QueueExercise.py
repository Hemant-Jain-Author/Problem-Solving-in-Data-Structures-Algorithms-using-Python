import sys
from collections import deque

def circular_tour(arr,  n) :
    i = 0
    while (i < n) :
        total = 0
        found = True
        j = 0
        while (j < n) :
            total += (arr[(i + j) % n][0] - arr[(i + j) % n][1])
            if (total < 0) :
                found = False
                break
            j += 1
        if (found) :
            return  i
        i += 1
    return  -1

def circular_tour2(arr, n):
    que = deque([])
    next_pump = 0
    count = 0
    petrol = 0

    while len(que) != n:
        while petrol >= 0 and len(que) != n :
            que.append(next_pump)
            petrol += (arr[next_pump][0] - arr[next_pump][1])
            next_pump = (next_pump + 1) % n
            
        while petrol < 0 and len(que) > 0:
            prev_pump = que.popleft()
            petrol -= (arr[prev_pump][0] - arr[prev_pump][1])
        
        count += 1
        if count == n:
            return -1

    if petrol >= 0:
        return que.popleft()
    else:
        return -1


def main1():
    tour = [[8, 6], 
    [1, 4], 
    [7, 6]]
    print(circular_tour(tour, 3))
    print(circular_tour2(tour, 3))


"""
2
"""

def convert_XY(src, dst):
    que = deque([])
    visited = {}
    que.append((src, 0))
    while len(que) != 0:
        node = que.popleft()
        visited[node[0]] = 1
        value = node[0]
        steps = node[1]
        if value == dst:
            return steps
        if value < dst and (value*2) not in visited:
            que.append((value*2, steps+1))
        if value > 0 and (value - 1) not in visited:
            que.append((value-1, steps+1))
    return -1

def main2():   
    print("3 to 4 Steps counter ::", convert_XY(3, 4))
    print("3 to 5 Steps counter ::", convert_XY(3, 5))
    print("3 to 6 Steps counter ::", convert_XY(3, 6))

"""
3 to  4  :  2
3 to  5  :  2
3 to  6  :  1
"""

def max_sliding_windows(arr,  k) :
    size = len(arr)
    i = 0
    while (i < size - k + 1) :
        mx = arr[i]
        j = 1
        while (j < k) :
            mx = max(mx,arr[i + j])
            j += 1
        print(str(mx) + " ", end ="")
        i += 1
    print()

def max_sliding_windows2(arr, k):
    size = len(arr)
    que = deque()
    for i in range(size):
        # Remove out of range elements
        if que and que[0] <= i - k:
            que.popleft()
        # Remove smaller values at left.
        while que and arr[que[-1]] <= arr[i] :
            que.pop()
        que.append(i)
        # window of size k
        if i >= (k - 1):
            print(arr[que[0]], end=" ")

def main3():
    arr = [11, 2, 75, 92, 59, 90, 55]
    k = 3
    max_sliding_windows(arr, k)
    max_sliding_windows2(arr, k)


"""
75 92 92 92 90
"""

def first_neg_sliding_windows(arr, k):
    size = len(arr)
    que = deque()
    for i in range(size):
        # Remove out of range elements
        if que and que[0] <= i - k:
            que.popleft()
        if arr[i] < 0:
            que.append(i)
        # window of size k
        if i >= (k - 1) :
            if len(que) > 0:
                print(arr[que[0]], end=" ")
            else:
                print("NAN", end=" ") 

def main4():
    arr3 = [13, -2, -6, 10, -14, 50, 14, 21]
    first_neg_sliding_windows(arr3, 3)

"""
-2 -2 -6 -14 -14 NAN
"""

def minofmax_sliding_windows(arr, k):
    size = len(arr)
    que = deque()
    min_val = 999999
    for i in range(size):
        # Remove out of range elements
        if que and que[0] <= i - k:
            que.popleft()
        # Remove smaller values at left.
        while que and arr[que[-1]] <= arr[i] :
            que.pop()
        que.append(i)
        # window of size k
        if i >= (k - 1) and min_val > arr[que[0]] :
            min_val = arr[que[0]]
    print("Min of max is : ", min_val)

def main5():
    arr = [11, 2, 75, 92, 59, 90, 55]
    minofmax_sliding_windows(arr, 3)

"""
Min of max is :  75
"""

def maxofmin_sliding_windows(arr, k):
    size = len(arr)
    que = deque()
    max_val = -999999
    for i in range(size):
        # Remove out of range elements
        if que and que[0] <= i - k:
            que.popleft()
        # Remove smaller values at left.
        while que and arr[que[-1]] >= arr[i] :
            que.pop()
        que.append(i)
        # window of size k
        if i >= (k - 1) and max_val < arr[que[0]] :
            max_val = arr[que[0]]
    print("Max of min is : ", max_val)


def main6():
    arr = [10, 20, 30, 50, 10, 70, 30]
    maxofmin_sliding_windows(arr, 3)

"""     
Max of min is :  20
"""

def rottenFruitUtil(arr,  maxCol,  maxRow,  currCol,  currRow,  traversed,  day) :
    dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for i in range(4) :
        x = currCol + dir[i][0]
        y = currRow + dir[i][1]
        if (x >= 0 and x < maxCol and 
            y >= 0 and y < maxRow and 
            traversed[x][y] > day + 1 and arr[x][y] == 1) :
            traversed[x][y] = day + 1
            rottenFruitUtil(arr, maxCol, maxRow, x, y, traversed, day + 1)

def rottenFruit(arr,  maxCol,  maxRow) :
    traversed = [[0] * (maxRow) for _ in range(maxCol)]
    i = 0
    while (i < maxCol) :
        j = 0
        while (j < maxRow) :
            traversed[i][j] = sys.maxsize
            j += 1
        i += 1
    i = 0
    while (i < maxCol) :
        j = 0
        while (j < maxRow) :
            if (arr[i][j] == 2) :
                traversed[i][j] = 0
                rottenFruitUtil(arr, maxCol, maxRow, i, j, traversed, 0)
            j += 1
        i += 1
    maxDay = 0
    i = 0
    while (i < maxCol) :
        j = 0
        while (j < maxRow) :
            if (arr[i][j] == 1) :
                if (traversed[i][j] == sys.maxsize) :
                    return  -1
                if (maxDay < traversed[i][j]) : 
                    maxDay = traversed[i][j]
            j += 1
        i += 1
    return  maxDay

def rottenFruit2(arr,  maxCol,  maxRow) :
    traversed = [[False] * (maxRow) for _ in range(maxCol)]
    dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    que =  deque()
    i = 0
    while (i < maxCol) :
        j = 0
        while (j < maxRow) :
            traversed[i][j] = False
            if (arr[i][j] == 2) :
                que.append((i, j, 0))
                traversed[i][j] = True
            j += 1
        i += 1
    mx = 0
    while (len(que) > 0) :
        temp = que.popleft()
        i = 0
        while (i < 4) :
            x = temp[0] + dir[i][0]
            y = temp[1] + dir[i][1]
            day = temp[2] + 1
            if (x >= 0 and x < maxCol and y >= 0 and y < maxRow and arr[x][y] != 0 and traversed[x][y] == False) :
                que.append((x, y, day))
                mx = max(mx,day)
                traversed[x][y] = True
            i += 1
    i = 0
    while (i < maxCol) :
        j = 0
        while (j < maxRow) :
            if (arr[i][j] == 1 and traversed[i][j] == False) :
                return  -1
            j += 1
        i += 1
    return  mx

def main7() :
    arr = [[1, 0, 1, 1, 0], [2, 1, 0, 1, 0], [0, 0, 0, 2, 1], [0, 2, 0, 0, 1], [1, 1, 0, 0, 1]]
    print(rottenFruit(arr, 5, 5))
    print(rottenFruit2(arr, 5, 5))
#  3

def stepsOfKnightUtil(size,  currCol,  currRow,  traversed,  dist) :
    dir = [[-2, -1], [-2, 1], [2, -1], [2, 1], [-1, -2], [1, -2], [-1, 2], [1, 2]]
    i = 0
    while (i < 8) :
        x = currCol + dir[i][0]
        y = currRow + dir[i][1]
        if (x >= 0 and x < size and y >= 0 and y < size and traversed[x][y] > dist + 1) :
            traversed[x][y] = dist + 1
            stepsOfKnightUtil(size, x, y, traversed, dist + 1)
        i += 1
def stepsOfKnight(size,  srcX,  srcY,  dstX,  dstY) :
    traversed = [[0] * (size) for _ in range(size)]
    i = 0
    while (i < size) :
        j = 0
        while (j < size) :
            traversed[i][j] = sys.maxsize
            j += 1
        i += 1
    traversed[srcX - 1][srcY - 1] = 0
    stepsOfKnightUtil(size, srcX - 1, srcY - 1, traversed, 0)
    return  traversed[dstX - 1][dstY - 1]


def stepsOfKnight2(size,  srcX,  srcY,  dstX,  dstY) :
    traversed = [[0] * (size) for _ in range(size)]
    dir = [[-2, -1], [-2, 1], [2, -1], [2, 1], [-1, -2], [1, -2], [-1, 2], [1, 2]]
    que =  deque()
    i = 0
    while (i < size) :
        j = 0
        while (j < size) :
            traversed[i][j] = sys.maxsize
            j += 1
        i += 1
    que.append((srcX - 1, srcY - 1, 0))
    traversed[srcX - 1][srcY - 1] = 0
    while (len(que) != 0) :
        temp = que.popleft()
        i = 0
        while (i < 8) :
            x = temp[0] + dir[i][0]
            y = temp[1] + dir[i][1]
            cost = temp[2] + 1
            if (x >= 0 and x < size and y >= 0 and y < size and traversed[x][y] > cost) :
                que.append((x, y, cost))
                traversed[x][y] = cost
            i += 1
    return  traversed[dstX - 1][dstY - 1]

def main8() :
    print(stepsOfKnight(20, 10, 10, 20, 20))
    print(stepsOfKnight2(20, 10, 10, 20, 20))
#  8

def distNearestFillUtil(arr,  maxCol,  maxRow,  currCol,  currRow,  traversed,  dist) :
    #  Range check
    dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    i = 0
    while (i < 4) :
        x = currCol + dir[i][0]
        y = currRow + dir[i][1]
        if (x >= 0 and x < maxCol and y >= 0 and y < maxRow and traversed[x][y] > dist + 1) :
            traversed[x][y] = dist + 1
            distNearestFillUtil(arr, maxCol, maxRow, x, y, traversed, dist + 1)
        i += 1

def distNearestFill(arr,  maxCol,  maxRow) :
    traversed = [[0] * (maxRow) for _ in range(maxCol)]
    i = 0
    while (i < maxCol) :
        j = 0
        while (j < maxRow) :
            traversed[i][j] = sys.maxsize
            j += 1
        i += 1
    i = 0
    while (i < maxCol) :
        j = 0
        while (j < maxRow) :
            if (arr[i][j] == 1) :
                traversed[i][j] = 0
                distNearestFillUtil(arr, maxCol, maxRow, i, j, traversed, 0)
            j += 1
        i += 1
    i = 0
    while (i < maxCol) :
        j = 0
        while (j < maxRow) :
            print(str(traversed[i][j]) + " ", end ="")
            j += 1
        print()
        i += 1



def distNearestFill2(arr,  maxCol,  maxRow) :
    traversed = [[0] * (maxRow) for _ in range(maxCol)]
    dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    que =  deque()
    i = 0
    while (i < maxCol) :
        j = 0
        while (j < maxRow) :
            traversed[i][j] = sys.maxsize
            if (arr[i][j] == 1) :
                que.append((i, j, 0))
                traversed[i][j] = 0
            j += 1
        i += 1
    while (len(que) != 0) :
        temp = que.popleft()
        i = 0
        while (i < 4) :
            x = temp[0] + dir[i][0]
            y = temp[1] + dir[i][1]
            dist = temp[2] + 1
            if (x >= 0 and x < maxCol and y >= 0 and y < maxRow and traversed[x][y] > dist) :
                que.append((x, y, dist))
                traversed[x][y] = dist
            i += 1
    i = 0
    while (i < maxCol) :
        j = 0
        while (j < maxRow) :
            print(str(traversed[i][j]) + " ", end ="")
            j += 1
        print()
        i += 1

def main9() :
    arr = [[1, 0, 1, 1, 0], [1, 1, 0, 1, 0], [0, 0, 0, 0, 1], [0, 0, 0, 0, 1], [0, 0, 0, 0, 1]]
    distNearestFill(arr, 5, 5)
    distNearestFill2(arr, 5, 5)
#    0 1 0 0 1 
#    0 0 1 0 1 
#    1 1 2 1 0 
#    2 2 2 1 0 
#    3 3 2 1 0

def findLargestIslandUtil(arr,  maxCol,  maxRow,  currCol,  currRow,  traversed) :
    dir = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    sum = 1
    i = 0
    while (i < 8) :
        x = currCol + dir[i][0]
        y = currRow + dir[i][1]
        if (x >= 0 and x < maxCol and y >= 0 and y < maxRow and traversed[x][y] == False and arr[x][y] == 1) :
            traversed[x][y] = True
            sum += findLargestIslandUtil(arr, maxCol, maxRow, x, y, traversed)
        i += 1
    return  sum

def findLargestIsland(arr,  maxCol,  maxRow) :
    maxVal = 0
    currVal = 0
    traversed = [[False] * (maxRow) for _ in range(maxCol)]
    i = 0
    while (i < maxCol) :
        j = 0
        while (j < maxRow) :
            traversed[i][j] = False
            j += 1
        i += 1
    i = 0
    while (i < maxCol) :
        j = 0
        while (j < maxRow) :
            if (arr[i][j] == 1) :
                traversed[i][j] = True
                currVal = findLargestIslandUtil(arr, maxCol, maxRow, i, j, traversed)
                if (currVal > maxVal) : maxVal = currVal
            j += 1
        i += 1
    return  maxVal

def main10() :
    arr = [[1, 0, 1, 1, 0], [1, 0, 0, 1, 0], [0, 1, 1, 1, 1], [0, 1, 0, 0, 0], [1, 1, 0, 0, 1]]
    print("Largest Island : " + str(findLargestIsland(arr, 5, 5)))

#  Largest Island : 12

def reverseStack(stk) :
    que =  deque()
    while (not (len(stk) == 0)) :
        que.append(stk[-1])
        stk.pop()
    while (len(que) != 0) :
        stk.append(que.popleft())

def reverseQueue(que) :
    stk =  []
    while (len(que) != 0) :
        stk.append(que.popleft())

    while (not (len(stk) == 0)) :
        que.append(stk[-1])
        stk.pop()

def main11() :
    stk =  []
    i = 0
    while (i < 5) :
        stk.append(i)    
        i += 1
    print(stk)
    reverseStack(stk)
    print(stk)
    que =  deque()
    i = 0
    while (i < 5) :
        que.append(i)    
        i += 1
    print(que)
    reverseQueue(que)
    print(que)

def Josephus(n,  k) :
    que =  deque()
    i = 0
    while (i < n) :
        que.append(i + 1)    
        i += 1
    while (len(que) > 1) :
        i = 0
        while (i < k - 1) :
            que.append(que.popleft())
            i += 1
        que.popleft()
    return  que[0]

def main12() :
    print("Position : " + str(Josephus(11, 5)))
# Position : 8

main1()
main2()
main3()
main4()
main5()
main6()
main7()
main8()
main9()
main10()
main11()
main12()




