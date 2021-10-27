def main1():
    numbers = [0] * 100
    numbers[1] = 2
    print(numbers[1])


def main2() :
    al =  []
    al.append(1) #  add 1 to the end of the list 
    al.append(2) #  add 2 to the end of the list
    print("Contents of Array : " + str(al))
    print("Array Size : " + str(len(al)))
    print("Array IsEmpty : " + str((len(al) == 0)))
    del al[- 1] #  last element of list is removed.
    al = []   #  all the elements of list are removed.
    print("Array IsEmpty : " + str((len(al) == 0)))


def main3():
    lst = [1, 2, 3, 4]
    print(lst)
    lst.append(5)
    lst.append(4)
    lst.append(2)
    lst.append(6)
    print(lst)
    print(len(lst))

    lst.remove(4)
    print(lst)

    print(lst.pop())
    print(lst.pop())
    print(lst)

    lst.sort()
    print(lst)
    lst.reverse()
    print(lst)

main1()
main2()
main3()

"""
Contents of Array : [1, 2]
Array Size : 2
Array IsEmpty : False
Array IsEmpty : True
"""
"""
[1, 2, 3, 4]
[1, 2, 3, 4, 5, 4, 2, 6]
8
[1, 2, 3, 5, 4, 2, 6]
6
2
[1, 2, 3, 5, 4]
[1, 2, 3, 4, 5]
[5, 4, 3, 2, 1]
"""