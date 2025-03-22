hero_list = ["Generic Superhero", "Kazuya Kinoshita", "Rentarou Aijou", "Peacemaker", "Omniman", "Chainsaw man", "Satoru Gojo", "Sung Jin Woo", "Shadow", "......."]
pow_list = [1, 1.1, 2.3, 4.8, 6.6, 8.1, 8.9, 9.4, 9.9, 9.99]
price_list = [20, 13, 24, 30, 32, 34, 60, 65, 100, 1000]

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
    print(pow_list)

def part_two():
    """
    Prints out the welcome message for the main loop of part 2
    
    Example:
        Welcome to SuperHeros for Hire
        We have many superheros availible. Our levels range from 1 to 9.99. What powerlevel do you require
    """
    class const():
        NOT_FOUND = -1
    print("Welcome to SuperHeros for Hire")
    print("We have many superheros availible. Our levels range from 1 to 9.99. What powerlevel do you require")
    print(f"Current Availible Power Levels {pow_list}")
    target_pow = float(input())
    hero_index = binary_search(pow, target_pow)

    match index:
        case const.NOT_FOUND:
            print("Im sorry we do not have anyone with that powerlevel availible")
        case _:
            print(f"You have chosen to hire hero {hero_list[hero_index]}. The total cost per hour is ${price_list[hero_index]}.")

def part_three():
    class const():
        NOT_FOUND = -1
    EMPLOYMENT_ENSURANCE = 1.2

    while True:
        print("Welcome to SuperHeros for Hire")
        print("We have many superheroes available.  Our levels range from 1 to 9.99.  What power level do you require?")
        print(f"Current Availible Power Levels {pow_list}")
        target_pow = floatint(input())
        hero_index = binary_search(pow_list, target_pow)

        match hero_index:
            case const.NOT_FOUND:
                print("Im sorry we do not have anyone with that powerlevel availible")
            case _:
                print(f"You have chosen to hire hero {hero_list[hero_index]}. The total cost per hour is ${price_list[hero_index]}.")
                break

    while True:
        print("For how many hours do you need our superhero services?")
        hours = floatint(input())
        if hours < 3:
            print("Heros can only work for a minimum of 3 Hours please try again")
        else:
            total_price = hours * price_list[hero_index] * EMPLOYMENT_ENSURANCE
            print(f"Your total price including taxes and employment ensurance is ${total_price}")

def part_four():
    """
    An employee may work a maximum of 12 hours a day
    An employee is entitled to one 30-minute paid or unpaid break after the first 5 hours of work for shifts that are between 5 and 10 hours long.
    For shifts 10 hours or longer, an employee is entitled to two 30-minute breaks.
    An employee is not entitled to any breaks if their shift is 5 hours or less.
    Add a loop that will exit if the user enters 0 for number of hours. (Make it say something snarky.)
    """
    #i need this for switch cases because variables dont work but properties do
    class const():
        ZERO_BREAKS = 0
        ONE_BREAK = 1
        TWO_BREAKS = 2
        NOT_FOUND = -1
    EMPLOYMENT_ENSURANCE = 1.2
    EXIT = 0
    RUN = 1
    DAY_MAX = 12
    DAY_MIN = 3
    HALF_HOUR_BREAK = 0.5
    HOUR_BREAK = 1
    HOURS_PER_BREAK = 5

    while True:
        print("Welcome to SuperHeros for Hire")
        print("We have many superheroes available.  Our levels range from 1 to 9.99.  What power level do you require?")
        print(f"Current Availible Power Levels {pow_list}")
        target_pow = float(input())
        hero_index = binary_search(pow_list, target_pow)

        match hero_index:
            case const.NOT_FOUND:
                print("Im sorry we do not have anyone with that powerlevel availible, please try again")
            case _:
                print(f"You have chosen to hire hero {hero_list[hero_index]}. The total cost per hour is ${price_list[hero_index]}.")
                break

    while True:
        print("For how many hours do you need our superhero services?")
        hours = float(input())
        if hours == EXIT:
            return EXIT 
        elif hours < DAY_MIN:
            print("Heros can only work for a minimum of 3 Hours per day please try again")
        elif hours > DAY_MAX:
            print("Heros can only work for a maximum of 12 Hours per day please try again")
        else:
            break_amt = hours // HOURS_PER_BREAK 
            match break_amt:
                case const.ZERO_BREAKS:
                    total_price = hours * price_list[hero_index] * EMPLOYMENT_ENSURANCE
                    print(f"Your total price including taxes and employment ensurance is ${total_price}")
                    break
                case const.ONE_BREAK:
                    total_price = (hours - HALF_HOUR_BREAK) * price_list[hero_index] * EMPLOYMENT_ENSURANCE
                    print(f"Your total price including taxes and employment ensurance is ${total_price}")
                    break
                case const.TWO_BREAKS:
                    total_price = (hours - HOUR_BREAK) * price_list[hero_index] * EMPLOYMENT_ENSURANCE
                    print(f"Your total price including taxes and employment ensurance is ${total_price}")
                    break

    return 1

def main():
    """
    Runs a loop that asks the user for what powerlevel they require, printing out a superhero that matches their needs
    after superhero is found the user is prompted for their hours needed and multiplys it with the price of the superhero
    
    Examples:
        
    """
    TRUE = 1

    running = TRUE
    while running == TRUE:
        print("\n")
        running = part_four() 

    print("Huh, you dont need anyone anymore, well go on your merry way :)")

if __name__ == "__main__":
    main()