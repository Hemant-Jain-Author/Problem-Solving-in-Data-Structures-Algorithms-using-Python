text = "Hello, World!"
PI = 3.141592653589793

def main1():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    totalsum = 0
    for n in numbers:
        totalsum += n
    print("Sum is :: " , totalsum)

def main2():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    totalsum = 0
    i = 0
    while i < len(numbers):
        totalsum += numbers[i]
        i += 1
    print("Sum is :: " , totalsum)

def main3():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    totalsum = 0
    i = 0
    while True:
        totalsum += numbers[i]
        i += 1
        if i >= len(numbers):
            break
    print("Sum is :: " , totalsum)


main1()
main2()
main3()

"""
Sum is ::  55
Sum is ::  55
Sum is ::  55
"""