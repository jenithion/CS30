from math import pi

class Coin():
    def __init__(self, coin_name, radius, matirial, value):
        self.coin_name = coin_name
        self.radius = radius
        self.matirial = matirial
        self.value = value

    def get_circumfrance(self):
        return pi * self.radius * 2

    def get_area(self):
        return pi * (self.radius ** 2)

    def __repr__(self):
        line_one = f"The surface area of one side of a {self.coin_name} is {self.get_area():.2f}mm²"
        line_two = f"\nA {self.coin_name}’s circumference is {self.get_circumfrance():.2f}mm"  
        line_three = f"\nA {self.coin_name} is made of {self.matirial} and has a value of {self.value:.0f} cents"
        string = "".join([line_one, line_two, line_three])
        return string


