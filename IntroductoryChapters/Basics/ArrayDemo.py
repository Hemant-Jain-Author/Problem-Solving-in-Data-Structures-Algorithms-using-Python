#!/usr/bin/env python
class ArrayDemo(object):
    def __init__(self):
        self.numbers = [0] * 100

    def addValue(self, index, data):
        self.numbers[index] = data

    def getValue(self, index):
        return self.numbers[index]



d = ArrayDemo()
d.addValue(0, 1)
d.addValue(1, 2)
print((d.getValue(0)))
print((d.getValue(1)))

