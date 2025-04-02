class Rectangle():
    def __init__(self, name, width, length, height=0):
        self.__name = name
        self.__width = width
        self.__length = length
        self.__height = height
        self.__2d_area = self.__length * self.__width
        self.__3d_area = (self.__2d_area * 2) + (self.__width * self.__height * 2) + (self.__length * self.__height * 2)
        self.__perimiter = (2 * width) + (2 * length)
        self.__area = self.__2d_area if (self.__height == 0) else self.__3d_area
        self.__volume = "" if (self.__height == 0) else (self.__2d_area * height)

    def get_name(self):
        return self.__name

    def print_area(self):
        return self.__area

    def print_perimiter(self):
        return self.__perimiter

    def print_volume(self):
        return self.__volume