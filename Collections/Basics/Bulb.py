class Bulb(object):
    def __init__(self):         # Constructor
        self.isOn = False       # Instance Variable
    
    def turnOn(self):           # Instance Method
        self.isOn = True
    
    def turnOff(self):          # Instance Method
        self.isOn = False
    
    def isOnFun(self):          # Instance Method
        return self.isOn


b = Bulb()
print(("bulb is on return : " , b.isOnFun()))
b.turnOn()
print(("bulb is on return : " , b.isOnFun()))

c = Bulb()
print(("bulb c is on return : " , c.isOnFun()))

