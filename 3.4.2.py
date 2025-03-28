class Student():
    def __init__(self, id, name, module1grade, module2grade, module3grade):
        self.__id = id
        self.__name = name
        self.__module1grade = module1grade
        self.__module2grade = module2grade
        self.__module3grade = module3grade
        self.__average = (self.__module1grade + self.__module2grade + self.__module3grade) / 3

    def __repr__():
        line1 = f"Student ID: {self.__id}\n"
        line2 = f"Name: {self.__name}\n"
        line3 = f"Module 1 Grade: {self.__module1grade}\n" 
        line4 = f"Module 2 Grade: {self.__module2grade}\n" 
        line5 = f"Module 3 Grade: {self.__module3grade}\n" 
        line6 = f"Student Course Average: {self.__average}"
        return "".join(line1, line2, line3, line4, line5, line6)

class Keyboard():
    def __init__(self, switchs, size, case_material, plate_material):
        self.__switchs = switchs
        self.__size = size
        self.__case_material = case_material
        self.__plate_material = plate_material
        self.__same_material = True if (self.__plate_material == self.__case_material) else False
    
    def __repr__(self):
        line1 = f"This keyboard has {self.__switchs}'s with a {self.__plate_material} plate, and {self.__case_material} case material made in a {self.__size} layout.\n"
        line2 = f"The plate and case matireal are the same" if (self.__same_material == True) else f"The plate and case matireal are different"
        return "".join([line1, line2]) 

Snake60 = Keyboard("Gateron Ink Black V2", "60 %", "PVD stainless steel with tri-color enamel infills", "FR4")
AkkoMod_008 = Keyboard("Akko CS Radiant Red", "65 %", "CNC Aluminium", "Stainless Steel") #woah thats crazy thats my keyboard 
EXT_65 = Keyboard("Jade Ruby HE", "65 % + left Numpad", "CNC Aluminium", "FR4")
