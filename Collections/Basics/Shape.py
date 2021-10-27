from abc import ABCMeta
from abc import abstractmethod

# Abstract Class
class Shape(object, metaclass=ABCMeta):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
