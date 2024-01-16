
def andEx(a,  b) :
    return  a & b

def orEx(a,  b) :
    return  a | b

def xorEx(a,  b) :
    return  a ^ b

def leftShiftEx(a) : #  multiply by 2
    return  a << 1  

def rightShiftEx(a) : #  divide by 2
    return  a >> 1 

def bitReversalEx(a) :
    return  ~a

def twoComplementEx(a) :
    return  -a

def kthBitCheck(a,  k) :
    return  (a & 1 << (k - 1)) > 0

def kthBitSet(a,  k) :
    return  (a | 1 << (k - 1))

def kthBitReset(a,  k) :
    return  (a & ~(1 << (k - 1)))

def kthBitToggle(a,  k) :
    return  (a ^ (1 << (k - 1)))

def rightMostBit(a) :
    return  a & -a

def resetRightMostBit(a) :
    return  a & (a - 1)

def isPowerOf2(a) :
    if ((a & (a - 1)) == 0) :
        return  True
    else :
        return  False
    
def countBits(a) :
    count = 0
    while (a > 0) :
        count += 1
        a = a & (a - 1)
    return  count


# Testing Code
a = 4
b = 8
print(andEx(a, b))
print(orEx(a, b))
print(xorEx(a, b))
print(leftShiftEx(a)) # multiply by 2
print(rightShiftEx(a)) # divide by 2
print(bitReversalEx(a))
print(twoComplementEx(a))
print(kthBitCheck(a, 3))
print(kthBitSet(a, 2))
print(kthBitReset(a, 3))
print(kthBitToggle(a, 3))
print(rightMostBit(a))
print(resetRightMostBit(a))
print(isPowerOf2(a))
for i in range(10) :
    print(str(i) + " bit count : " + str(countBits(i)))    

"""
0
12
12
8
2
-5
-4
True
6
0
0
4
0
True
0 bit count : 0
1 bit count : 1
2 bit count : 1
3 bit count : 2
4 bit count : 1
5 bit count : 2
6 bit count : 2
7 bit count : 3
8 bit count : 1
9 bit count : 2
"""