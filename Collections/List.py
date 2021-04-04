lst = [1, 2, 3, 4]
print(lst)

lst.append(5)
lst.append(4)
lst.append(2)
lst.append(6)
print(lst)
print(len(lst))
print(lst + lst)

lst.remove(4)
print(lst)

print(lst.pop())
print(lst)

lst.sort()
print(lst)

lst.reverse()
print(lst)

"""
[5, 4, 2, 6]
4
[5, 4, 2, 6, 5, 4, 2, 6]
[5, 2, 6]
6
[5, 2]
[2, 5]
[5, 2]
"""

