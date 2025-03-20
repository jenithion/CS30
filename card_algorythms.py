import random, copy

def make_hand(cards, hand_size):
    """
    Makes a hand given the list of cards and the size to make it

    Args:
        (list)cards: a list of all the 52 cards
        (int)hand_size: the size to make the hand
    
    Returns: 
        (list): return a list of cards from a new "deck"

    Examples:
        print(make_hand(CARDS, 8))
        >>> [[2, '♠'], [5, '♣'], [8, '♥'], ['Jack', '♥'], [5, '♥'], ['Queen', '♥'], [5, '♦'], [7, '♥'], [6, '♥'], ['Ace', '♠']]

        print(make_hand(CARDS, 2))
        >>> [[9, '♥'], [3, '♦']]

    """
    hand = []
    new_deck = copy.copy(cards)

    for i in range(hand_size):
        START_OF_DECK = 0
        LAST_OF_DECK = len(new_deck) - 1

        rand_card_num = random.randint(START_OF_DECK, LAST_OF_DECK)
        hand.append(new_deck[rand_card_num])
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
        card_list = [('♥', 4), ('♠', 6), ('♠', 3), ('♣', 6), ('♣', 6), ('♦', 10), ('♣', 10), ('♥', 5)]
        print(all_equal(card_list))
        >>> False

        card_list = [('♥', 3) , ('♣', 3), ('♦', 3)]
        print(all_equal(card_list))
        >>> True
    """
    RANK_OF_CARD = 0
    list = [x[RANK_OF_CARD] for x in arr]

    LIST_LEN = len(list)

    SUIT_AMT = 4
    if LIST_LEN > SUIT_AMT:
        return False

    for i in range(1, LIST_LEN):
        TARGET_NUMBER = i
        PREVIOUS_NUMBER = i - 1

        if list[PREVIOUS_NUMBER] != list[TARGET_NUMBER]:
            return False

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

    arr = [frozenset(x) for x in arr]
    arr = set(arr) 

    arr = [list(x) for x in arr]
    arr = list(arr)

    for x in arr:
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

    LIST_INDEX_LENGTH = len(list) - 1
    LIST_INDEX_MIN = 0
    ITERATE_BACKWARD = -1
    INCLUSIVE_OFFSET = 1
    for i in range(LIST_INDEX_LENGTH, LIST_INDEX_MIN - INCLUSIVE_OFFSET, ITERATE_BACKWARD):
        if len(list) < CANNOT_MAKE_THREE:
            return False

        target = list.pop()
        i -= ONE_REMOVED_OFFSET 

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
        print( pairs_amt([[2, '♠'], [5, '♣'], [8, '♥'], [11, '♥'], [5, '♥'], [12, '♥'], [5, '♦'], [7, '♥'], [6, '♥'], [1, '♠']]) )
        >>> 0 

        print( pairs_amt([[11, '♣'], [8, '♠'], [13, '♣'], [10, '♦'], [8, '♣'], [13, '♦']]) )
        >>> 2
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

    list = [x[RANK_OF_CARD] for x in arr]

    mut_insertion_sort(list)
    pairs_amt = HAND_NOT_CHECKED 

    LIST_INDEX_LENGTH = len(list) - 1
    ITERATE_BACKWARD = -1
    INCLUSIVE_OFFSET = 1
    LIST_INDEX_MIN = 0
    for i in range(LIST_INDEX_LENGTH, LIST_INDEX_MIN - INCLUSIVE_OFFSET, ITERATE_BACKWARD):
        if len(list) < CANNOT_MAKE_PAIR:
            break

        target = list.pop()
        i -= ONE_REMOVED_OFFSET 

        if len(list) > NO_INDEX_ERROR_POP_THREE:
            first_pop = list.pop() 
            second_pop = list.pop()
            third_pop = list.pop() 
            i -= THREE_REMOVED_OFFSET 

        elif len(list) > INDEX_ERROR_POP_TWO:
            first_pop = list.pop() 
            second_pop = list.pop()
            third_pop = INDEX_ERROR_PLACEHOLDER
            i -= TWO_REMOVED_OFFSET 
        
        else:
            first_pop = list.pop() 
            second_pop = INDEX_ERROR_PLACEHOLDER
            third_pop = INDEX_ERROR_PLACEHOLDER
            i -= ONE_REMOVED_OFFSET 

        if  third_pop != INDEX_ERROR_PLACEHOLDER:
            if target == third_pop:
                pairs_amt += TWO_PAIR 
            elif target == second_pop:
                list.append(third_pop)
                i += READD_THIRD_POP_OFFSET 
            elif target == first_pop:
                pairs_amt += ONE_PAIR 
                list.append(third_pop)
                list.append(second_pop)
                i += READD_SECOND_POPS_OFFSET 
            else:
                list.append(third_pop)
                list.append(second_pop)
                list.append(first_pop)
                i += READD_ALL_POPS_OFFSET

        elif second_pop != INDEX_ERROR_PLACEHOLDER:
            if target == first_pop:
                pairs_amt += ONE_PAIR 
                list.append(second_pop)
                i += READD_SECOND_POPS_OFFSET  - ONE_REMOVED_OFFSET 

            else:
                list.append(second_pop)
                list.append(first_pop)
                i += READD_ALL_POPS_OFFSET - ONE_REMOVED_OFFSET 
            
        else:
            if target == first_pop:
                pairs_amt += ONE_PAIR
            else:
                list.append(first_pop)
                i += READD_SECOND_POPS_OFFSET - TWO_REMOVED_OFFSET 
        
        
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
        print( highest_pair([[2, '♠'], [5, '♣'], [8, '♥'], [11, '♥'], [5, '♥'], [12, '♥'], [5, '♦'], [7, '♥'], [6, '♥'], [1, '♠']]) )
        >>> "There are no pairs in this hand"

        print( highest_pair([[8, '♠'], [13, '♣'], [10, '♦'], [8, '♣'], [13, '♦']]) )
        >>> [13, 13] 

        print( highest_pair([[6, '♦'], [10, '♠'], [2, '♥'], [5, '♣'], [10, '♦'], [5, '♠'], [12, '♥'], [5, '♥'], [2, '♠']]) )
        >>> [10, 10]
    """
    list = [x[0] for x in arr]
    mut_insertion_sort(list)
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

    LIST_INDEX_LENGTH = len(list) - 1
    ITERATE_BACKWARD = -1
    LIST_INDEX_MIN = 0
    for i in range(LIST_INDEX_LENGTH, LIST_INDEX_MIN - 1, ITERATE_BACKWARD):
        if len(list) < CANNOT_MAKE_PAIR:
            break

        target = list.pop()
        i -= ONE_REMOVED_OFFSET 

        if len(list) > NO_INDEX_ERROR_POP_THREE:
            first_pop = list.pop()
            second_pop = list.pop()
            third_pop = list.pop()
            i -= THREE_REMOVED_OFFSET

        elif len(list) > INDEX_ERROR_POP_TWO:
            first_pop = list.pop()
            second_pop = list.pop()
            third_pop = INDEX_ERROR_PLACEHOLDER
            i -= TWO_REMOVED_OFFSET 
        
        else:
            first_pop = list.pop()
            second_pop = INDEX_ERROR_PLACEHOLDER
            third_pop = INDEX_ERROR_PLACEHOLDER
            i -= ONE_REMOVED_OFFSET 

        if  third_pop != INDEX_ERROR_PLACEHOLDER:
            if target == third_pop:
                return [target, first_pop, second_pop, third_pop]
            elif target == second_pop:
                list.append(third_pop)
                i += READD_THIRD_POP_OFFSET 
            elif target == first_pop:
                return [target, first_pop]
            else:
                list.append(third_pop)
                list.append(second_pop)
                list.append(first_pop)
                i += READD_ALL_POPS_OFFSET

        elif second_pop != INDEX_ERROR_PLACEHOLDER:
            if target == first_pop:
                return [target, first_pop]
            else:
                list.append(second_pop)
                list.append(first_pop)
                i += READD_ALL_POPS_OFFSET - ONE_REMOVED_OFFSET 
            
        else:
            if target == first_pop:
                return [target, first_pop]
            else: 
                list.append(second_pop)
        
    return "There are no pairs in this hand" 

def test_all_equal():
    assert all_equal([[2, '♠'], [2, '♣'], [2, '♥']]) == True
    assert all_equal([[7, '♠'], [2, '♣'], [2, '♥'], [2, '♦']]) == False 

def test_shuffle():
    assert shuffle([[2, '♠'], [5, '♣'], [8, '♥'], ['Jack', '♥'], [5, '♥'], ['Queen', '♥'], [5, '♦'], [7, '♥'], [6, '♥'], ['Ace', '♠']]) != [[2, '♠'], [5, '♣'], [8, '♥'], ['Jack', '♥'], [5, '♥'], ['Queen', '♥'], [5, '♦'], [7, '♥'], [6, '♥'], ['Ace', '♠']]
    assert shuffle([[6, '♦'], [10, '♠'], [2, '♥'], [5, '♣'], [10, '♦'], [5, '♠'], ['Queen', '♥'], [5, '♥'], [2, '♠']]) != [[6, '♦'], [10, '♠'], [2, '♥'], [5, '♣'], [10, '♦'], [5, '♠'], ['Queen', '♥'], [5, '♥'], [2, '♠']]

def test_three_of_a_kind():
    assert three_of_a_kind([[2, '♠'], [5, '♣'], [8, '♥'], [11, '♥'], [5, '♥'], [11, '♥'], [5, '♦'], [7, '♥'], [6, '♥'], [1, '♠']]) == True
    assert three_of_a_kind([[13, '♣'], [8, '♠'], [13, '♣'], [10, '♦'], [8, '♣'], [12, '♦']]) == False

def test_pairs_amt():
    assert pairs_amt([[2, '♠'], [5, '♣'], [8, '♥'], [11, '♥'], [5, '♥'], [12, '♥'], [5, '♦'], [7, '♥'], [6, '♥'], [1, '♠']]) == 0 
    assert pairs_amt([[11, '♣'], [8, '♠'], [13, '♣'], [10, '♦'], [8, '♣'], [13, '♦']]) == 2

def test_highest_pair():
    assert highest_pair([[2, '♠'], [5, '♣'], [8, '♥'], [11, '♥'], [5, '♥'], [12, '♥'], [5, '♦'], [7, '♥'], [6, '♥'], [1, '♠']]) == "There are no pairs in this hand"
    assert highest_pair([[8, '♠'], [13, '♣'], [10, '♦'], [8, '♣'], [13, '♦']]) == [13, 13] 
    assert highest_pair([[6, '♦'], [10, '♠'], [2, '♥'], [5, '♣'], [10, '♦'], [5, '♠'], [12, '♥'], [5, '♥'], [2, '♠']]) == [10, 10]

def test_cases():
    test_all_equal()
    test_shuffle()
    test_three_of_a_kind()
    test_pairs_amt()
    test_highest_pair()
    return True

def main():
    """
    what are you even supposed to put for the main docstring like
    'it runs the code......' lol
    """
    test_cases()

    SUITS = ['♥', '♠', '♦', '♣']
    RANKS = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
    CARDS = [[rank, suit] for rank in RANKS for suit in SUITS]

    MAX_HAND_SIZE = 13
    MIN_HAND_SIZE = 1 
    HAND_SIZE = lambda a: a + random.randint(MIN_HAND_SIZE, MAX_HAND_SIZE)

    HANDS_AMT = 4
    RUN_HANDS_FUNCTION = 0

    hands = [make_hand(CARDS, HAND_SIZE(RUN_HANDS_FUNCTION)) for j in range(HANDS_AMT)]

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

    while True:
        try:
            hand_num = 0
            while hand_num == 0:

                for i in range(HANDS_AMT):
                    USER_HAND_INDEX = i + FIX_INDEX
                    CURRENT_HAND = i
                    print(f"Hand #{USER_HAND_INDEX}:\n{hands[CURRENT_HAND]} \n")

                print("Which hand do you want to check, press 5 to remake them, or Ctrl C to exit")
                hand_num = int(input())
                
                if (hand_num > OP_REROLL) or (hand_num < MIN_HAND_NUM):
                    hand_num = NO_HAND_NUM 
                    print("The value you've inputed is not one of the hands")
                
                if hand_num == OP_REROLL:
                    hands = [make_hand(CARDS, HAND_SIZE(RUN_HANDS_FUNCTION)) for j in range(HANDS_AMT)]
                    hand_num = NO_HAND_NUM
                else:
                    hand_num -= FIX_INDEX 
                    rank_to_int(hands[hand_num])
                    break

            while True:
                print("What operation do you want to do on the hand:")
                print("   1. Check if all cards are equal")
                print("   2. Shuffle the hand")
                print("   3. Check for three of a kind")
                print("   4. Count for pairs")
                print("   5. Find the highest Pair")
                print("   6. Go Back")
                operation = int(input())
                print("\n")

                match operation:
                    case constant.OP_ALL_EQUAL:
                        print(all_equal(hands[hand_num]))
                        int_to_rank(hands[hand_num])
                        break
                    case constant.OP_SHUFFLE:
                        hands[hand_num] = shuffle(hands[hand_num])
                        print(shuffle(hands[hand_num]))
                        int_to_rank(hands[hand_num])
                        break
                    case constant.OP_THREE_OF_A_KIND:
                        print(three_of_a_kind(hands[hand_num]))
                        int_to_rank(hands[hand_num])
                        break
                    case constant.OP_PAIRS_AMT:
                        print(pairs_amt(hands[hand_num]))
                        int_to_rank(hands[hand_num])
                        break
                    case constant.OP_HIGHEST_PAIR:
                        print(highest_pair(hands[hand_num]))
                        int_to_rank(hands[hand_num])
                        break
                    case constant.OP_GO_BACK:
                        int_to_rank(hands[hand_num])
                        break
                    case _:
                        print("The number you've entered is not one of the options") 

        except KeyboardInterrupt:
            break

        except ValueError:
            print("The awnser you've typed is not a interger please try again")

if __name__ == "__main__":
    main()
