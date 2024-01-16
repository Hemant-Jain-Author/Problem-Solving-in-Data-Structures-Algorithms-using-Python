class Bulb(object):

    # Class Variables 
    TotalBulbCount = 0
    
    # Constructor
    def __init__(self):
        Bulb.TotalBulbCount += 1
        self.isOn = False  # Instance Variable

    # Class Method
    @classmethod
    def getBulbCount(cls):
        return Bulb.TotalBulbCount

    # Instance Method
    def turnOn(self):
        self.isOn = True

    # Instance Method
    def turnOff(self):
        self.isOn = False

    # Instance Method
    def isOnFun(self):
        return self.isOn


b = Bulb()
print(("bulb is on return : " , b.isOnFun()))
b.turnOn()
print(("bulb is on return : " , b.isOnFun()))
print((Bulb.getBulbCount()))
