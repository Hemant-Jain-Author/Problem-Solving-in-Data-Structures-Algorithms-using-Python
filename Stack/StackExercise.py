import math
import sys

def function2() :
    print("Fun2 line 1")

def function1() :
    print("Fun1 line 1")
    function2()
    print("Fun1 line 2")

# Testing code
def main() :
    print("Main line 1")
    function1()
    print("Main line 2")

main()

"""
Main line 1
Fun1 line 1
Fun2 line 1
Fun1 line 2
Main line 2
"""

def is_balanced_parenthesis(expn):
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
    value = is_balanced_parenthesis(expn)
    print("Given Expn:" , expn)
    print("Result after isParenthesisMatched:" , value)

main1()

"""
Given Expn: {()}[]
Result after isParenthesisMatched: True
"""

def insert_at_bottom(stk, value):  # !!!!!!!!! waste for python.
    if len(stk) == 0:
        stk.append(value)
    else:
        temp = stk.pop()
        insert_at_bottom(stk, value)
        stk.append(temp)


def reverse_stack(stk):  # !!!!!!!!! waste for python.
    if len(stk) == 0:
        return
    else:
        value = stk.pop
        reverse_stack(stk)
        insert_at_bottom(stk, value)


def postfix_evaluate(expn):
    stk = []
    token_list = expn.split()

    for token in token_list:
        if token == '+':
            num1 = stk.pop()
            num2 = stk.pop()
            stk.append(num1 + num2)
        elif token == '-':
            num1 = stk.pop()
            num2 = stk.pop()
            stk.append(num1 - num2)
        elif token == '*':
            num1 = stk.pop()
            num2 = stk.pop()
            stk.append(num1 * num2)
        elif token == '/':
            num1 = stk.pop()
            num2 = stk.pop()
            stk.append(num1 / num2)
        else: 
            stk.append(int(token))
    return stk.pop()

def main2():
    expn = "6 5 2 3 + 8 * + 3 + *"
    value = postfix_evaluate(expn)
    print("Given Postfix Expn: " , expn)
    print("Result after Evaluation: " , value)

main2()

"""
Given Postfix Expn:  6 5 2 3 + 8 * + 3 + *
Result after Evaluation:  288
"""

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

def infix_to_postfix(expn):
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

def main4():
    expn = "10 + ( ( 3 ) ) * 5 / ( 16 - 4 )"
    value = infix_to_postfix(expn)
    print("Infix Expn: " , expn)
    print("Postfix Expn: " , value)

main4()

"""
Infix Expn:  10 + ( ( 3 ) ) * 5 / ( 16 - 4 )
Postfix Expn:   10 3 5 * 16 4 - / + 
"""

def reverse_string(expn):
    lower = 0
    upper = len(expn)
    newexp = ""
    while lower < upper:
        newexp += expn[upper - 1]
        upper -= 1
    return newexp

def replace_paranthesis(expn):
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

def infix_to_prefix(expn):
    expn = reverse_string(expn)
    expn = replace_paranthesis(expn)
    expn = infix_to_postfix(expn)
    expn = reverse_string(expn)
    return expn

def main3():
    expn = "10 + ( ( 3 ) ) * 5 / ( 16 - 4 )"
    value = infix_to_prefix(expn)
    print("Infix Expn: " , expn)
    print("Prefix Expn: " , value)

main3()

"""
Infix Expn:  10 + ( ( 3 ) ) * 5 / ( 16 - 4 )
Prefix Expn:  + 10 * 3 / 5 - 16 4 
"""

def stock_span_range(arr):
    stock_range = [0] * len(arr)
    stock_range[0] = 1
    i = 1
    size = len(arr)
    
    while i < size:
        stock_range[i] = 1
        j = i - 1
        while (j >= 0) and (arr[i] >= arr[j]):
            stock_range[i] += 1
            j -= 1
        i += 1
    return stock_range

def stock_span_range2(arr):
    stk = []
    size = len(arr)
    stock_range = [0] * size
    stk.append(0)
    stock_range[0] = 1
    i = 1
    while i < size:
        while len(stk) != 0 and arr[stk[len(stk) - 1]] <= arr[i]:
            stk.pop()
        if (len(stk) == 0):
            stock_range[i] = i + 1  
        else:
            stock_range[i] = i - stk[len(stk) - 1]
        stk.append(i)
        i += 1
    return stock_range

def main5():
    arr = [6, 5, 4, 3, 2, 4, 5, 7, 9]
    value = stock_span_range(arr)
    print("stock_span_range: " , value)
    value = stock_span_range2(arr)
    print("stock_span_range: " , value)

main5()

"""
stock_span_range:  [1, 1, 1, 1, 1, 4, 6, 8, 9]
stock_span_range:  [1, 1, 1, 1, 1, 4, 6, 8, 9]
"""

def get_max_area(arr):
    size = len(arr)
    max_area = -1
    min_height = 0
    i = 1
    while i < size:
        min_height = arr[i]
        j = i - 1
        while j >= 0:
            if min_height > arr[j]:
                min_height = arr[j]
            curr_area = min_height * (i - j + 1)
            if max_area < curr_area:
                max_area = curr_area
            j -= 1
        i += 1
    return max_area

def get_max_area2(arr):
    size = len(arr)
    stk = []
    max_area = 0
    i = 0
    while i < size:
        while (i < size) and (len(stk) == 0 or arr[stk[len(stk) - 1]] <= arr[i]):
            stk.append(i)
            i += 1
        while not len(stk) == 0 and (i == size or arr[stk[len(stk) - 1]] > arr[i]):
            top = stk[len(stk) - 1]
            stk.pop()
            top_area = arr[top] * (i if len(stk) == 0 else i - stk[len(stk) - 1] - 1)
            if max_area < top_area:
                max_area = top_area
    return max_area

def main6():
    arr = [7, 6, 5, 4, 4, 1, 6, 3, 1]
    print("get_max_area:", get_max_area(arr))
    print("get_max_area:", get_max_area2(arr))

main6()

"""
get_max_area: 20
get_max_area: 20
"""

def is_known(relation, a, b) :
    if relation[a][b] == 1 : 
        return True
    return False

def find_celebrity(relation, count):
    stk = []
    first, second = 0,0
    for i in range(count):
        stk.append(i)

    first = stk.pop()
    while len(stk) :
        second = stk.pop()
        if is_known(relation, first, second) :
            first = second
    
    for i in range(count):
        if first != i and is_known(relation, first, i) :
            return -1
        if first != i and is_known(relation,i, first) == False:
            return -1

    return first

def find_celebrity2(relation, count):
    stk = []
    first, second = 0, 0
    
    for i in range(1,count,1):
        if is_known(relation, first, i) :
            stk.append(i)

    while len(stk) :
        second = stk.pop()
        if is_known(relation, first, second) :
            first = second
    
    for i in range(count):
        if first != i and is_known(relation, first, i) :
            return -1
        if first != i and is_known(relation,i, first) == False:
            return -1

    return first


def find_celebrity3(relation, count):
    first, second = 0,1

    for i in range(count-1):
        if is_known(relation, first, second) :
            first = second
        second = second+1
    
    for i in range(count):
        if first != i and is_known(relation, first, i) :
            return -1
        if first != i and is_known(relation,i, first) == False:
            return -1

    return first

def main7():
    arr = [
        [ 1 , 0 , 1, 1 , 0], 
        [ 1 , 0 , 0, 1 , 0], 
        [ 0 , 0 , 1, 1 , 1], 
        [ 0 , 0 , 0, 1 , 0], 
        [ 1 , 1 , 0, 1 , 1]]
    print(find_celebrity(arr, 5))
    print(find_celebrity2(arr, 5))
    print(find_celebrity3(arr, 5))

main7()

"""
3
3
3
"""

def decode(text):
    n = len(text)
    value = 0
    output = ""
    stk = []
    for i in range(n):
        if text[i].isdigit() :
            value = value*10 + int(text[i])
        elif text[i] == '[':
            stk.append(value)
            value = 0
            stk.append('[')
        elif text[i] == ']' :
            st = ""
            temp = stk.pop()
            while temp != '[' :
                st = temp + st
                temp = stk.pop()

            count = stk.pop()
            st2 = ""
            for _ in range(count):
                st2 += st
            stk.append(st2)
        else :
            stk.append(text[i])

    while len(stk) != 0:
        output = stk.pop() + output
    return output

def main8():
    #str = '3[Z]'
    str = '1[x4[y]]13[Z]1[a]'
    print(decode(str))

main8()
"""
xyyyyZZZZZZZZZZZZZa
"""

def is_bst_array(preorder):
    stk = []
    root = -sys.maxsize
    for value in preorder:
        # If value of the right child is less then root.
        if value < root :
            return False
        # First left child values will be popped
        # Last popped value will be the root.
        while(len(stk) > 0 and stk[-1] < value) :
            root = stk.pop()
        # add current value to the stack.
        stk.append(value)
    return True

def main9(): 
    preorder1 = [30 , 20 , 25 , 70 , 200]
    print("Is BST Array" , is_bst_array(preorder1) )
    preorder2 = [30 , 20 , 25 , 10 , 70 , 200]
    print("Is BST Array" , is_bst_array(preorder2) )
    preorder3 = [30 , 20 , 35 , 30 ]
    print("Is BST Array" , is_bst_array(preorder3) )
    preorder4 = [30 , 20 , 35 , 29 ]
    print("Is BST Array" , is_bst_array(preorder4) )

main9()
"""
Is BST Array True
Is BST Array False
Is BST Array True
Is BST Array False
"""


def water_jug(maxX, maxY, target) :
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
        curr_cost = cost[top]
        if X < maxX :
            child = (maxX, Y)
            if child not in parent or curr_cost + 1 < cost[child]:
                stk.append(child)
                parent[child] = top
                cost[child] = curr_cost + 1

        if Y < maxY :
            child = (X, maxY)
            if child not in parent or curr_cost + 1 < cost[child]:
                stk.append(child)
                parent[child] = top
                cost[child] = curr_cost + 1

        if X > 0 :
            child = (0, Y)
            if child not in parent or curr_cost + 1 < cost[child]:
                stk.append(child)
                parent[child] = top
                cost[child] = curr_cost + 1

        if Y > 0 :
            child = (X, 0)
            if child not in parent or curr_cost + 1 < cost[child]:
                stk.append(child)
                parent[child] = top
                cost[child] = curr_cost + 1

        if Y > 0 :
            child = (min(X + Y, maxX), max(0, X + Y - maxX))
            if child not in parent or curr_cost + 1 < cost[child]:
                stk.append(child)
                parent[child] = top
                cost[child] = curr_cost + 1

        if X > 0 :
            child = (max(0, X + Y - maxY), min(X + Y, maxY))
            if child not in parent or curr_cost + 1 < cost[child]:
                stk.append(child)
                parent[child] = top
                cost[child] = curr_cost + 1

    if ans == None :
        print("target not found")
        return []

    path.append(ans)
    while parent[ans] != ans :
        path.insert(0, parent[ans])
        ans = parent[ans]
    return path

def main10():
    print(water_jug(4, 3, 2))
    print(water_jug(6, 1, 2))
    print(water_jug(9, 2, 7))
    print(water_jug(12, 19, 7))

main10()
"""
[(0, 0), (0, 3), (3, 0), (3, 3), (4, 2), (0, 2)]
[(0, 0), (0, 1), (1, 0), (1, 1), (2, 0)]
[(0, 0), (9, 0), (7, 2), (7, 0)]
[(0, 0), (0, 19), (12, 7), (0, 7)]
"""

def next_larger_element(arr):
    size = len(arr)
    output = []
    for i in range(0, size, 1):
        next = -1
        for j in range(i+1, size, 1):
            if arr[i] < arr[j]:
                next = arr[j]
                break
        output.append(next)
    print(output)

class Stack(object):
    def __init__(self):
        self.data = []     

    def size(self):
        return len(self.data)

    def is_empty(self):
        return (len(self.data) == 0)

    def push(self, value):
        self.data.append(value)

    def top(self):
        if self.is_empty():
            raise RuntimeError("StackEmptyException")
        return self.data[len(self.data) - 1]

    def pop(self):
        if self.is_empty():
            raise RuntimeError("StackEmptyException")
        return self.data.pop()

def next_larger_element2(arr):
    size = len(arr)
    stk = Stack()
    output = [-1]*size
    stk.push(arr[size - 1])
    output[size - 1] = -1
    i = size -2
    while i >= 0:
        while stk.is_empty() == False :
            top = stk.top()
            if top <= arr[i] :
                stk.pop()
            else :
                output[i] = top
                break
        
        if stk.is_empty() :
            output[i] = -1
        stk.push(arr[i])
        i -= 1
    print(output)

def next_larger_element3(arr):
    size = len(arr)
    stk = Stack()
    output = [-1]*size
    for i in range(size) :
        curr = arr[i]
        # stack always have values in decreasing order.
        while stk.is_empty() == False and arr[stk.top()] <= curr:
            index = stk.pop()
            output[index] = curr
        stk.push(i)
    
    # index which dont have any next Larger.
    while stk.is_empty() == False :
        index = stk.pop()
        output[index] = -1
        
    print(output)

# Testing code
def main11():
    arr = [13,21,3,6,20,3]
    next_larger_element(arr)
    next_larger_element2(arr)
    next_larger_element3(arr)

main11()
"""
[21, -1, 6, 20, -1, -1]
[21, -1, 6, 20, -1, -1]
[21, -1, 6, 20, -1, -1]
"""

def next_smaller_element(arr):
    size = len(arr)
    stk = Stack()
    output = [-1]*size
    stk.push(arr[size - 1])
    output[size - 1] = -1
    i = size -2
    while i >= 0:
        while stk.is_empty() == False :
            top = stk.top()
            if top >= arr[i] :
                stk.pop()
            else :
                output[i] = top
                break
        
        if stk.is_empty() :
            output[i] = -1
        stk.push(arr[i])
        i -= 1
    print(output)

def next_smaller_element2(arr):
    size = len(arr)
    stk = Stack()
    output = [-1]*size
    for i in range(size) :
        curr = arr[i]
        while stk.is_empty() == False and arr[stk.top()] > curr:
            index = stk.pop()
            output[index] = curr
        stk.push(i)
    # index which don't have any next Smaller.
    while stk.is_empty() == False :
        index = stk.pop()
        output[index] = -1
    print(output)

# Testing code
def main12():
    arr = [13,21,3,6,20,3]
    next_smaller_element(arr)
    next_smaller_element2(arr)
    
main12()
"""
[3, 3, -1, 3, 3, -1]
[3, 3, -1, 3, 3, -1]
"""


def next_larger_element_circular(arr) :
    size = len(arr)
    output = [-1] * size
    for i in range(size) :
        for j in range(1, size) :
            if (arr[i] < arr[(i + j) % size]) :
                output[i] = arr[(i + j) % size]
                break
    print(output)

def next_larger_element_circular2(arr):
    size = len(arr)
    stk = Stack()
    output = [-1]*size
    for i in range(2*size - 1) :
        curr = arr[i % size]
        # stack always have values in decreasing order.
        while stk.is_empty() == False and arr[stk.top()] <= curr:
            index = stk.pop()
            output[index] = curr
        stk.push(i % size)
    
    # index which don't have any next Larger.
    while stk.is_empty() == False :
        index = stk.pop()
        output[index] = -1  
    print(output)

def main13():
    arr = [6, 3, 9, 8, 10, 2, 1, 15, 7]
    next_larger_element_circular(arr)
    next_larger_element_circular2(arr)

main13()
"""
[9, 9, 10, 10, 15, 15, 15, -1, 9]
[9, 9, 10, 10, 15, 15, 15, -1, 9]
"""


def smallest_larger_element_array(arr):
    size = len(arr)
    output = []
    for i in range(size): 
        minDiff = sys.maxsize
        value = -1
        for j in range(size):
            if arr[i] < arr[j] and (arr[j] - arr[i] ) < minDiff :
                minDiff = arr[j] - arr[i]
                value = arr[j]
        output.append(value)
    print(output)

def smallest_larger_element_array2(arr):
    size = len(arr)
    output = [-1]*size
    aux = []
    for i in range(size) :
        aux.append((arr[i], i))
    aux.sort()
    
    for i in range(size-1) :
        output[aux[i][1]] = aux[i+1][0]
    output[aux[size - 1][1]] = -1
    print(output)

def main14():
    arr = [6, 3, 9, 8, 10, 2, 1, 15, 7]
    smallest_larger_element_array(arr)
    smallest_larger_element_array2(arr)

main14()
"""
[7, 6, 10, 9, 15, 3, 2, -1, 8]
[7, 6, 10, 9, 15, 3, 2, -1, 8]
"""

def find_leaders(arr):
    size = len(arr)
    stk = []
    for i in range(size) :
        curr = arr[i]
        # stack always have values in decreasing order.
        if len(stk) == 0 or stk[-1] > curr :
            stk.append(arr[i])
            continue
        while len(stk) != 0 and stk[-1] <= curr:
            stk.pop()
        stk.append(arr[i])
    print(stk)

def find_leaders2(arr):
    size = len(arr)
    largest = -sys.maxsize
    i = size -1
    output = []
    while i >= 0 :
        curr = arr[i]
        if largest < curr:
            largest = curr
            output.append(curr)
        i -= 1
    print(output)

def main15():
    arr = [16, 17, 4, 3, 5, 2]
    find_leaders(arr)
    find_leaders2(arr)

main15()
"""
[17, 5, 2]
[2, 5, 17]
"""

def is_balanced_parenthesis(expn):
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


def main16():
    expn = "{()}[]"
    value = is_balanced_parenthesis(expn)
    print("Given Expn:", expn)
    print("Result after isParenthesisMatched:", value)

main16()
"""
Given Expn: {()}[]
Result after isParenthesisMatched: True
"""

def max_depth_parenthesis(expn):
    stk = []
    max_depth = 0
    depth = 0
    for ch in expn:
        if ch == '(':
            stk.append(ch)
            depth += 1
        elif ch == ')':
            stk.pop()
            depth -= 1
        if depth > max_depth:
            max_depth = depth
    return max_depth


def max_depth_parenthesis2(expn):
    max_depth = 0
    depth = 0
    for ch in expn:
        if ch == '(':
            depth += 1
        elif ch == ')':
            depth -= 1
        if depth > max_depth:
            max_depth = depth
    return max_depth


def main17():
    expn = "((((A)))((((BBB()))))()()()())"
    print("Given expn:", expn)
    value = max_depth_parenthesis(expn)
    print("Max depth parenthesis is:", value)
    value = max_depth_parenthesis2(expn)
    print("Max depth parenthesis is:", value)


main17()
"""
Given expn: ((((A)))((((BBB()))))()()()())
Max depth parenthesis is: 6
Max depth parenthesis is: 6
"""

def longest_balanced_parenthesis(expn):
    stk = []
    count = 0
    for ch in expn:
        if ch == '(':
            stk.append(ch)
        elif ch == ')':
            if(len(stk) != 0):
                stk.pop()
                count += 2
    return count

def main18():
    expn = "())(())(())("
    value = longest_balanced_parenthesis(expn)
    print("Given expn:", expn)
    print("longest Balanced Parenthesis is:", value)

main18()
"""
Given expn: ())(())(())(
longest Balanced Parenthesis is: 10
"""

def longest_cont_bal_parenthesis(string):
    size = len(string)
    stk = []
    stk.append(-1)
    length = 0

    for i in range(size):
        if string[i] == '(':
            stk.append(i)
        elif string[i] == ')':
            stk.pop()
            if len(stk) == 0:
                stk.append(i)
            else:
                length = max(length, i - stk[-1])
    return length

def main19():
    expn = "())((()))(())()(()((()))((()))"    
    value = longest_cont_bal_parenthesis(expn)
    print("Longest Continuous Balanced Parenthesis is:", value)

main19()
"""
Given expn: ())((()))(())()(()
Longest Continuous Balanced Parenthesis is: 14
"""

def reverse_parenthesis(expn):
    stk = []
    if len(expn) % 2 == 1:
        print("Invalid odd length : ", len(expn))
        return -1
    open_count = 0
    close_count = 0
    for ch in expn:
        if ch == '(':
            stk.append(ch)
        elif ch == ')':
            if len(stk) != 0 and stk[-1] == '(':
                stk.pop()
            else:
                stk.append(')')
    while len(stk) != 0:
        if stk.pop() == '(':
            open_count += 1
        else:
            close_count += 1
    
    reversal = math.ceil(open_count / 2) + math.ceil(close_count / 2) # fractional division.
    return reversal

def main20():
    expn = "())((()))(())()(()()()()))"
    expn2 = ")(())((("
    value = reverse_parenthesis(expn2)
    print("Given expn:", expn2)
    print("reverse Parenthesis is:", value)

main20()
"""
Given expn: )(())(((
reverse Parenthesis is: 3
"""

def find_duplicate_parenthesis(expn):
    stk = []
    for ch in expn:
        if ch == ')':
            count = 0
            while len(stk) != 0 and stk[-1] != '(':
                stk.pop()
                count += 1
            if count <= 1:
                return True
        else:
            stk.append(ch)

    return False

def find_duplicate_parenthesis2(expn):
	stk = []
	for ch in expn:
		# close parenthesis ')'
		if ch == ')':
			# pop character from the stack
			top = stk.pop()

			# If there are less then 2 elements between paranthesis pair then 
            # the paranthesis is redundant.
			count = 0
			while top != '(':
				count += 1
				top = stk.pop()

			if(count <= 1) :
				return True
		else:
			stk.append(ch)

	return False

def main21():
    expn = "(((a+(b))+(c+d)))"
    print("Given expn:", expn)
    value = find_duplicate_parenthesis(expn)
    print("Duplicate Found :", value)

main21()
"""
Given expn: (((a+(b))+(c+d)))
Duplicate Found : True
"""

def print_parenthesis_number(expn):
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

    print("Parenthesis Count :", output)

def main22():
    expn1 = "(((a+(b))+(c+d)))"
    expn2 = "(((a+b))+c)((("
    print("Given expn:", expn1)
    print_parenthesis_number(expn1)
    print("Given expn:", expn2)
    print_parenthesis_number(expn2)

main22()
"""
Given expn: (((a+(b))+(c+d)))
Parenthesis Count : [1, 2, 3, 4, 4, 3, 5, 5, 2, 1]
Given expn: (((a+b))+c)(((
Parenthesis Count : [1, 2, 3, 3, 2, 1, 4, 5, 6]
"""

def print_number_pattern(expr):
    size = len(expr)
    output = [-1]*(size+1)
    val = 1
    count = 0

    for i in range(size) :
        curr = expr[i]
        if curr == 'D':
            count += 1
        elif curr == 'I':
            if count == 0:
                output[i] = val
                val += 1
                continue
            for j in range(count+1) :
                output[i - j] = val
                val += 1
            count = 0

    i = size
    for j in range(count+1):
        output[i - j] = val
        val += 1
    
    print(output)

def main23():
    print_number_pattern("DIDD")
    print_number_pattern("DDIDDIID")

main23()
"""
[2, 1, 5, 4, 3]
[3, 2, 1, 6, 5, 4, 7, 9, 8]
"""

class Stack(object):
    def __init__(self):
        self.data = []     

    def size(self):
        return len(self.data)

    def is_empty(self):
        return (len(self.data) == 0)

    def push(self, value):
        self.data.append(value)

    def top(self):
        if self.is_empty():
            raise RuntimeError("StackEmptyException")
        return self.data[len(self.data) - 1]

    def pop(self):
        if self.is_empty():
            raise RuntimeError("StackEmptyException")
        return self.data.pop()

    def print(self):
        print(self.data)

def sorted_insert(stk, element) :
    if stk.is_empty() or element > stk.top() :
        stk.push(element)
    else :
        temp = stk.pop()
        sorted_insert(stk, element)
        stk.push(temp)

def main24():
    stk = Stack()
    sorted_insert(stk, 4)
    sorted_insert(stk, 2)
    sorted_insert(stk, 3)
    sorted_insert(stk, 1)
    stk.print()

main24()
"""
[1, 2, 3, 4]
"""

def sort_stack(stk):
    if stk.is_empty() == False :
        temp = stk.pop()
        sort_stack(stk)
        sorted_insert(stk, temp)

def sort_stack2(stk):
    stk2 = Stack()
    while stk.is_empty() == False :
        temp = stk.pop()
        while stk2.is_empty() == False and stk2.top() < temp :
            stk.push(stk2.pop())
        stk2.push(temp)

    while stk2.is_empty() == False :
        stk.push(stk2.pop())

def main24():
    stk = Stack()
    stk.push(4)
    stk.push(2)
    stk.push(3)
    stk.push(1)
    sort_stack(stk)
    stk.print()

    stk = Stack()
    stk.push(4)
    stk.push(2)
    stk.push(3)
    stk.push(1)
    sort_stack2(stk)
    stk.print()

main24()
"""
[1, 2, 3, 4]
[1, 2, 3, 4]
"""

def bottom_insert(stk, element) :
    if stk.is_empty() :
        stk.push(element)
    else :
        temp = stk.pop()
        bottom_insert(stk, element)
        stk.push(temp)

def main24():
    stk = Stack()
    stk.push(1)
    stk.push(2)
    stk.push(3)
    bottom_insert(stk, 0)
    stk.print()

main24()
"""
[0, 1, 2, 3]
"""

def reverse_stack(stk):
    if stk.is_empty() == False :
        temp = stk.pop()
        reverse_stack(stk)
        bottom_insert(stk, temp)


from collections import deque
class Queue(object):    
    def __init__(self):
        self.data = deque([])

    def add(self, value):
        self.data.append(value)

    def remove(self):
        value = self.data.popleft()
        return value
    
    def is_empty(self):
        return (len(self.data) == 0)

    def size(self):
        return len(self.data)
    
    def print(self):
        print(self.data)

def reverse_stack2(stk):
    que = Queue()
    while stk.is_empty() == False :
        que.add(stk.pop())

    while que.is_empty() == False :
        stk.push(que.remove())


def main24():
    stk = Stack()
    stk.push(1)
    stk.push(2)
    stk.push(3)
    reverse_stack(stk)
    stk.print()

    stk = Stack()
    stk.push(1)
    stk.push(2)
    stk.push(3)
    reverse_stack2(stk)
    stk.print()


main24()
"""
[3, 2, 1]
[3, 2, 1]
"""


def reverse_Kelement_in_stack(stk, k):
    que = Queue()
    i = 1
    while stk.is_empty() == False and i <= k:
        que.add(stk.pop())
        i += 1

    while que.is_empty() == False :
        stk.push(que.remove())

def reverse_queue(que):
    stk = Stack()
    while que.is_empty() == False :
        stk.push(que.remove())

    while stk.is_empty() == False :
        que.add(stk.pop())

def reverse_Kelement_in_queue(que, k):
    stk = Stack()
    i = 1
    while que.is_empty() == False and i <= k:
        stk.push(que.remove())
        i += 1

    while stk.is_empty() == False :
        que.add(stk.pop())

    diff = que.size() - k
    while diff > 0 :
        temp = que.remove()
        que.add(temp)
        diff -= 1

def main24():
    stk = Stack()
    stk.push(1)
    stk.push(2)
    stk.push(3)
    stk.print()
    reverse_Kelement_in_stack(stk, 2)
    stk.print()

    que = Queue()
    que.add(1)
    que.add(2)
    que.add(3)
    que.print()
    reverse_queue(que)
    que.print()

    que = Queue()
    que.add(1)
    que.add(2)
    que.add(3)
    que.print()
    reverse_Kelement_in_queue(que, 2)
    que.print()

main24()
"""
[1, 2, 3]
[1, 3, 2]
deque([1, 2, 3])
deque([3, 2, 1])
deque([1, 2, 3])
deque([2, 1, 3])
"""

def get_max_area(arr):
	size = len(arr)
	maxArea = -1
	minHeight = 0
	for i in range(1, size):
		minHeight = arr[i]
		j = i - 1
		for j in range(i-1, -1, -1):
			if minHeight > arr[j]:
				minHeight = arr[j]
			currArea = minHeight * (i - j + 1)
			if maxArea < currArea:
				maxArea = currArea
	return maxArea

def get_max_area2(arr):
	size = len(arr)
	stk = []
	maxArea = 0
	i = 0
	while i < size:
		while (i < size) and (len(stk) == 0 or arr[stk[-1]] <= arr[i]):
			stk.append(i)
			i += 1
		while len(stk) != 0 and (i == size or arr[stk[-1]] > arr[i]):
			top = stk[-1]
			stk.pop()
			topArea = arr[top] * (i if len(stk) == 0 else i-stk[-1]-1)
			if maxArea < topArea:
				maxArea = topArea
	return maxArea



# Testing code
def main25():
    arr = [7, 6, 5, 4, 4, 1, 6, 3, 1]
    print("get_max_area: " , get_max_area(arr))
    print("get_max_area: " , get_max_area2(arr))

main25()
"""
get_max_area:  20
get_max_area:  20
"""

def rotten_fruit_util (arr, max_col, max_row, curr_col, curr_row, traversed, day):
    # Range check
    if curr_col < 0 or curr_col >= max_col or curr_row < 0 or curr_row >= max_row :
        return
    # Traversable and rot if not already rotten.
    if traversed[curr_col][curr_row] <= day or arr[curr_col][curr_row] == 0:
        return
    # Update rot time.
    traversed[curr_col][curr_row] = day
    # each line corresponding to 4 direction.
    rotten_fruit_util (arr, max_col, max_row, curr_col-1, curr_row, traversed, day+1)
    rotten_fruit_util (arr, max_col, max_row, curr_col+1, curr_row, traversed, day+1)
    rotten_fruit_util (arr, max_col, max_row, curr_col, curr_row+1, traversed, day+1)
    rotten_fruit_util (arr, max_col, max_row, curr_col, curr_row-1, traversed, day+1)


def rotten_fruit(arr, max_col, max_row):
    infi = sys.maxsize
    traversed = [[infi]*max_col for i in range(max_row)]
    for i in range(0, max_col-1, 1):
        for j in range(0, max_row-1, 1):
            if arr[i][j] == 2:
                rotten_fruit_util (arr, max_col, max_row, i, j, traversed, 0)
    max_day = 0
    for i in range(0, max_col, 1):
        for j in range(0, max_row, 1):
            if arr[i][j] == 1 : 
                if traversed[i][j] == infi :
                    return -1
                if max_day < traversed[i][j]:
                    max_day = traversed[i][j]
    return max_day

def main():
    arr = [
        [ 1, 1, 1, 1, 0], 
        [ 1, 1, 0, 1, 0], 
        [ 0, 0, 0, 2, 1], 
        [ 0, 2, 0, 0, 1], 
        [ 1, 1, 0, 0, 1]]
    print(rotten_fruit(arr, 5, 5))

main()
"""
6
"""

def dist_nearest_fill_util(arr, max_col, max_row, curr_col, curr_row, traversed, dist):
    # Range check
    if curr_col < 0 or  curr_col >= max_col or curr_row < 0 or curr_row >= max_row :
        return
    # Traversable if their is a better distance.
    if traversed[curr_col][curr_row] <= dist :
        return
    # Update distance.
    traversed[curr_col][curr_row] = dist
    # each line corresponding to 4 direction.
    dist_nearest_fill_util(arr, max_col, max_row, curr_col-1, curr_row, traversed, dist+1)
    dist_nearest_fill_util(arr, max_col, max_row, curr_col+1, curr_row, traversed, dist+1)
    dist_nearest_fill_util(arr, max_col, max_row, curr_col, curr_row+1, traversed, dist+1)
    dist_nearest_fill_util(arr, max_col, max_row, curr_col, curr_row-1, traversed, dist+1)

infi = sys.maxsize
def dist_nearest_fill(arr, max_col, max_row):
    traversed = [[infi]*max_col for i in range(max_row)]
    for i in range(0, max_col, 1):
        for j in range(0, max_row, 1):
            if arr[i][j] == 1:
                dist_nearest_fill_util(arr, max_col, max_row, i, j, traversed, 0)
    print(traversed)

def main2():
    arr = [
        [ 1 , 0 , 1, 1 , 0], 
        [ 1 , 1, 0, 1 , 0], 
        [ 0 , 0 , 0, 0 , 1], 
        [ 0 , 0 , 0, 0 , 1], 
        [ 0 , 0 , 0, 0 , 1]]
    dist_nearest_fill(arr, 5, 5)

main2()
"""
[[0, 1, 0, 0, 1], [0, 0, 1, 0, 1], [1, 1, 2, 1, 0], [2, 2, 2, 1, 0], [3, 3, 2, 1, 0]]
"""

def steps_of_knight_util(size, curr_col, curr_row, traversed, dist):
    # Range check
    if curr_col < 0 or curr_col >= size or curr_row < 0 or curr_row >= size :
        return
    # Traversable and rot if not already rotten.
    if traversed[curr_col][curr_row] <= dist :
        return
    # Update rot time.
    traversed[curr_col][curr_row] = dist
    # each line corresponding to 4 direction.
    steps_of_knight_util(size, curr_col-2, curr_row-1, traversed, dist+1)
    steps_of_knight_util(size, curr_col-2, curr_row+1, traversed, dist+1)
    steps_of_knight_util(size, curr_col+2, curr_row-1, traversed, dist+1)
    steps_of_knight_util(size, curr_col+2, curr_row+1, traversed, dist+1)
    steps_of_knight_util(size, curr_col-1, curr_row-2, traversed, dist+1)
    steps_of_knight_util(size, curr_col+1, curr_row-2, traversed, dist+1)
    steps_of_knight_util(size, curr_col-1, curr_row+2, traversed, dist+1)
    steps_of_knight_util(size, curr_col+1, curr_row+2, traversed, dist+1)

infi = sys.maxsize
def steps_of_knight(size, srcX, srcY, dstX, dstY):
    traversed = [[infi]*size for _ in range(size)]
    steps_of_knight_util(size, srcX - 1, srcY - 1, traversed, 0)
    return traversed[dstX - 1][dstY - 1]

print(steps_of_knight(20,10,10,20,20))
"""
8
"""


def find_largest_island_util(arr, max_col, max_row, curr_col, curr_row, value, traversed) :
    if curr_col < 0 or curr_col >= max_col or curr_row < 0 or curr_row >= max_row :
        return 0
    if traversed[curr_col][curr_row] == 1 or arr[curr_col][curr_row] != value :
        return 0
    traversed[curr_col][curr_row] = 1

    # each call corresponding to 8 direction.
    return 1 + find_largest_island_util(arr, max_col, max_row, curr_col - 1, curr_row - 1, value, traversed) + find_largest_island_util(arr, max_col, max_row, curr_col - 1, curr_row, value, traversed) + find_largest_island_util(arr, max_col, max_row, curr_col - 1, curr_row + 1, value, traversed) + find_largest_island_util(arr, max_col, max_row, curr_col, curr_row - 1, value, traversed) + find_largest_island_util(arr, max_col, max_row, curr_col, curr_row + 1, value, traversed) + find_largest_island_util(arr, max_col, max_row, curr_col + 1, curr_row - 1, value, traversed) + find_largest_island_util(arr, max_col, max_row, curr_col + 1, curr_row, value, traversed) + find_largest_island_util(arr, max_col, max_row, curr_col + 1, curr_row + 1, value, traversed)

def find_largest_island(arr, max_col, max_row):
    maxVal = 0
    currVal = 0
    traversed = [[infi]*max_col for i in range(max_row)]

    for i in range(max_col):
        for j in range(max_row):
            currVal = find_largest_island_util(arr, max_col, max_row, i, j, arr[i][j], traversed)
            if currVal > maxVal :
                maxVal = currVal

    return maxVal

def main19():
    arr = [[1, 0, 1, 1, 0], [1, 0, 0, 1, 0], [0, 1, 1, 1, 1 ], [ 0, 1, 0, 0, 0], [1, 1, 0, 0, 1]]
    print("Largest Island : " , find_largest_island(arr, 5, 5))

main19()
"""
Largest Island :  12
"""


def stockAnalystAdd(stk,  value) :
    while (not (len(stk) == 0) and stk[-1] <= value) :
        stk.pop()
    stk.append(value)
def main7a() :
    arr = [20, 19, 10, 21, 40, 35, 39, 50, 45, 42]
    stk =  []
    i = len(arr) - 1
    while (i >= 0) :
        stockAnalystAdd(stk, arr[i])    
        i -= 1
    print(stk)

main7a()
"""
[50, 40, 21, 20]
"""