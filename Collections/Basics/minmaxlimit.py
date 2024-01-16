import sys

maxInt = sys.maxsize
minInt = -sys.maxsize

longstart = maxInt + 1
floatvalue = 0.1
str = "hello, world!"

print(("type of maxint" , type(maxInt) , "value : " , maxInt))
print(("type of minInt" , type(minInt) , "value : " , minInt))
print(("type of longstart" , type(longstart) , "value : " , longstart))
print(("type of floatvalue" , type(floatvalue) , "value : " , floatvalue)) 
print(("type of str" , type(str) , "value : " , str))             


"""
('type of maxint', <class 'int'>, 'value : ', 9223372036854775807)
('type of minInt', <class 'int'>, 'value : ', -9223372036854775808)
('type of longstart', <class 'int'>, 'value : ', 9223372036854775808)
('type of floatvalue', <class 'float'>, 'value : ', 0.1)
('type of str', <class 'str'>, 'value : ', 'hello, world!')
"""


