#!/usr/bin/env python
from abc import ABCMeta
from abc import abstractmethod

# Abstract Class
class Shape(object):
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
