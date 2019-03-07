"""
Let (X, Y) is a current state so their can be max 6 other states:
1: Second jug is emptied (X, 0)
2: First jug is emptied (0, Y)
3: First jug is completely filled (maxX, Y)
4: Second jug is completely filled (X, maxY)
5: Content of second jug added to first jug (min(maxX, X+Y), max(0, X+Y-maxX))
6: Content of first jug added to second jug (max(X+Y-maxY, 0), min(maxY, X+Y))


You need to produce an optimal path to reach target.

"""
import sys
def WaterJug(maxX, maxY, target) :
    stk = []
    parent = {}
    cost = {}
    path = []
    start=(0,0)
    stk.append(start)
    parent[start] = start
    cost[start] = 0
    ans = None
    ansCost = sys.maxsize

    while len(stk) != 0:
        top = stk.pop()
        if (top == (target, 0) or top == (0, target) ) and (cost[top] < ansCost) :
            ans = top
            ansCost = cost[top]

        X = top[0]
        Y = top[1]
        currCost = cost[top]
        if X < maxX :
            child = (maxX, Y)
            if child not in parent or currCost + 1 < cost[child]:
                stk.append(child)
                parent[child] = top
                cost[child] = currCost + 1

        if Y < maxY :
            child = (X, maxY)
            if child not in parent or currCost + 1 < cost[child]:
                stk.append(child)
                parent[child] = top
                cost[child] = currCost + 1

        if X > 0 :
            child = (0, Y)
            if child not in parent or currCost + 1 < cost[child]:
                stk.append(child)
                parent[child] = top
                cost[child] = currCost + 1

        if Y > 0 :
            child = (X, 0)
            if child not in parent or currCost + 1 < cost[child]:
                stk.append(child)
                parent[child] = top
                cost[child] = currCost + 1

        # min(x + y, maxX), max(0, x + y - maxX)) if y > 0
        if Y > 0 :
            child = (min(X + Y, maxX), max(0, X + Y - maxX))
            if child not in parent or currCost + 1 < cost[child]:
                stk.append(child)
                parent[child] = top
                cost[child] = currCost + 1

        # max(0, x + y - maxY), min(x + y, maxY)) if x > 0
        if X > 0 :
            child = (max(0, X + Y - maxY), min(X + Y, maxY))
            if child not in parent or currCost + 1 < cost[child]:
                stk.append(child)
                parent[child] = top
                cost[child] = currCost + 1

    if ans == None :
        print("target not found")
        return []

    path.append(ans)
    while parent[ans] != ans :
        path.insert(0, parent[ans])
        ans = parent[ans]
    return path


print(WaterJug(4, 3, 2))
print(WaterJug(6, 1, 2))
print(WaterJug(9, 2, 7))
print(WaterJug(12, 19, 7))