class Mathy():
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        return x / y

    @staticmethod
    def subtract(x, y):
        return x - y
    
    @staticmethod
    def hypotnuse(x, y):
        return 0.5 * ((x ** 2) + (y ** 2))

    @staticmethod
    def pow(x, y):
        return x ** y

    @staticmethod
    def getKthDigit(x, y):
        return abs(n) // (10 ** k) % 10

    @staticmethod
    def short1():
        line1 = "A static meathod is a function that belongs to the class as a whole, with it having no knowledge of its"
        line2 = "\nbase class the static meathod is technechly not even considered a meathod anymore rather just a function"
        line3 = "\ninfo from https://stackoverflow.com/questions/37659660/static-methods-and-designing-for-inheritance"
        return "".join([line1, line2, line3])

    @staticmethod
    def short2():
        line1 = "They are useful when a function logically belongs to a class but does not need to interact with"
        line2 = "\ninstance or class variables. More spesifcly the @staticmeathod decorator is kindof like def or class"
        line3 = "\nit is a keyword that defines spesifcly the function ahead of it as a static function. the @ before the words"
        line3 = "\nstatic function probaly define a keyword that is classes spesifc"
        return "".join([line1, line2, line3, line4])

    @staticmethod
    def short3():
        line1 = "a static meathod is connected to the class itself, it does not need an object/instcae to be called,"
        line2 = "meanwhile a instance meathod is a meathod for this instance/object, these meathods work on the variables"
        line3 = "inside of the class and ise its defined atributes"
        return "".join([line1, line2, line3])

    @staticmethod
    def name

class main():
    @staticmethod
    def main():
        try:
            while True:
                print("1. Name")
                print("2. Addition")
                print("3. Subtraction")
                print("4. Multiplication")
                print("5. Division")
                print("6. Hypotnuse")
                print("7. Power")
                print("8. Get Nth Digit")
                print("9. Short Awnser 1")
                print("10. Short Awnser 2")
                print("11. Short Awnser 3")
                print("12. Exit")
                operation = int(input())

                if operation < 1 and (operation > 12):
                    print("Please input a valid number.")

                else: 
                    break
                
            while True:
                if operation >= 2 and operation <= 8:
                    num1 = float(input())
                    num2 = float(input())
                    match operation:
                        case 2:
                            Mathy.add(num1, num2)
                        case 3:
                            Mathy.subtract(num1, num2)
                        case 4:
                            Mathy.multiply(num1, num2)
                        case 5:
                            Mathy.divide(num1, num2)
                        case 6:
                            Mathy.hypotnuse(num1, num2)
                        case 7:
                            Mathy.pow(num1, num2)
                        case 8:
                            Mathy.getKthDigit(num1, num2)

                else:
                    match operation:
                        case 1:
                            Mathy.name()
                        case 10:
                            Mathy.short1()
                        case 11:
                            Mathy.short2()
                        case 12:
                            Mathy.short3()
                        case 13:
                            break
            break
                

        except ValueError:
            print("The value you've inputed is not a number please try again")

if __name__ = "__main__":
    main()