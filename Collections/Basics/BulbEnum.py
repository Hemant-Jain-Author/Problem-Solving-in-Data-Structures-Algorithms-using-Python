class Bulb(object):
    class BulbSize:
        SMALL = 'SMALL'
        MEDIUM = 'MEDIUM'
        LARGE = 'LARGE'

    # Constructor
    def __init__(self):
        self.isOn = False  # Instance Variables
        self.size = Bulb.BulbSize.MEDIUM

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
    
    def setBulbSize(self, value):
        self.size = value


b = Bulb()
print(("Bulb Size : " + b.getBulbSize()))
