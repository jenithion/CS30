import random, copy

def make_hand(cards, hand_size):
    hand = []
    new_deck = copy.copy(cards)
    for i in range(hand_size):
        rand_card_num = random.randint(0, len(new_deck) - 1)
        hand.append(new_deck[rand_card_num])
        new_deck.pop(rand_card_num)
    
    return hand

def binary_search(arr, target):
    """
    Preforms Binary search on a sorted list
    
    Args:
        arr(list): a sorted list of nums
        target(int or float): the value to search for

    Example:
        binary_search([range(1, 10)], 6)
        >>> 5
        
        binary_search([range(1, 10, 2)], 4)
        >>> -1
    """
    
    low = 0
    high = len(arr) - 1
    mid = 0
    
    i = 0
    while low <= high:
        mid = (high + low) // 2 #find mid point through average
        
        #if target is equal to the middle elemtnt
        if arr[mid] == target:
            return mid
        #if target is greater, ignore left half
        elif arr[mid] < target:
            low = mid + 1
        #if target is smaller, ignore right side
        else:
            high = mid - 1
            
    #target not found
    return -1

def mut_insertion_sort(arr):
    """
    Prefoms selection sort on a array and returns a sorted array, it is also mutable so it changes the original argument
    
    Args:
        (list) arr: a list
    
    Example:
        mut_selection_sort([5, 3, 8, 4, 2])
        >>> [2, 3, 4, 5, 8]
    """
    
    n = len(arr)
    
    #list empty edge case
    if n <= 1:
        return arr
        
    for i in range(1, n):
        #key is the current selected element that needs to be sorted
        key = arr[i]
        #j is the start of the sorted part of the array
        j = i - 1
        
        #shift all items in the sorted part of the array to the right(arr[current_idx++]) until the key is in the correct place
        #we use j >= 0 to ensure that the key doesnt go past the start of the array due to python's negitive elements
        while (j >= 0) and (key < arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j+1] = key
        
    return arr

def all_equal(arr):
    """
    Checks an array of cards to check if all ranks are equal

    Args:
        (list)arr: an array of cards (suit, rank)

    Return:
        True: if all cards are equal
        False: if cards arent all equal

    Example:
        card_list = [('Hearts', '4'), ('Spades', '6'), ('Spades', '3'), ('Clubs', '6'), ('Spades', '6'), ('Diamonds', '10'), ('Clubs', '10'), ('Hearts', '5')]
        print(all_equal(card_list))
        >>> False

        card_list = [('Hearts', '3') , ('Clubs', '3'), ('Diamonds', '5')]
        print(all_equal(card_list))
        >>> True
    """
    #create the list of just the ranks
    list = [x[0] for x in arr]
    print(list)

    #get its length due to it being reused 
    LIST_LEN = len(list)

    #if the list is greater than 4 there is no way for it to be all equal due to there being only one card per suit
    if LIST_LEN > 4:
        return False

    #check if one of the cards are not equal and go through the whole list
    #we can return false right away due to the fact that if one is not equal the whole list cannot be equal
    for i in range(1, LIST_LEN):
        if list[i - 1] != list[i]:
            return False

    #if it has no return yet we can just return true because the check hasnt returned false
    return True

def shuffle(arr):
    arr = set(arr)
    arr = list(arr)
    return arr
    
def three_of_a_kind(arr):
    list = [x[0] for x in arr]
    print(list)
    mut_insertion_sort(list)

    #we iterate through all the numbers in the list
    for i in range(len(list) - 1, 0):
        #if the function hasnt returned true and the amt of items in the list is less than 3 it cant be true
        if i < 2:
            return False

        #we put one as the current amount at the start of every loop to keep track of the current card
        current_amt = 1

        #get the number to check
        target = list[i]

        #to make sure that the card we selected isnt checked again we remove it from the list
        list.pop()

        #get the amount of the rank were cheching and remove the item when checed
        while binary_search(list, target) != -1:
            current_amt += 1
            to_pop = binary_search(list)
            list.pop(to_pop)
        
        #check if we have three or more of a kind
        if current_amt >= 3:
            return True
        
        i -= 1
        
    return False 
    
def pairs_amt(arr):
    list = [x[1] for x in arr]

    #we iterate through all the numbers in the list
    for i in range(len(list) - 1, 0):
        #if the function hasnt returned true and the amt of items in the list is less than 3 it cant be true
        if i < 2:
            return False

        #we put one as the current amount at the start of every loop to keep track of the current card
        current_amt = 1

        #get the number to check
        target = list[i]

        #to make sure that the card we selected isnt checked again we remove it from the list
        list.pop()

        #get the amount of the rank were cheching and remove the item when checed
        while binary_search(list, target) != -1:
            current_amt += 1
            to_pop = binary_search(list)
            list.pop(to_pop)
        
        #check if we have three or more of a kind
        if current_amt >= 3:
            return True
        
        i -= 1
        
    return True

def highest_pair(arr):
    list = [x[1] for x in arr]

    #we iterate through all the numbers in the list
    for i in range(len(list) - 1, 0):
        #if the function hasnt returned true and the amt of items in the list is less than 3 it cant be true
        if i < 2:
            return False

        #we put one as the current amount at the start of every loop to keep track of the current card
        current_amt = 1

        #get the number to check
        target = list[i]

        #to make sure that the card we selected isnt checked again we remove it from the list
        list.pop()

        #get the amount of the rank were cheching and remove the item when checed
        while binary_search(list, target) != -1:
            current_amt += 1
            to_pop = binary_search(list)
            list.pop(to_pop)
        
        #check if we have three or more of a kind
        if current_amt >= 3:
            return True
        
        i -= 1
        
    return True

def main():
    #create a list of all the card to choose from
    suits = ['♥', '♠', '♦', '♣']
    ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    cards = [[rank, suit] for rank in ranks for suit in suits]

    #create the hands
    MAX_HAND_SIZE = 13
    MIN_HAND_SIZE = 1
    hand_size = lambda a: a + random.randint(MIN_HAND_SIZE, MAX_HAND_SIZE)

    HANDS_AMT = 4
    hands = [make_hand(cards, hand_size(0)) for j in range(HANDS_AMT)]

    while True:
        for i in range(HANDS_AMT):
            print(f"Hand #{i + 1}:\n{hands[i]} \n")

        hand_num = 0
        while hand_num == 0: 
            print("which hand do you want to check")
            hand_num = int(input())

            if (hand_num > 4) or (hand_num < 1):
                hand_num = 0
                print("The value you've inputed is not one of the hands")
            else:
                hand_num -= 1
                break
                
        while True:
            print("What operation do you want to do on the hand:")
            print("   1. Check if all cards are equal")
            print("   2. Shuffle the hand")
            print("   3. Check for three of a kind")
            print("   4. Count for pairs")
            print("   5. Find the highest Pair")
            operation = input()
            match operation:
                case "1":
                    print(all_equal(hands[hand_num]))
                    break
                case "2":
                    print(shuffle(hands[hand_num]))
                    break
                case "3":
                    print(three_of_a_kind(hands[hand_num]))
                    break
                case "4":
                    print(pairs_amt(hands[hand_num]))
                    break
                case "5":
                    print(highest_pair(hands[hand_num]))
                    break
                case _:
                    print("The character you've enterenterd is not one of the options") 

if __name__ == "__main__":
    main()
