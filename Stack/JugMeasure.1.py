"""
Let (X, Y) is a current state so their can be max 6 other states:
1: Second jug is emptied (X, 0)
2: First jug is emptied (0, Y)
3: First jug is completely filled (maxX, Y)
4: Second jug is completely filled (X, maxY)
5: Content of second jug added to first jug (min(maxX, X+Y), max(0, X+Y-maxX))
6: Content of first jug added to second jug (max(X+Y-maxY, 0), min(maxY, X+Y))
"""
def WaterJug(maxX, maxY, target) :
    stk = []
    parent = {}
    path = []

    start=(0,0,0)
    stk.append(start)
    parent[start] = start

    while len(stk) != 0:
        top = stk.pop()
        if top == (target, 0) or top == (0, target) :
            break
        X = top[0]
        Y = top[1]
        cost = top[2]
        if X < maxX :
            child = (maxX, Y, cost+1)
            if child not in parent:
                stk.append(child)
                parent[child] = top

        if Y < maxY :
            child = (X, maxY)
            if child not in parent :
                stk.append(child)
                parent[child] = top

        if X > 0 :
            child = (0, Y)
            if child not in parent :
                stk.append(child)
                parent[child] = top

        if Y > 0 :
            child = (X, 0)
            if child not in parent :
                stk.append(child)
                parent[child] = top

        # min(x + y, maxX), max(0, x + y - maxX)) if y > 0
        if Y > 0 :
            child = (min(X + Y, maxX), max(0, X + Y - maxX))
            if child not in parent :
                stk.append(child)
                parent[child] = top

        # max(0, x + y - maxY), min(x + y, maxY)) if x > 0
        if X > 0 :
            child = (max(0, X + Y - maxY), min(X + Y, maxY))
            if child not in parent :
                stk.append(child)
                parent[child] = top

    if top != (target, 0) and top != (0, target) :
        print "target not found"
        return []

    path.append(top)
    while parent[top] != top :
        path.insert(0, parent[top])
        top = parent[top]
    return path


print WaterJug(4, 3, 2)
print WaterJug(6, 1, 2)
print WaterJug(2, 9, 7)