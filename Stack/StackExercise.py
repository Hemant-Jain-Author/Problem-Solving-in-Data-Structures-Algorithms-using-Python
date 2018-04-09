#!/usr/bin/env python

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


def insertAtBottom(stk, value):  # !!!!!!!!! waste for python.
    if len(stk) == 0:
        stk.append(value)
    else:
        temp = stk.pop()
        insertAtBottom(stk, value)
        stk.append(temp)


def reverseStack(stk):  # !!!!!!!!! waste for python.
    if len(stk) == 0:
        return
    else:
        value = stk.pop
        reverseStack(stk)
        insertAtBottom(stk, value)


def postfixEvaluate(expn):
    stk = []
    token_list = expn.split()

    for token in token_list:
        if token == '+':
            num1 = stk.pop();
            num2 = stk.pop();
            stk.append(num1 + num2)
        elif token == '-':
            num1 = stk.pop();
            num2 = stk.pop();
            stk.append(num1 - num2)
        elif token == '*':
            num1 = stk.pop();
            num2 = stk.pop();
            stk.append(num1 * num2)
        elif token == '/':
            num1 = stk.pop();
            num2 = stk.pop();
            stk.append(num1 / num2)
        else: 
            stk.append(int(token))
    return stk.pop()


def main2():
    expn = "6 5 2 3 + 8 * + 3 + *"
    value = postfixEvaluate(expn)
    print("Given Postfix Expn: " , expn)
    print("Result after Evaluation: " , value)


def precedence(x):
    if x == '(':
        return (0)
    if x == '+' or x == '-':
        return (1)
    if x == '*' or x == '/' or x == '%':
        return (2)
    if x == '^':
        return (3)
    return (4)



def infixToPostfix(expn):
    stk = []
    token_list = expn.split()
    output = ""
    for token in token_list:
        if token in '+-*/^':
            while len(stk) != 0 and precedence(token) <= precedence(stk[len(stk) - 1]):
                outsrt = stk.pop()
                output = output + " " + outsrt
            stk.append(token)
        elif token == '(':
            stk.append(token)
        elif token == ')':
            outsrt = None
            while len(stk) != 0 and outsrt != '(':
                outsrt = stk.pop()
                if outsrt != '(' :
                    output = output + " " + outsrt
        else :
            output = output + " " + token
        
    while len(stk) != 0:
        outsrt = stk.pop()
        output = output + " " + outsrt
    return output


def main3():
    expn = "10 + ( ( 3 ) ) * 5 / ( 16 - 4 )"
    # value = infixToPostfix(expn)
    value = infixToPrefix(expn)
    print("Infix Expn: " , expn)
    print("Postfix Expn: " , value)


def infixToPrefix(expn):
    expn = reverseString(expn)
    expn = replaceParanthesis(expn)
    expn = infixToPostfix(expn)
    expn = reverseString(expn)
    return expn


def replaceParanthesis(expn):
    lower = 0
    upper = len(expn)
    newexp = ""
    while lower < upper:
        if expn[lower] == '(':
            newexp += ')'
        elif expn[lower] == ')':
            newexp += '('
        else:
            newexp += expn[lower]
        lower += 1
    return newexp


def reverseString(expn):
    lower = 0
    upper = len(expn)
    newexp = ""
    while lower < upper:
        newexp += expn[upper - 1]
        upper -= 1
    return newexp


def main4():
    expn = "10+((3))*5/(16-4)"
    value = infixToPrefix(expn)
    print("Infix Expn: " , expn)
    print("Prefix Expn: " , value)


def StockSpanRange(arr):
    SR = [0] * len(arr)
    SR[0] = 1
    i = 1
    size = len(arr)
    
    while i < size:
        SR[i] = 1
        j = i - 1
        while (j >= 0) and (arr[i] >= arr[j]):
            SR[i] += 1
            j -= 1
        i += 1
    return SR


def main5():
    arr = [6, 5, 4, 3, 2, 4, 5, 7, 9]
    value = StockSpanRange2(arr)
    print("StockSpanRange: " , value)



def StockSpanRange2(arr):
    stk = []
    size = len(arr)
    SR = [0] * size
    stk.append(0)
    SR[0] = 1
    i = 1
    while i < size:
        while len(stk) != 0 and arr[stk[len(stk) - 1]] <= arr[i]:
            stk.pop()
        if (len(stk) == 0):
            SR[i] = i + 1  
        else:
            SR[i] = i - stk[len(stk) - 1]
        stk.append(i)
        i += 1
    return SR



def GetMaxArea(arr):
    size = len(arr)
    maxArea = -1
    minHeight = 0
    i = 1
    while i < size:
        minHeight = arr[i]
        j = i - 1
        while j >= 0:
            if minHeight > arr[j]:
                minHeight = arr[j]
            currArea = minHeight * (i - j + 1)
            if maxArea < currArea:
                maxArea = currArea
            j -= 1
        i += 1
    return maxArea


def GetMaxArea2(arr):
    """ generated source for method GetMaxArea2 """
    size = len(arr)
    stk = []
    maxArea = 0
    i = 0
    while i < size:
        while (i < size) and (len(stk) == 0 or arr[stk[len(stk) - 1]] <= arr[i]):
            stk.append(i)
            i += 1
        while not len(stk) == 0 and (i == size or arr[stk[len(stk) - 1]] > arr[i]):
            top = stk[len(stk) - 1]
            stk.pop()
            topArea = arr[top] * (i if len(stk) == 0 else i - stk[len(stk) - 1] - 1)
            if maxArea < topArea:
                maxArea = topArea
    return maxArea


def main6():
    arr = [7, 6, 5, 4, 4, 1, 6, 3, 1]
    value = GetMaxArea2(arr)
    print("GetMaxArea: " , value)

main1()
main2()
main3()
main4()
main5()
main6()

