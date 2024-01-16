def main1():
    numbers = [0] * 100
    numbers[1] = 2
    print(numbers[1])


def main2() :
    al =  []
    al.append(1) #  add 1 to the end of the list 
    al.append(2) #  add 2 to the end of the list
    print("Contents of List :", al)
    print("List Size :", len(al))
    print("List IsEmpty :", (len(al) == 0))
    del al[- 1] #  last element of list is removed.
    al = []   #  all the elements of list are removed.
    print("List IsEmpty :", (len(al) == 0))


lst = [1, 2, 3]
print(lst)

lst.append(4)
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

"""
[1, 2, 3]
[1, 2, 3, 4]
4

[1, 2, 3]
3
2
[1]
[1]
[1]
"""