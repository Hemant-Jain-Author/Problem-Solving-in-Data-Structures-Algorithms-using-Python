"""
Chota bhim had visited his meternal grandfather takshak. 
Takshak had offered bhim to drink elixir of power. 
He had offered number of cups filled with different quantity of elixir. 
Bhim is instructed to drink maximum quantity of elixir from the cups.
The cups are magical when bhim drink from a cup, it refill itself with half the previous quantity it uses ceil [ previous amont / 2 ] function to fill itself.
Bhim is given 1 munutes time. He is efficient, in each second he drink from one cup and puts it back.
Bhim had consumed lot of elixir by always picking the cup with maxumum elixir.
Now takshak had called you to find how much he had consumed.
5 Cups
2,1,7,4,2

>> 7
2 1 4 4 2
>> 4 two times
2 1 2 2 2
>> 2 four times
1 1 1 1 1
>> rest all 1

7+4+4+2+2+2+2+(60 - 7)
76 units of elixir
"""
import math
def ChotaBhim(cups):
    time = 60
    cups.sort(reverse=True)
    value = 0
    while time > 0:
        value += cups[0]
        cups[0] = math.ceil(cups[0]/2.0)
        cups.sort(reverse=True)
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
#ChotaBhim2(cups)


def JoinRope(ropes):
    ropes.sort(reverse=True)
    value = 0
    while len(ropes) >= 2:
        sumTwo = ropes.pop() + ropes.pop()
        ropes.append(sumTwo)
        value += sumTwo 
        ropes.sort(reverse=True)
    print value

ropes = [4, 3, 2, 6]
JoinRope(ropes)

"""
Performance of JoinRope can be improved by using insertion into proper possition approach.
so by doing this the complexity of the algorithm will O(n2)

Performance can be improved by using a heap to store values. Deletion and Insertion will take
O(LogN) time and finally the whole algorithm will be over in O(NlogN)
"""