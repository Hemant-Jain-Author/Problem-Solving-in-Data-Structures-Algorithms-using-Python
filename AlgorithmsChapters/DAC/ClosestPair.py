import math
import sys

class Point :
    def __init__(self, a,  b) :
        self.x = a
        self.y = b

def closestPairBF(arr) :
    n = len(arr)
    dmin = sys.maxsize
    for i in range (0, n - 1) :
        for j in range(i+1, n) :
            d = math.sqrt((arr[i][0] - arr[j][0]) * (arr[i][0] - arr[j][0]) + (arr[i][1] - arr[j][1]) * (arr[i][1] - arr[j][1]))
            if (d < dmin) :
                dmin = d
    return  dmin

def distance(a,  b) :
    return  math.sqrt((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y))

def stripMin(q,  n,  d) :
    min = d
    #  Find the distance between all the points in the strip. 
    #  Array q is sorted according to the y axis coordinate.
    #  The inner loop will run at most 6 times for each point.
    for i in range (0, n) :
        j = i + 1
        while (j < n and (q[j].y - q[i].y) < min) :
            d = distance(q[i], q[j])
            if (d < min) : 
                min = d
            j += 1
    return  min


def closestPairDCUtil(p,  start,  stop,  q,  n) :
    if (stop - start < 1) :
        return  sys.maxsize
    if (stop - start == 1) :
        return  distance(p[start], p[stop])

    mid = (start + stop) // 2  #  Find the middle point
    dl = closestPairDCUtil(p, start, mid, q, n)
    dr = closestPairDCUtil(p, mid + 1, stop, q, n)
    d = min(dl,dr)

    #  Build an list strip[] that contains points whose x axis coordinate
    #  in the range p[mid]-d and p[mid]+d
    #  Points are already sorted according to y axis.
    strip = [None] * n
    j = 0
    for i in range (0, n) :
        if (abs(q[i].x - p[mid].x) < d) :
            strip[j] = q[i]
            j += 1

    #  Find the closest points in strip and compare with d.
    return  min(d,stripMin(strip, j, d))


def closestPairDC(arr) :
    n = len(arr)
    p = [None] * n
    for i in range(0, n) :
        p[i] = Point(arr[i][0], arr[i][1])

    p.sort(key =  lambda a : a.x)#  Sort according to x axis.
    q = p.copy()
    q.sort(key = lambda  a : a.y) #  Sort according to y axis.
    return  closestPairDCUtil(p, 0, n - 1, q, n)

# Testing Code
arr = [[648, 896], [269, 879], [250, 922], [453, 347], [213, 17]]
print("Smallest distance is:", closestPairBF(arr))
print("Smallest distance is:", closestPairDC(arr))

"""
Smallest distance is: 47.01063709417264
Smallest distance is: 47.01063709417264
"""