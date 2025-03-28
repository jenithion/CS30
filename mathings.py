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

class main():
    @staticmethod
    def main():
        while True:
            try:
                num1 = float(input("What is the first number you would like to use"))
                num2 = float(input("What is the second number you would like to use"))

                while True:
                    try:
                        print("What operation would you like to do on the numbers")
                        print("1. Multiply")
                        print("2. Add")
                        print("3. Divide")
                        print("4. Subtract")
                        choice = int(input())

                    match choice:
                        case 1:
                            print(Mathy.multiply(num1, num2))
                            break
                        case 2:
                            print(Mathy.add(num1, num2))
                            break
                        case 3:
                            print(Mathy.divide(num1, num2))
                            break
                        case 4: 
                            print(Mathy.subtract(num1, num2))
                            break
                        case _:
                            print("The value youve inputed is not one of the options please try again")

            except ValueError:
                print("The value you've inputed is not a number please try again")

    