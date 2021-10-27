import sys

value1 = sys.maxsize
value2 = value1 + 1
value3 = 13.05
value4 = 3.14j
value5 = "hello, world!"
print((type(value1),value2, type(value2), type(value3), type(value4),type(value5), value5))

# Parameter Passing
def Change1(B):
    B = 2
        
A = 1
Change1(A)
print(A)

# Parameter Passing 2
def Change2(B):
    B.append(2)

A = [1]
Change2(A)
print(A)