import math
def ChotaBhim(cup):
    cups = cup
    size = len(cups)
    time = 60
    cups.sort(reverse=True)
    value = 0
    while time > 0:
        print cups
        value += cups[0]
        cups[0] = math.ceil(cups[0]/2.0)
        index = 0
        temp = cups[0]
        while index < size-1 and temp < cups[index + 1]:
            cups[index] = cups[index + 1]
            index += 1
        cups[index] = temp

        #cups.sort(reverse=True)
        time -= 1
    print value

def ChotaBhim2(cups):
    time = 60
    size = len(cups)
    cups.sort(reverse=True)
    value = 0
    while time > 0:
        value += cups[0]
        cups[0] = math.ceil(cups[0]/2.0)
        i = 0
        # Insert into proper location.
        while i < size-1 :
            if(cups[i] > cups[i+1]):
                 break
            temp = cups[i]
            cups[i] = cups[i+1]
            cups[i+1] = temp
            i += 1
        time -= 1
    print value

"""
this performance can be further improved by using a heap to store the cups. 
Each deletion will take logK time and each insertion will again take logK time 
so the final time complexity will be N.LogK
"""
cups = [2,1,7,4,2]
ChotaBhim(cups)
cups = [2,1,7,4,2]
ChotaBhim2(cups)


def JoinRope(ropes):
    ropes.sort(reverse=True)
    total = 0
    value = 0
    while len(ropes) >= 2:
        value = ropes.pop() + ropes.pop()
        ropes.append(value)
        total += value 
        index = len(ropes) - 1
        temp = ropes[-1]
        while index > 0 and ropes[index] < ropes[index - 1]:
            ropes[index] = ropes[index - 1]
            index -= 1
        ropes[index] = temp
        #ropes.sort(reverse=True)
    print total

"""
Performance of JoinRope can be improved by using insertion into proper possition approach.
so by doing this the complexity of the algorithm will O(n2)

Performance can be improved by using a heap to store values. Deletion and Insertion will take
O(LogN) time and finally the whole algorithm will be over in O(NlogN)
"""
import heapq
def JoinRope2(ropes):
    heapq.heapify(ropes)
    total = 0
    value = 0
    while len(ropes) > 1:
        value = heapq.heappop(ropes)
        value += heapq.heappop(ropes)
        heapq.heappush(ropes, value)
        total += value
    print total

"""
ropes = [4, 3, 2, 6]
JoinRope(ropes)
ropes = [4, 3, 2, 6]
JoinRope2(ropes)
"""