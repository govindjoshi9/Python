from abc import ABCMeta, abstractmethod

class Shape(metaclass=ABCMeta):
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle:
    type = "Rectangle"
    side = 4
    def __init__(self):
        self.leanth = 6
        self.breath = 7

    def printarea(self):
        return self.leanth * self.breath

rect1 = Rectangle()
print(rect1.printarea())


