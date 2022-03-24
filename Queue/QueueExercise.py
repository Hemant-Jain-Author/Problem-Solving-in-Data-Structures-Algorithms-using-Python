import sys
from collections import deque

def circular_tour(arr,  n) :
    for i in range(n) :
        total = 0
        found = True
        for j in range(n) :
            total += (arr[(i + j) % n][0] - arr[(i + j) % n][1])
            if (total < 0) :
                found = False
                break
        if (found) :
            return  i
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

# Testing Code
def test1():
    tour = [[8, 6], 
    [1, 4], 
    [7, 6]]
    print("Circular tour :", circular_tour(tour, 3))
    print("Circular tour :", circular_tour2(tour, 3))


"""
Circular tour : 2
Circular tour : 2
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

# Testing Code
def test2():   
    print("3 to 4 Steps counter ::", convert_XY(3, 4))
    print("3 to 5 Steps counter ::", convert_XY(3, 5))
    print("3 to 6 Steps counter ::", convert_XY(3, 6))

"""
3 to 4 Steps counter :: 2
3 to 5 Steps counter :: 2
3 to 6 Steps counter :: 1
"""

def max_sliding_windows(arr,  k) :
    size = len(arr)
    for i in range(size - k + 1) :
        mx = arr[i]
        for j in range(1, k) :
            mx = max(mx,arr[i + j])
        print(mx, end =" ")
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

# Testing Code
def test3():
    arr = [11, 2, 75, 92, 59, 90, 55]
    k = 3
    max_sliding_windows(arr, k)
    max_sliding_windows2(arr, k)


"""
75 92 92 92 90
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

# Testing Code
def test4():
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
    print("Min of max is :", min_val)

# Testing Code
def test5():
    arr = [11, 2, 75, 92, 59, 90, 55]
    minofmax_sliding_windows(arr, 3)

"""
Min of max is : 75
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
    print("Max of min is :", max_val)


# Testing Code
def test6():
    arr = [11, 2, 75, 92, 59, 90, 55]
    maxofmin_sliding_windows(arr, 3)

"""     
Max of min is : 59
"""

def rotten_fruit_util(arr,  maxCol,  maxRow,  currCol,  currRow,  traversed,  day) :
    dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for i in range(4) :
        x = currCol + dir[i][0]
        y = currRow + dir[i][1]
        if (x >= 0 and x < maxCol and 
            y >= 0 and y < maxRow and 
            traversed[x][y] > day + 1 and arr[x][y] == 1) :
            traversed[x][y] = day + 1
            rotten_fruit_util(arr, maxCol, maxRow, x, y, traversed, day + 1)

def rotten_fruit(arr,  maxCol,  maxRow) :
    traversed = [[sys.maxsize] * (maxRow) for _ in range(maxCol)]
        
    for i in range(maxCol) :
        for j in range(maxRow) :
            if (arr[i][j] == 2) :
                traversed[i][j] = 0
                rotten_fruit_util(arr, maxCol, maxRow, i, j, traversed, 0)

    maxDay = 0
    for i in range(maxCol) :
        for j in range(maxRow) :
            if (arr[i][j] == 1) :
                if (traversed[i][j] == sys.maxsize) :
                    return  -1
                
                if (maxDay < traversed[i][j]) : 
                    maxDay = traversed[i][j]
    
    return  maxDay

def rotten_fruit2(arr,  maxCol,  maxRow) :
    traversed = [[False] * (maxRow) for _ in range(maxCol)]
    dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    que =  deque()
    for i in range( maxCol) :
        for j in range(maxRow) :
            if (arr[i][j] == 2) :
                que.append((i, j, 0))
                traversed[i][j] = True

    mx = 0
    while (len(que) > 0) :
        temp = que.popleft()
        for i in range(4) :
            x = temp[0] + dir[i][0]
            y = temp[1] + dir[i][1]
            day = temp[2] + 1
            if (x >= 0 and x < maxCol and y >= 0 and y < maxRow and arr[x][y] != 0 and traversed[x][y] == False) :
                que.append((x, y, day))
                mx = max(mx,day)
                traversed[x][y] = True

    for i in range(maxCol) :
        for j in range(maxRow) :
            if (arr[i][j] == 1 and traversed[i][j] == False) :
                return  -1

    return  mx

# Testing Code
def test7() :
    arr = [[1, 0, 1, 1, 0], [2, 1, 0, 1, 0], [0, 0, 0, 2, 1], [0, 2, 0, 0, 1], [1, 1, 0, 0, 1]]
    print("rotten_fruit : ", rotten_fruit(arr, 5, 5))
    print("rotten_fruit : ", rotten_fruit2(arr, 5, 5))

"""
Rotten Fruit : 3
Rotten Fruit : 3
"""

def steps_of_knight_util(size,  currCol,  currRow,  traversed,  dist) :
    dir = [[-2, -1], [-2, 1], [2, -1], [2, 1], [-1, -2], [1, -2], [-1, 2], [1, 2]]
    for i in range(8) :
        x = currCol + dir[i][0]
        y = currRow + dir[i][1]
        if (x >= 0 and x < size and y >= 0 and y < size and traversed[x][y] > dist + 1) :
            traversed[x][y] = dist + 1
            steps_of_knight_util(size, x, y, traversed, dist + 1)

def steps_of_knight(size,  srcX,  srcY,  dstX,  dstY) :
    traversed = [[sys.maxsize] * (size) for _ in range(size)]
    traversed[srcX - 1][srcY - 1] = 0
    steps_of_knight_util(size, srcX - 1, srcY - 1, traversed, 0)
    return  traversed[dstX - 1][dstY - 1]


def steps_of_knight2(size,  srcX,  srcY,  dstX,  dstY) :
    traversed = [[sys.maxsize] * (size) for _ in range(size)]
    dir = [[-2, -1], [-2, 1], [2, -1], [2, 1], [-1, -2], [1, -2], [-1, 2], [1, 2]]
    que =  deque()
    que.append((srcX - 1, srcY - 1, 0))
    traversed[srcX - 1][srcY - 1] = 0

    while (len(que) != 0) :
        temp = que.popleft()
        for i in range(8) :
            x = temp[0] + dir[i][0]
            y = temp[1] + dir[i][1]
            cost = temp[2] + 1
            if (x >= 0 and x < size and y >= 0 and y < size and traversed[x][y] > cost) :
                que.append((x, y, cost))
                traversed[x][y] = cost

    return  traversed[dstX - 1][dstY - 1]

# Testing Code
def test8() :
    print("steps_of_knight : ", steps_of_knight(20, 10, 10, 20, 20))
    print("steps_of_knight : ", steps_of_knight2(20, 10, 10, 20, 20))

"""
Steps of knight : 8
Steps of knight : 8
"""

def dist_nearest_fill_util(arr,  maxCol,  maxRow,  currCol,  currRow,  traversed,  dist) :
    #  Range check
    dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for i in range(4) :
        x = currCol + dir[i][0]
        y = currRow + dir[i][1]
        if (x >= 0 and x < maxCol and y >= 0 and y < maxRow and traversed[x][y] > dist + 1) :
            traversed[x][y] = dist + 1
            dist_nearest_fill_util(arr, maxCol, maxRow, x, y, traversed, dist + 1)

def dist_nearest_fill(arr,  maxCol,  maxRow) :
    traversed = [[sys.maxsize] * (maxRow) for _ in range(maxCol)]
    
    for i in range(maxCol) :
        for j in range(maxRow) :
            if (arr[i][j] == 1) :
                traversed[i][j] = 0
                dist_nearest_fill_util(arr, maxCol, maxRow, i, j, traversed, 0)
    
    for i in range(maxCol) :
        for j in range(maxRow) :
            print(traversed[i][j], end =" ")
        print()


def dist_nearest_fill2(arr,  maxCol,  maxRow) :
    traversed = [[sys.maxsize] * (maxRow) for _ in range(maxCol)]
    dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    que =  deque()

    for i in range(maxCol) :
        for j in range(maxRow) : 
            if (arr[i][j] == 1) :
                que.append((i, j, 0))
                traversed[i][j] = 0

    while (len(que) != 0) :
        temp = que.popleft()
        for i in range(4) :
            x = temp[0] + dir[i][0]
            y = temp[1] + dir[i][1]
            dist = temp[2] + 1
            if (x >= 0 and x < maxCol and y >= 0 and y < maxRow and traversed[x][y] > dist) :
                que.append((x, y, dist))
                traversed[x][y] = dist

    for i in range(maxCol) :
        for j in range(maxRow) :
            print(traversed[i][j], end =" ")
        print()

# Testing Code
def test9() :
    arr = [[1, 0, 1, 1, 0], [1, 1, 0, 1, 0], [0, 0, 0, 0, 1], [0, 0, 0, 0, 1], [0, 0, 0, 0, 1]]
    dist_nearest_fill(arr, 5, 5)
    dist_nearest_fill2(arr, 5, 5)
#    0 1 0 0 1 
#    0 0 1 0 1 
#    1 1 2 1 0 
#    2 2 2 1 0 
#    3 3 2 1 0

def reverse_stack(stk) :
    que =  deque()
    while len(stk) != 0 :
        que.append(stk[-1])
        stk.pop()
    while len(que) != 0 :
        stk.append(que.popleft())

def reverse_queue(que) :
    stk =  []
    while len(que) != 0 :
        stk.append(que.popleft())

    while len(stk) != 0 :
        que.append(stk[-1])
        stk.pop()

# Testing Code
def test10() :
    stk =  []
    for i in range(5) :
        stk.append(i)    
    print(stk)
    reverse_stack(stk)
    print(stk)

    que =  deque()
    for i in range( 5) :
        que.append(i)    
    print(que)
    reverse_queue(que)
    print(que)

def josephus(n,  k) :
    que =  deque()
    for i in range(n) :
        que.append(i + 1)    

    while (len(que) > 1) :
        for i in range(k - 1) :
            que.append(que.popleft())
        que.popleft()
    return  que[0]

# Testing Code
def test11() :
    print("Position :", josephus(11, 5))

"""
Position : 8
"""

test1()
test2()
test3()
test4()
test5()
test6()
test7()
test8()
test9()
test10()
test11()