def isKnown(relation, a, b) :
    if relation[a][b] == 1 : 
        return True
    return False

def findCelebrity(relation, count):
    stk = []
    first, second = 0,0
    for i in range(count):
        stk.append(i)

    first = stk.pop()
    while len(stk) :
        second = stk.pop()
        if isKnown(relation, first, second) :
            first = second
    
    for i in range(count):
        if first != i and isKnown(relation, first, i) :
            return -1
        if first != i and isKnown(relation,i, first) == False:
            return -1

    return first

def findCelebrity2(relation, count):
    stk = []
    first, second = 0,0
    
    for i in range(1,count,1):
        if isKnown(relation, first, i) :
            stk.append(i)

    while len(stk) :
        second = stk.pop()
        if isKnown(relation, first, second) :
            first = second
    
    for i in range(count):
        if first != i and isKnown(relation, first, i) :
            return -1
        if first != i and isKnown(relation,i, first) == False:
            return -1

    return first

def main():
    arr = [
        [ 1 , 0 , 1, 1 , 0], 
        [ 1 , 0 , 0, 1 , 0], 
        [ 0 , 0 , 1, 1 , 1], 
        [ 0 , 0 , 0, 0 , 0], 
        [ 1 , 1 , 0, 1 , 1]]
    print(findCelebrity(arr, 5))
    print(findCelebrity2(arr, 5))

main()