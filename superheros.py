name = []
pow = []
price = []

def binary_search(arr, target):
    """
    Given a sorted array and target, binary_search(), returns the index of the target through the binary search algorhythm, if target isn't found it will return -1
    
    Args:
        (list)arr: a sorted list
        (void)target: the value being searched for
        
    Examples:
        binary_search(list(range(0,7)), 5)
        >>> 5
        
        binary_search()
        >>> -1
    
    """
    min = 0             #minimium index of the array
    max = len(arr) - 1  #max index of the array
    
    while min <= max:
        mid = (min + max) // 2 #middle point index of the array
        
        if arr[mid] == target:
            return mid
        elif arr[mid] <= target:
            min = mid + 1
        else:
            max = mid - 1
        
    return -1

def part_one():
    """
    Prints out the message for part one of the assignment
    
    Example:
        Welcome to SuperHeros for Hire
        Availible power Levels
        []
    """
    print("Welcome to SuperHeros for Hire")
    print("Availible power Levels")
    print(pow)

def part_two():
    """
    Prints out the welcome message for the main loop of part 2
    
    Example:
        Welcome to SuperHeros for Hire
        We have many superheros availible. Our levels range from 1 to 9.99. What powerlevel do you require
    """
    NOT_FOUND = -1
    print("Welcome to SuperHeros for Hire")
    print("We have many superheros availible. Our levels range from 1 to 9.99. What powerlevel do you require")
    target_pow = input()
    hero_index = binary_search(pow, target_pow)

    match index:
        case NOT_FOUND:
            print("Im sorry we do not have anyone with that powerlevel availible")
        case _:
            print(f"You have chosen to hire hero {hero_list[index]}. The total cost per hour is ${price_list[index]}.")

def part_three():
    NOT_FOUND = -1
    EMPLOYMENT_ENSURANCE = 1.2

    print("Welcome to SuperHeros for Hire")
    print("We have many superheroes available.  Our levels range from 1 to 9.99.  What power level do you require?")
    target_pow = int(input())
    hero_index = binary_search(pow, target_pow)
    
    match hero_index:
        case NOT_FOUND:
            print("Im sorry we do not have anyone with that powerlevel availible")
        case _:
            print(f"You have chosen to hire hero {hero_list[index]}. The total cost per hour is ${price_list[index]}.")

    while True:
        print("For how many hours do you need our superhero services?")
        hours = int(input())
        if hours < 3:
            print("Heros can only work for a minimum of 3 Hours please try again")
        else:
            total_price = hours * price[hero_index] * EMPLOYMENT_ENSURANCE
            print(f"Your total price including taxes and employment ensurance is ${total_price}")

def part_four():
    """
    An employee may work a maximum of 12 hours a day
    An employee is entitled to one 30-minute paid or unpaid break after the first 5 hours of work for shifts that are between 5 and 10 hours long.
    For shifts 10 hours or longer, an employee is entitled to two 30-minute breaks.
    An employee is not entitled to any breaks if their shift is 5 hours or less.
    Add a loop that will exit if the user enters 0 for number of hours. (Make it say something snarky.)
    """
    NOT_FOUND = -1
    EMPLOYMENT_ENSURANCE = 1.2

    print("Welcome to SuperHeros for Hire")
    print("We have many superheroes available.  Our levels range from 1 to 9.99.  What power level do you require?")
    target_pow = int(input())
    hero_index = binary_search(pow, target_pow)
    
    match hero_index:
        case NOT_FOUND:
            print("Im sorry we do not have anyone with that powerlevel availible")
        case _:
            print(f"You have chosen to hire hero {hero_list[index]}. The total cost per hour is ${price_list[index]}.")

    while True:
        print("For how many hours do you need our superhero services?")
        hours = int(input())
        if hours == 0:
            break
        elif hours < 3:
            print("Heros can only work for a minimum of 3 Hours per day please try again")
        elif hours > 12:
            print("Heros can only work for a maximum of 12 Hours per day please try again")
        else:
            match (hours // 5):
                case 0:
                    total_price = hours * price[hero_index] * EMPLOYMENT_ENSURANCE
                    print(f"Your total price including taxes and employment ensurance is ${total_price}")
                case 1:
                    total_price = (hours - 0.5) * price[hero_index] * EMPLOYMENT_ENSURANCE
                    print(f"Your total price including taxes and employment ensurance is ${total_price}")
                case 2:
                    total_price = (hours - 1) * price[hero_index] * EMPLOYMENT_ENSURANCE
                    print(f"Your total price including taxes and employment ensurance is ${total_price}")

def main():
    """
    Runs a loop that asks the user for what powerlevel they require, printing out a superhero that matches their needs
    after superhero is found the user is prompted for their hours needed and multiplys it with the price of the superhero
    
    Examples:
        
    """

        
        
    
    
if __name__ == "__main__":
    main()