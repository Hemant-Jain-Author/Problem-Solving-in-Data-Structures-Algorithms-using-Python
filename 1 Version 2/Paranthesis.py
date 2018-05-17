
def isBalancedParenthesis(expn):
    stk = []
    for ch in expn:
        if ch == '{' or ch == '[' or ch == '(':
            stk.append(ch)
        elif ch == '}':
            if stk.pop() != '{':
                return False
        elif ch == ']':
            if stk.pop() != '[':
                return False
        elif ch == ')':
            if stk.pop() != '(':
                return False
    return len(stk) == 0



def main1():
    expn = "{()}[]"
    value = isBalancedParenthesis(expn)
    print("Given Expn:" , expn)
    print("Result after isParenthesisMatched:" , value)


def maxDepthParenthesis(expn):
    stk = []
    maxCount = 0
    count = 0
    for ch in expn:
        if ch == '(':
            stk.append(ch)
            count += 1
        elif ch == ')':
            stk.pop()
            count -= 1
        if count > maxCount :
            maxCount = count
    return maxCount

def main2():
    expn = "((((A)))((((BBB()))))()()()())"
    value = maxDepthParenthesis(expn)
    print("Given expn:" , expn)
    print("Max depth parenthesis is:" , value)

# main2()


def longestBalancedParenthesis(expn):
    stk = []
    count = 0
    for ch in expn:
        if ch == '(':
            stk.append(ch)
        elif ch == ')':
            if( len(stk) != 0 ):
                stk.pop()
                count += 2
    return count


def main3():
    expn = "())(())(())("
    value = longestBalancedParenthesis(expn)
    print("Given expn:" , expn)
    print("longest Balanced Parenthesis is:" , value)

#main3()

def longestContinousBalancedParenthesis(expn):
    stk = []
    count = 0
    maxCount = 0
    for ch in expn:
        if ch == '(':
            stk.append(ch)
        elif ch == ')':
            if( len(stk) != 0):
                stk.pop()
                count += 2
            else :
                count = 0
                stk = []
        if count > maxCount and len(stk) == 0:
            maxCount = count
    return maxCount

def main4():
    expn = "())((()))(())()(()()()())"
    value = longestContinousBalancedParenthesis(expn)
    print("Given expn:" , expn)
    print("longest Continous Balanced Parenthesis is:" , value)

#main4()

import math 

def reverseParenthesis(expn):
    stk = []
    if len(expn) % 2 == 1 :
        print("Invalid odd length : ", len(expn))
        return -1
    openCount = 0
    closeCount = 0
    for ch in expn:
        if ch == '(':
            stk.append(ch)
        elif ch == ')':
            if len(stk) != 0 and stk[-1] == '(':
                stk.pop()
            else :
                stk.append(')')
    while len(stk) != 0 :
        if stk.pop() == '(':
            openCount += 1
        else :
            closeCount += 1
    reversal = math.ceil (openCount / 2.0 ) + math.ceil(closeCount/2.0)
    """ when openCount is even closeCount is also even and 
    their half element reversal will make the expression balanced.
    when openCount is odd and also closeCount, then once you had reversed 
    openCount/2 and closeCount/2. You will be left with ")(" which need 2 more reversal
    above formula is drived from this.
    """
    return reversal

def main5():
    expn = "())((()))(())()(()()()()))"
    expn2 = ")(())((("
    value = reverseParenthesis(expn2)
    print("Given expn:" , expn2)
    print("reverse Parenthesis is:" , value)

main5()

def findDuplicateParenthesis(expn):
    stk = []
    for ch in expn:
        if ch == ')':
            if stk[-1] == '(' :
                return True
            while len(stk) != 0 :
                temp = stk.pop()
                if temp == '(' : 
                    break
        else :
            stk.append(ch)
    return False


def main6():
    expn = "(((a+(b))+(c+d)))"
    expn = "(((a+b))+c)"
    print("Given expn:" , expn)
    value = findDuplicateParenthesis(expn)
    print("Duplicate Found :" , value)

# main6()

def printParenthesisNumber(expn):
    stk = []
    output = []
    count = 1
    for ch in expn:
        if ch == '(':
            stk.append(count)
            output.append(count)
            count += 1
        elif ch == ')':
            output.append(stk.pop())

    print("Parenthesis Count :" , output)


def main7():
    expn1 = "(((a+(b))+(c+d)))"
    expn2 = "(((a+b))+c)((("
    print("Given expn:" , expn1)
    printParenthesisNumber(expn1)
    print("Given expn:" , expn2)
    printParenthesisNumber(expn2)

main7()
