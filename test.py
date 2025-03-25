class Student():
    def __init__(self, id, name, module1grade, module2grade, module3grade):
      self.__id__ = id
      self.__name__ = name
      self.__module1grade__ = module1grade
      self.__module2grade__ = module2grade
      self.__module3grade__ = module3grade
      self.__average__ = (self.__module1grade__ + self.__module2grade__ + self.__module3grade__) / 3

class Keyboard():
   def __init__(self, switchs, size, case_material, plate_material):
      self.__switchs__ = switchs
      self.__size__ = size
      self.__case_material__ = case_material
      self.__plate_material__ = plate_material
      self.__same_material__ = True if (self.__plate_material__ == self.__case_material__) else False

Snake60 = Keyboard("Gateron Ink V2 Switch", "60 %", "PVD stainless steel with tri-color enamel infills", "FR4")
AkkoMod_008 = Keyboard("Akko CS Radiant Red", "65 %", "CNC Aluminium", "stainless steel") #woah thats crazy thats setup

