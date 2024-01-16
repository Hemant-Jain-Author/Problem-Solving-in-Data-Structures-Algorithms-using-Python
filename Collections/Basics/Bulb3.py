class Bulb(object):
    TotalBulbCount = 0          # Class Variables
   
    def __init__(self):         # Constructor
        Bulb.TotalBulbCount += 1
        self.isOn = False       # Instance Variables 

    @classmethod
    def getBulbCount(cls):
        return cls.TotalBulbCount
    
    def turnOn(self):           # Instance Method
        self.isOn = True
    
    def turnOff(self):          # Instance Method
        self.isOn = False
    
    def isOnFun(self):          # Instance Method
        return self.isOn


class AdvanceBulb(Bulb):
    def __init__(self):                 # Constructor
        self.intensity = 0 # Instance Variables 
        Bulb.__init__(self)
   
    def setIntersity(self, i):          # Instance Method
        self.intensity = i
              
    def getIntersity(self, i):          # Instance Method
        return self.intensity



# b = Bulb()
c = AdvanceBulb()
print((Bulb.getBulbCount()))
print((c.isOnFun()))
