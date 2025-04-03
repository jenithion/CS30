from math import pi

class Pyramid():
    def __init__(self, name, radius, height=0):
        self.__name = name
        self.__radius = radius
        self.__height = height
        self.__area = 4 * pi * (self.__radius ** 2)

    def def_name(self):
        return self.__name
    
    def print_area(self)
        return f"{self.__area}"

    def print_volume():
        return f"{self.__volume}"