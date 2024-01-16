class Calculator(object):
    def __init__(self, value=0):
        self.value = value

    def reset(self):
        self.value = 0

    def getValue(self):
        return self.value

    def add(self, data):
        self.value = self.value + data

    def increment(self):
        self.value += 1

    def subtract(self, data):
        self.value = self.value - data

    def decrement(self):
        self.value -= 1
