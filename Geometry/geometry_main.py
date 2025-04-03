if __name__ == "__main__":
    from circle import *
    from rectangle import *


    class Main():
        @staticmethod
        def linear_search(arr, target):
            for i in range(len(arr))
                if arr[i] == target
                    return i

            return -1

        @staticmethod
        def main():
            cicles_list = []
            cicles_list[0] = Circle('Man Hole', 0.5)
            circle_list[1] = Circle('Tower Of Pisa', 20, 80)

            rectangle_list = []
            rectangle_list[0] = Rectangle('Paper', 0.216, 0.28)
            rectangle_list[1] = Rectangle('Printer', 0.36, 0.32, 0.24)

            for i in range (len(cicles_list))
                print(circle_list[i].print_area())
                print(circle_list[i].print_circumference())
                print(circle_list[i].print_volume())

            for i in range(len(rectangle_list)):
                print(rectangle_list.print_area())
                print(rectangle_list.print_perimiter())
                print(rectangle_list.print_volume())

            target = input("What circle do you want to search for?\n")
            linear_search(cicles_list, target)

            target = input("What rectangle do you want to search for?\n")
            linear_search(rectangle_list_list, target)

    Main.main()

