def increment1(var):
    var += 1

def main1():
    var = 1
    print(("Value before increment :" , var))
    increment1(var)
    print(("Value after increment :" , var))
    
class MyInt(object):
    def __init__(self):
        self.value = 1

def increment2(value):
    value.value += 1   
    
def main2():
    var = MyInt()
    print(("Value before increment :" , var.value))
    increment2(var)
    print(("Value after increment :" , var.value))  
        
main1()
main2()