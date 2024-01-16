from abc import ABCMeta
from abc import abstractmethod

class BulbInterface(object, metaclass=ABCMeta):
    @abstractmethod
    def turnOn(self):
        pass
    
    @abstractmethod
    def turnOff(self):
        pass

    @abstractmethod
    def isOnFun(self):
        pass

# implements BulbInterface
class Bulb(BulbInterface):
    class BulbSize:
        SMALL = 'SMALL'
        MEDIUM = 'MEDIUM'
        LARGE = 'LARGE'

    # Class Variables 
    TotalBulbCount = 0

    # Constructor
    def __init__(self):
        Bulb.TotalBulbCount += 1
        self.isOn = False  # Instance Variables
        self.size = Bulb.BulbSize.MEDIUM

    # Class Method
    @classmethod
    def getBulbCount(cls):
        return cls.TotalBulbCount

    # Instance Method
    def turnOn(self):
        self.isOn = True

    # Instance Method
    def turnOff(self):
        self.isOn = False

    # Instance Method
    def isOnFun(self):
        return self.isOn

    def getBulbSize(self):
        return self.size

class AdvanceBulb(Bulb):
    # Constructor
    def __init__(self):
        self.intensity = 0 # Instance Variables 
        Bulb.__init__(self)
        
    # Instance Method
    def setIntersity(self, i):
        self.intensity = i
        
        # Instance Method
    def getIntersity(self, i):
        return self.intensity


b = Bulb()
print(("Bulb Size : " + b.getBulbSize()))
print(("bulb is on return : " , b.isOnFun()))
b.turnOn()
print(("bulb is on return : " , b.isOnFun()))

