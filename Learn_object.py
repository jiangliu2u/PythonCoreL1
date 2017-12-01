import math

class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    #Getter functipn
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    @first_name.deleter
    def first_name(self):
        raise AttributeError("'Can't delete attribute'")

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi*self.radius*self.radius

    @property
    def diameter(self):
        return self.radius**2
    @property
    def perimeter(self):
        return 2*math.pi*self.radius
