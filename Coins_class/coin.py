if __name__ == "__main__":
    from math import pi

    class Coin():
        def __init__(self, coin_name, radius, matirial, value):
            self.__coin_name__ = coin_name
            self.__radius__ = radius
            self.__matirial__ = matirial
            self.__value__ = value

        def get_circumfrance(self):
            return pi * self.__radius__ * 2

        def get_area(self):
            return pi * (self.__radius__ ** 2)

        def __repr__():
            line_one = f"The surface area of one side of a {self.__coin_name__} is {get_area()}mm²"
            line_two = f"\nA {self.__coin_name__}’s circumference is {get_circumfrance()}mm"  
            line_three = f"\nA {self.__coin_name__} is made of {self.__matirial__} and has a value of {self.__value__} cents"
            string = "".join([line_one, line_two, line_three])
            return string


