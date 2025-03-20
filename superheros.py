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

class partTwo:
    def find_hero(index, hero_list, price_list):
        """
        Given a list of heros their price and their location in the list, the fuction will return a string containing their info, if the index is -1, meaning the hero isn't found,
        the function will return a string stating that a hero of their chosing hasn't been found
    
        Args:
            (int)index: the index of where the hero is in the list
            (string list)hero_list: an array of heros
            (float list)price_list: an array for the price of hero's matching up with the index of the hero chosen
        
        Examples:
        
        """
        NOT_FOUND = -1
    
        match index:
            case NOT_FOUND:
                print("Im sorry we do not have anyone with that powerlevel availible")
            case _:
                print(f"You have chosen to hire hero {hero_list[index]}. The total cost per hour is ${price_list[index]}.")
           
    def part_two():
        """
        Prints out the welcome message for the main loop of part 2
        
        Example:
            Welcome to SuperHeros for Hire
            We have many superheros availible. Our levels range from 1 to 9.99. What powerlevel do you require
        """
        while True:
            print("Welcome to SuperHeros for Hire")
            print("We have many superheros availible. Our levels range from 1 to 9.99. What powerlevel do you require")
            target_pow = input()
            hero_index = binary_search(pow, target_pow)
            find_hero()

def part_three():
    return True
 
def main():
    """
    Runs a loop that asks the user for what powerlevel they require, printing out a superhero that matches their needs
    after superhero is found the user is prompted for their hours needed and multiplys it with the price of the superhero
    
    Examples:
        
    """

        
        
    
    
if __name__ == "__main__":
    main()