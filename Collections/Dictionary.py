a = {}
a["mango"] = 20
a["apple"] = 40
a["banana"] = 10

print(a)
print(a["mango"])
print(a.get("mango"))
print("apple" in a)

"""
{'mango': 20, 'apple': 40, 'banana': 10}
20
20
True
"""

a =  dict()
a["mango"] = 20
a["apple"] = 40
a["banana"] = 10

print(a)
print(a["mango"])
print(a.get("mango"))
print("apple" in a)

"""
{'mango': 20, 'apple': 40, 'banana': 10}
20
20
True
"""

# from 3.7 dict will also keep the elements in order.
# effectively dict and ordereddict are same. 
from collections import OrderedDict

b = OrderedDict()
b["apple"] = 40
b["mango"] = 20
b["banana"] = 10

print(b)
print(b["mango"])
print(b.get("mango"))
print("banana" in b)
