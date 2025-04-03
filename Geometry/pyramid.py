class Pyramid():
    def __init__(self, name, width, length, height):
        self.__name = name
        self.__width = width
        self.__length = length
        self.__height = height
        self.__area = (length * width) + ((width * height) * 0.5) + ((length * height) * 0.5)

    def def_name(self):
        return self.__name
    
    def print_area(self)
        return f"{self.__area}"

    def print_volume():
        return f"{self.__volume}"