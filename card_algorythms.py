import random, copy
#you may notice alot of constants or all caps variables, that just equal to a constant and never change
#its just my style of code, i usualy dont use comments, sometimes i use docstrings, but i digress
#Since i dont use comments, i just use constants to makesure i can either 
#really quickly find something i need to change or understand why i put a variable there

def make_hand(cards, hand_size):
    """
    Makes a hand given the list of cards and the size to make it

    Args:
        (list)cards: a list of all the 52 cards
        (int)hand_size: the size to make the hand
    
    Returns: 
        (list): return a list of cards from a new "deck"

    Examples:

    """
    #create an empty array of what will be the hand
    hand = []
    #create a new "deck" of cards to tell which ones we've pulled
    new_deck = copy.copy(cards)

    #go for how much cards to make the hand
    for i in range(hand_size):
        START_OF_DECK = 0
        LAST_OF_DECK = len(new_deck) - 1

        #pick a random card, and remember its index
        rand_card_num = random.randint(START_OF_DECK, LAST_OF_DECK)
        #add the random card to our hand
        hand.append(new_deck[rand_card_num])
        #remove the random card from the deck to make sure we dont pull it twice
        new_deck.pop(rand_card_num)
    
    return hand

def rank_to_int(arr):
    """
    Changes the problem cases (Ace, Jack, Queen, King) to their interger varient for use in functions

    Args:
        (list)arr: a list of cards with string representations for (Ace, Jack, Queen, King)

    Examples:
        print(rank_to_int([[2, '♠'], [3, '♦'], [9, '♦'], ['King', '♠'], [9, '♣'], [5, '♠'], [10, '♥'], [6, '♥'], [9, '♥']]))
        >>> [[2, '♠'], [3, '♦'], [9, '♦'], [13, '♠'], [9, '♣'], [5, '♠'], [10, '♥'], [6, '♥'], [9, '♥']]
    """
    RANK_OF_CARD = 0

    ACE = 1
    JACK = 11
    QUEEN = 12
    KING = 13

    for x in arr:
        match x[RANK_OF_CARD]:
            case 'Ace':
                x[RANK_OF_CARD] = ACE 
            case 'Jack':
                x[RANK_OF_CARD] = JACK 
            case 'Queen':
                x[RANK_OF_CARD] = QUEEN 
            case 'King':
                x[RANK_OF_CARD] = KING 

def int_to_rank(arr):
    """
    Changes the problem cases (1, 11, 12, 13) to their string varient to change the look back for printing

    Args:
        (list)arr: a list of cards with interger representations for (Ace, Jack, Queen, King)

    Examples:
        print(int_to_rank([[2, '♠'], [3, '♦'], [9, '♦'], [13, '♠'], [9, '♣'], [5, '♠'], [10, '♥'], [6, '♥'], [9, '♥']]))
        >>> [[2, '♠'], [3, '♦'], [9, '♦'], ['King', '♠'], [9, '♣'], [5, '♠'], [10, '♥'], [6, '♥'], [9, '♥']]
    """
    RANK_OF_CARD = 0

    #switchcases are just wierd
    class constant():
        ACE = 1
        JACK = 11
        QUEEN = 12
        KING = 13

    for x in arr:
        match x[RANK_OF_CARD]:
            case constant.ACE:
                x[RANK_OF_CARD] = 'Ace'
            case constant.JACK:
                x[RANK_OF_CARD] = 'Jack' 
            case constant.QUEEN:
                x[RANK_OF_CARD] = 'Queen' 
            case constant.KING:
                x[RANK_OF_CARD] = 'King' 

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
        (list)arr: an array of cards (rank, suit)

    Return:
        True: if all cards are equal
        False: if cards arent all equal

    Example:
        card_list = [('Hearts', '4'), ('Spades', '6'), ('Spades', '3'), ('Clubs', '6'), ('Spades', '6'), ('Diamonds', '10'), ('Clubs', '10'), ('Hearts', '5')]
        print(all_equal(card_list))
        >>> False

        card_list = [('Hearts', '3') , ('Clubs', '3'), ('Diamonds', '3')]
        print(all_equal(card_list))
        >>> True
    """
    RANK_OF_CARD = 0
    #create the list of just the ranks
    list = [x[RANK_OF_CARD] for x in arr]

    #get its length due to it being reused 
    LIST_LEN = len(list)

    #if the list is greater than 4 there is no way for it to be all equal due to there being only one card per suit
    SUIT_AMT = 4
    if LIST_LEN > SUIT_AMT:
        return False

    #check if one of the cards are not equal and go through the whole list
    #we can return false right away due to the fact that if one is not equal the whole list cannot be equal
    for i in range(1, LIST_LEN):
        TARGET_NUMBER = i
        PREVIOUS_NUMBER = i - 1

        if list[PREVIOUS_NUMBER] != list[TARGET_NUMBER]:
            return False

    #if it has no return yet we can just return true because the check hasnt returned false
    return True

def shuffle(arr):
    """
    Shuffles the chosen hand (randomizes its current order)

    Args:
        (list)arr: an array of cards(rank, suit)

    Returns:
        (list): a "shuffled" array of the given cards
        
    Examples:
        print(shuffle([[5, '♦'], [4, '♣'], ['Queen', '♦'], ['Ace', '♥'], [9, '♠'], [8, '♠'], [6, '♦'], [4, '♥'], [2, '♦'], [5, '♠'], [4, '♠']]))
        >>> [[5, '♦'], [4, '♣'], ['Queen', '♦'], ['Ace', '♥'], [9, '♠'], [8, '♠'], [6, '♦'], [4, '♥'], [2, '♦'], [5, '♠'], [4, '♠']]

        print(shuffle([[8, '♥'], [9, '♠'], [10, '♠'], [4, '♥'], ['Queen', '♣'], [2, '♦'], [5, '♠'], [10, '♣']]))
        >>> [['Queen', '♣'], [2, '♦'], [4, '♥'], [10, '♠'], [5, '♠'], [10, '♣'], [9, '♠'], [8, '♥']]
    """
    RANK_OF_CARD = 0
    SUIT_OF_CARD = 1

    #change all the items in the array to immutible
    arr = [frozenset(x) for x in arr]
    #sets are unordered and therefore if arr is changed into a set it will "shuffle" it
    arr = set(arr) 

    #change back the items in the array to mutible elements in case used again in another function
    arr = [list(x) for x in arr]
    #changes the list back to a list to ensure that when given back to the main function the order will not change again
    arr = list(arr)

    #due to my need to change the set to immutible elemetns the order of cards(rank, suit) might be changed to cards(suit, rank)
    for x in arr:
        #due to the suit always being a string, and the rank of the card being changed to intergers before this function is called
        #we can find if the rank and suit has been swaped in the process of changeing the items inside the list to immutible
        if type(x[RANK_OF_CARD]) is str:
            x[RANK_OF_CARD], x[SUIT_OF_CARD] = x[SUIT_OF_CARD], x[RANK_OF_CARD]

    return arr
    
def three_of_a_kind(arr):
    """
    Check the array for three cards of the same kind

    Args:
        (list)arr: an array of cards(check the constant in the main file for what cards is) 
    
    Returns:
        (bool): returns true if there is three of a kind else returns false

    Examples:
        print(three_of_a_kind([[3, '♥'], [9, '♦'], [3, '♣'], [2, '♦'], [3, '♠'], [6, '♠'], [3, '♦'], [6, '♦'], [4, '♠'], [7, '♦'], [10, '♦'], [10, '♥']] ))
        >>> True 
        
        print(three_of_a_kind([['King', '♠'], ['Ace', '♠'], [9, '♦']]))
        >>> False

    """
    RANK_OF_CARD = 0
    CANNOT_MAKE_THREE = 3
    NO_INDEX_ERROR_POP_THREE = 3
    THREE_REMOVED_OFFSET = 3
    TWO_REMOVED_OFFSET = 2
    ONE_REMOVED_OFFSET = 1
    THERE_IS_THIRD_POP = 3
    READD_SECOND_POPS_OFFSET = 2
    READD_ALL_POPS_OFFSET = 3
    INDEX_ERROR_PLACEHOLDER = 0
    list = [x[RANK_OF_CARD] for x in arr]
    mut_insertion_sort(list)

    #we iterate through all the numbers in the list
    LIST_INDEX_LENGTH = len(list) - 1
    LIST_INDEX_MIN = 0
    ITERATE_BACKWARD = -1
    INCLUSIVE_OFFSET = 1
    for i in range(LIST_INDEX_LENGTH, LIST_INDEX_MIN - INCLUSIVE_OFFSET, ITERATE_BACKWARD):
        target = list.pop()
        i -= ONE_REMOVED_OFFSET 

        #if the function hasnt returned true and the amt of items in the list is less than 3 it cant be true
        if len(list) < CANNOT_MAKE_THREE:
            return False

        #we can do this becuase the list is sorted im so sorry 
        #but look O(n) time excluding the sorting algorhtm
        if len(list) > NO_INDEX_ERROR_POP_THREE:
            first_pop = list.pop()
            second_pop = list.pop()
            third_pop = list.pop()
            i -= THREE_REMOVED_OFFSET 
        else:
            first_pop = list.pop()
            second_pop = list.pop()
            third_pop = INDEX_ERROR_PLACEHOLDER 
            i -= TWO_REMOVED_OFFSET 

        #for no index error
        if  third_pop != INDEX_ERROR_PLACEHOLDER:
            if target == third_pop:
                return False
            elif target == second_pop:
                return True
            elif target == first_pop:
                list.append(third_pop)
                list.append(second_pop)
                i += READD_SECOND_POPS_OFFSET
            else:
                list.append(third_pop)
                list.append(second_pop)
                list.append(first_pop)
                i += READD_ALL_POPS_OFFSET
        else:
            if target == second_pop:
                return True
            elif target == first_pop:
                list.append(second_pop)
                i += READD_SECOND_POPS_OFFSET - ONE_REMOVED_OFFSET
            else:
                list.append(second_pop)
                list.append(first_pop)
                i += READD_ALL_POPS_OFFSET - ONE_REMOVED_OFFSET
        
    return False 
    
def pairs_amt(arr):
    """
    Check the array for the number pairs(meaning 2 % num = 0) 

    Args:
        (list)arr: an array of cards(check the constant in the main file for what cards is) 
    Returns:
        (int): will return the ammount of pairs in the hand

    Examples:
        print(pairs_amt())
    """
    RANK_OF_CARD = 0
    THREE_REMOVED_OFFSET = 3
    TWO_REMOVED_OFFSET = 2
    ONE_REMOVED_OFFSET = 1
    THERE_IS_THIRD_POP = 3
    THERE_IS_SECOND_POP = 2
    READD_THIRD_POP_OFFSET = 1
    READD_SECOND_POPS_OFFSET = 2
    READD_ALL_POPS_OFFSET = 3
    CANNOT_MAKE_PAIR = 2
    NO_INDEX_ERROR_POP_THREE = 3
    INDEX_ERROR_POP_TWO = 2
    ONE_PAIR = 1
    TWO_PAIR = 2
    HAND_NOT_CHECKED = 0
    INDEX_ERROR_PLACEHOLDER = 0

    #create a list of only the ranks of all the cards
    list = [x[RANK_OF_CARD] for x in arr]

    #sort the cards, was originally so i could use binary sort, but i found something faster
    mut_insertion_sort(list)
    #set the ammount of pairs to 0, because none of the hand has been checked yet
    pairs_amt = HAND_NOT_CHECKED 

    #iterate through all the cards in the list backwards due to .pop() and .append() being o(1) meanwhile .append(n) and .pop(n) being o(n)
    #this makes more sence later
    LIST_INDEX_LENGTH = len(list) - 1
    ITERATE_BACKWARD = -1
    INCLUSIVE_OFFSET = 1
    LIST_INDEX_MIN = 0
    for i in range(LIST_INDEX_LENGTH, LIST_INDEX_MIN - INCLUSIVE_OFFSET, ITERATE_BACKWARD):
        target = list.pop()
        i -= ONE_REMOVED_OFFSET 

        #if the array has less than two items inside of it, it isspossible for there to be another pair 
        if len(list) < CANNOT_MAKE_PAIR:
            break

        #we can do this becuase the list is sorted im so sorry 
        #but look O(n) time excluding the sorting algorhtm
        if len(list) > NO_INDEX_ERROR_POP_THREE:
            #create the items that we will check the target to 
            first_pop = list.pop() #the item before the current target
            second_pop = list.pop() #the item behind the target by 2  
            third_pop = list.pop() #the item three behind the target
            #offset the iterattion of the for loop due to the length of the list being changed
            i -= THREE_REMOVED_OFFSET 

        #this part ensure that we get no errors when there are only 2 items left in the list
        elif len(list) > INDEX_ERROR_POP_TWO:
            first_pop = list.pop() #the item before the current target
            second_pop = list.pop() #the item behind the target by 2  
            third_pop = INDEX_ERROR_PLACEHOLDER
            #offset the iterattion of the for loop due to the length of the list being changed
            i -= TWO_REMOVED_OFFSET 
        
        #this part ensure that we get no errors when there are only 1 item left in the list
        else:
            first_pop = list.pop() #the item before the current target
            second_pop = INDEX_ERROR_PLACEHOLDER #the item behind the target by 2  
            third_pop = INDEX_ERROR_PLACEHOLDER
            #offset the iterattion of the for loop due to the length of the list being changed
            i -= ONE_REMOVED_OFFSET 

        #this check ensure we dont check the third pop when there have been no changes to it because the list is too short
        if  third_pop != INDEX_ERROR_PLACEHOLDER:
            if target == third_pop:
                #change the ammout of pairs, due to the target being equal to the third pop(the item three behind it in the list) 
                #and due to the list being sorted, when third pop is equal to the target there would be four of the item 
                pairs_amt += TWO_PAIR 
            elif target == second_pop:
                #ensure that the items with a different value are readded to the list
                list.append(third_pop)
                #offset the iterattion of the for loop due to the length of the list being changed
                i += READD_THIRD_POP_OFFSET 
            elif target == first_pop:
                pairs_amt += ONE_PAIR 
                #ensure that the items with a different value are readded to the list
                list.append(third_pop)
                list.append(second_pop)
                #offset the iterattion of the for loop due to the length of the list being changed
                i += READD_SECOND_POPS_OFFSET 
            else:
                #readd all the removed items into to the list due to them all being different to the target
                list.append(third_pop)
                list.append(second_pop)
                list.append(first_pop)
                #offset the iterattion of the for loop due to the length of the list being changed
                i += READD_ALL_POPS_OFFSET

        #this check ensure we dont check the third pop when there have been no changes to it because the list is too short
        elif second_pop != INDEX_ERROR_PLACEHOLDER:
        #if there are two or three items that are identical to the target(target == second_pop || target == first_pop)
        #the ammount of pairs will go up, while we readd the unidentical items back into the list
            if target == first_pop:
                pairs_amt += ONE_PAIR 
                #ensure that the items with a different value are readded to the list
                list.append(second_pop)
                #offset the iterattion of the for loop due to the length of the list being changed
                i += READD_SECOND_POPS_OFFSET  - ONE_REMOVED_OFFSET 

            #case where there are no equal items to the current target 
            else:
                #readd all the removed items into to the list due to them all being different to the target
                list.append(second_pop)
                list.append(first_pop)
                #offset the iterattion of the for loop due to the length of the list being changed
                i += READD_ALL_POPS_OFFSET - ONE_REMOVED_OFFSET 
            
        else:
            if target == first_pop:
                pairs_amt += ONE_PAIR
            else:
                list.append(first_pop)
                i += READD_SECOND_POPS_OFFSET - TWO_REMOVED_OFFSET 
        
        print(list)
        
    return pairs_amt 

def highest_pair(arr):
    """
    Check the array for the highest number pair('s)(meaning 2 % num = 0) 

    Args:
        (list)arr: an array of cards(check the constant in the main file for what cards is) 

    Returns:
        (list): in cases where there is either a quad or pair in the chosen hand 
        or
        (string): in a case where there are no pairs in the chosen hand

    Examples:
    """
    #create a list of only the ranks of all the cards
    list = [x[0] for x in arr]
    #sort the cards, was originally so i could use binary sort, but i found something faster
    mut_insertion_sort(list)
    #set the ammount of pairs to 0, because none of the hand has been checked yet
    pairs_amt = 0

    THREE_REMOVED_OFFSET = 3
    TWO_REMOVED_OFFSET = 2
    ONE_REMOVED_OFFSET = 1
    THERE_IS_THIRD_POP = 3
    THERE_IS_SECOND_POP = 2
    READD_THIRD_POP_OFFSET = 1
    READD_ALL_POPS_OFFSET = 3
    CANNOT_MAKE_PAIR = 2
    NO_INDEX_ERROR_POP_THREE = 3
    INDEX_ERROR_POP_TWO = 2
    INDEX_ERROR_PLACEHOLDER = 0

    #iterate through all the cards in the list backwards due to .pop() and .append() being o(1) meanwhile .append(n) and .pop(n) being o(n)
    #this makes more sence later
    LIST_INDEX_LENGTH = len(list) - 1
    ITERATE_BACKWARD = -1
    LIST_INDEX_MIN = 0
    for i in range(LIST_INDEX_LENGTH, LIST_INDEX_MIN - 1, ITERATE_BACKWARD):
        target = list.pop()
        i -= ONE_REMOVED_OFFSET 

        #if the array has less than two items inside of it, it isspossible for there to be another pair 
        if len(list) < CANNOT_MAKE_PAIR:
            break

        #we can do this becuase the list is sorted im so sorry 
        #but look O(n) time excluding the sorting algorhtm

        if len(list) > NO_INDEX_ERROR_POP_THREE:
            #create the items that we will check the target to 
            first_pop = list.pop() #the item before the current target
            second_pop = list.pop() #the item behind the target by 2  
            third_pop = list.pop() #the item three behind the target
            #offset the iterattion of the for loop due to the length of the list being changed
            i -= THREE_REMOVED_OFFSET

        #this part ensure that we get no errors when there are only 2 items left in the list
        elif len(list) > INDEX_ERROR_POP_TWO:
            first_pop = list.pop() #the item before the current target
            second_pop = list.pop() #the item behind the target by 2  
            third_pop = INDEX_ERROR_PLACEHOLDER
            #offset the iterattion of the for loop due to the length of the list being changed
            i -= TWO_REMOVED_OFFSET 
        
        #this part ensure that we get no errors when there are only 1 item left in the list
        else:
            first_pop = list.pop() #the item before the current target
            second_pop = INDEX_ERROR_PLACEHOLDER #the item behind the target by 2  
            third_pop = INDEX_ERROR_PLACEHOLDER
            #offset the iterattion of the for loop due to the length of the list being changed
            i -= ONE_REMOVED_OFFSET 


        #due to us iterating through the list backwards the first pair, or quad it finds will be the highest pair
        #this check ensure we dont check the third pop when there have been no changes to it because the list is too short

        #this check ensure we dont check the third pop when there have been no changes to it because the list is too short
        if  third_pop != INDEX_ERROR_PLACEHOLDER:
            if target == third_pop:
                return [target, first_pop, second_pop, third_pop]
            elif target == second_pop:
                #ensure that the items with a different value are readded to the list
                list.append(third_pop)
                #offset the iterattion of the for loop due to the length of the list being changed
                i += READD_THIRD_POP_OFFSET 
            elif target == first_pop:
                return [target, first_pop]
            else:
                #readd all the removed items into to the list due to them all being different to the target
                list.append(third_pop)
                list.append(second_pop)
                list.append(first_pop)
                #offset the iterattion of the for loop due to the length of the list being changed
                i += READD_ALL_POPS_OFFSET

        #this check ensure we dont check the third pop when there have been no changes to it because the list is too short
        elif second_pop != INDEX_ERROR_PLACEHOLDER:
        #if there are two or three items that are identical to the target(target == second_pop || target == first_pop)
        #the ammount of pairs will go up, while we readd the unidentical items back into the list
            elif target == first_pop:
                return [target, first_pop]
            #case where there are no equal items to the current target 
            else:
                #readd all the removed items into to the list due to them all being different to the target
                list.append(second_pop)
                list.append(first_pop)
                #offset the iterattion of the for loop due to the length of the list being changed
                i += READD_ALL_POPS_OFFSET - ONE_REMOVED_OFFSET 
            
        else:
            if target == first_pop:
                return [target, first_pop]
            else: 
                list.append(second_pop)
        
    #if no pair has been found yet then 
    #                     ↓
    return "There are no pairs in this hand" 

def test_cases():

    return True

def main():
    """
    what are you even supposed to put for the main docstring like
    'it runs the code......' lol
    """
    test_cases()

    #create the suits that cards can be
    SUITS = ['♥', '♠', '♦', '♣']
    #create the rank that the card can be
    RANKS = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
    #create a list of all the card to choose from
    CARDS = [[rank, suit] for rank in RANKS for suit in SUITS]

    #create the hands
    MAX_HAND_SIZE = 13 #the max size the hand can be
    MIN_HAND_SIZE = 1  #the minimum size the hand can be
    HAND_SIZE = lambda a: a + random.randint(MIN_HAND_SIZE, MAX_HAND_SIZE)

    HANDS_AMT = 4 #the ammount of hands that are to be made
    RUN_HANDS_FUNCTION = 0 #ensures that when used by other coders this should be used to run the lambda

    #we make a hand for the amount of times we should make a hand and put that in an array
    hands = [make_hand(CARDS, HAND_SIZE(RUN_HANDS_FUNCTION)) for j in range(HANDS_AMT)]

    #i just use this for the switch cases or else they dont work dont worry i wont use object oriented
    class constant():
        OP_ALL_EQUAL = 1
        OP_SHUFFLE = 2
        OP_THREE_OF_A_KIND = 3
        OP_PAIRS_AMT = 4
        OP_HIGHEST_PAIR = 5

    OP_GO_BACK = 6
    OP_REROLL = 5
    FIX_INDEX = 1
    NO_HAND_NUM = 0
    MIN_HAND_NUM = 1

    #this is where the UI of the program starts
    while True:
        #this improves the looks when exiting the program as well as makes sure that the user inputs a number when they input something
        try:
            hand_num = 0 #is going to be the hand that the user has picked
            while hand_num == 0: #while the user has not picked a valid hand make them chose a hand

                #prints out all the hands in a nice format
                for i in range(HANDS_AMT):
                    USER_HAND_INDEX = i + FIX_INDEX
                    CURRENT_HAND = i
                    print(f"Hand #{USER_HAND_INDEX}:\n{hands[CURRENT_HAND]} \n")

                print("Which hand do you want to check, press 5 to remake them, or Ctrl C to exit")
                hand_num = int(input()) #the input of what hand that the user has chosen
                
                #if the user has chosen an invalid number for the input
                if (hand_num > OP_REROLL) or (hand_num < MIN_HAND_NUM):
                    #make the handnum back to 0 to make sure they choose a valid number
                    hand_num = NO_HAND_NUM 
                    print("The value you've inputed is not one of the hands")
                
                #if the user chooses to reroll the hands
                if hand_num == OP_REROLL:
                    #we rerun the make_hand function to remake the hands
                    hands = [make_hand(CARDS, HAND_SIZE(RUN_HANDS_FUNCTION)) for j in range(HANDS_AMT)]
                    #set the hand_num to 0 to make sure that the user has chosen a valid hand
                    hand_num = NO_HAND_NUM
                #the use has chosen a valid hand
                else:
                    #change the number the user has chose to what its index would be in the array
                    hand_num -= FIX_INDEX 
                    rank_to_int(hands[hand_num])
                    #exit the loop because the user has chosen as valid hand
                    break


            while True:
                #idk if i have to say but
                #shows the user the operations that they can do on the program
                print("What operation do you want to do on the hand:")
                print("   1. Check if all cards are equal")
                print("   2. Shuffle the hand")
                print("   3. Check for three of a kind")
                print("   4. Count for pairs")
                print("   5. Find the highest Pair")
                print("   6. Go Back")
                operation = int(input()) #gets what operation that the user wants to do
                print("\n")

                #unless you dont know, this is pythons switch bc they just have to be special
                match operation:

                    #have to type cast all to int or else a swich case wouldn't work because of a valueError
                    case constant.OP_ALL_EQUAL:
                        #prints the output of all_equal for the chozen hand
                        print(all_equal(hands[hand_num]))
                        #change all the ranks in the hands into their string varient if they have one
                        int_to_rank(hands[hand_num])
                        break
                    case constant.OP_SHUFFLE:
                        #idk why but the function is immutible so we have to ensure that the hand is equal to its reshuffled state
                        hands[hand_num] = shuffle(hands[hand_num])
                        #prints the output of shuffle for the chozen hand
                        print(shuffle(hands[hand_num]))
                        #change all the ranks in the hands into their string varient if they have one
                        int_to_rank(hands[hand_num])
                        break
                    case constant.OP_THREE_OF_A_KIND:
                        #prints the output of shuffle for the chozen hand
                        print(three_of_a_kind(hands[hand_num]))
                        #change all the ranks in the hands into their string varient if they have one
                        int_to_rank(hands[hand_num])
                        break
                    case constant.OP_PAIRS_AMT:
                        #prints the output of shuffle for the chozen hand
                        print(pairs_amt(hands[hand_num]))
                        #change all the ranks in the hands into their string varient if they have one
                        int_to_rank(hands[hand_num])
                        break
                    case constant.OP_HIGHEST_PAIR:
                        #prints the output of shuffle for the chozen hand
                        print(highest_pair(hands[hand_num]))
                        #change all the ranks in the hands into their string varient if they have one
                        int_to_rank(hands[hand_num])
                        break
                    case constant.OP_GO_BACK:
                        #go back because the user messed up or something and chose the wrong hand
                        #change all the ranks in the hands into their string varient if they have one
                        int_to_rank(hands[hand_num])
                        break
                    case _:
                        #make sure that the user has chosen a valid operation
                        print("The number you've entered is not one of the options") 


        #makes the exiting of the program look cleaner
        except KeyboardInterrupt:
            break

        #make sure that the user inputs an interger when they input something
        except ValueError:
            print("The awnser you've typed is not a interger please try again")

if __name__ == "__main__":
    main()
