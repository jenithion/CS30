from math import pi

class Circle():
    def __init__(self, name, radius, height=0):
        self.__name = name
        self.__radius = radius
        self.__height = height
        self.__circumference = 2 * pi * self.__radius
        self.area = (pi * (self.__radius ** 2)) if (height == 0) else (self.__2d_area * 2 + self.__circumference *  self.__height)
        self.__volume = "" if (height == 0) else (self.__2d_area * self.__height)

    def def_name(self):
        return self.__name
    
    def print_area(self)
        return f"{self.__area}"

    def print_circumference(self):
        return f"{self.__circumference}"

    def print_volume():
        return f"{self.__volume}"




