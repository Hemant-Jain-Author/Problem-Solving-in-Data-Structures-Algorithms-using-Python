
hs =  set() #  Create a set.

#  Add elements to the set.
hs.add("Banana")
hs.add("Apple")
hs.add("Mango")

print(hs)
print("Apple present : ", "Apple" in hs)
print("Grapes present : ", "Grapes" in hs)

hs.remove("Apple")
print("Apple present : ", "Apple" in hs)
print(hs)


"""
{'Apple', 'Banana', 'Mango'}
Apple present : True
Grapes present : False
Apple present : False
{'Banana', 'Mango'}
"""