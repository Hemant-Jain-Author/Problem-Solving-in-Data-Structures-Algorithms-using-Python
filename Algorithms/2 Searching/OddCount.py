"""
Given an array find the elements which appear odd number of times.
"""
def OddCount(arr):
    size = len(arr)
    hs = {}
    for i in range(size):
        if arr[i] in hs :
            hs[arr[i]] += 1
        else:
            hs[arr[i]] = 1

    for key in hs:
        if hs[key] % 2 == 1:
            print key ,

"""
Given an array in which all the elements appear even number of times except two 
which appear odd number of times.
find the elements which appear odd number of times.
"""
def OddCount2(arr):
    size = len(arr)
    # xor of all elements in arr[]
    # even occurance will cancel each other.
    # sum will contain sum of two odd elements.
    
    xorSum = 0
    for i in range(size):
        xorSum = xorSum ^ arr[i]
    
    # Rightmost set bit.
    setBit = xorSum & ~(xorSum - 1)
    
    # Dividing elements in two group: 
    # Elements having setBit bit as 1.
    # Elements having setBit bit as 0.
    # Even elements cancelled themself if group and we get our numbers.
    first, second = 0, 0
    for i in range(size):
        if(arr[i] & setBit):
            first = first ^ arr[i]
        else:
            second = second ^ arr[i] 

    print (first, "&", second)
 

arr = [10, 25, 30, 10, 15, 25, 15, 40]
OddCount(arr)
OddCount2(arr)


def RepeatedMissing(arr):
    size = len(arr)
    # xor of all elements in arr[]
    # even occurance will cancel each other.
    # sum will contain sum of two odd elements.
    
    xorSum = 0
    for i in range(size):
        xorSum = xorSum ^ (i+1)
        xorSum = xorSum ^ arr[i]
    
    # Rightmost set bit.
    setBit = xorSum & ~(xorSum - 1)
    
    # Dividing elements in two group: 
    # Elements having setBit bit as 1.
    # Elements having setBit bit as 0.
    # Even elements cancelled themself if group and we get our numbers.
    first, second = 0, 0
    for i in range(size):
        if(arr[i] & setBit):
            first = first ^ arr[i]
        else:
            second = second ^ arr[i]

        if((i+1) & setBit):
            first = first ^ (i+1)
        else:
            second = second ^ (i+1) 
    found = False
    for i in range(size):
        if(first == arr[i]):
            found = True
            break

    if found == True:
        print "Repeated element ::", first
        print "Missing element ::", second
    else:
        print "Repeated element ::", second
        print "Missing element ::", first

    
arr = [1, 3, 6, 5, 4, 1]
RepeatedMissing(arr)
