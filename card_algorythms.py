import random, copy

def make_hand(cards, hand_size):
    hand = []
    new_deck = copy.copy(cards)
    for i in range(hand_size):
        rand_card_num = random.randint(0, len(new_deck) - 1)
        hand.append(new_deck[rand_card_num])
        new_deck.pop(rand_card_num)
    
    return hand

def rank_to_int(arr):
    for x in arr:
        match x[0]:
            case 'Ace':
                x[0] = 1
            case 'Jack':
                x[0] = 11
            case 'Queen':
                x[0] = 12
            case 'King':
                x[0] = 13

def int_to_rank(arr):
    for x in arr:
        match x[0]:
            case 1:
                x[0] = 'Ace'
            case 11:
                x[0] = 'Jack' 
            case 12:
                x[0] = 'Queen' 
            case 13:
                x[0] = 'King' 

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
    arr = [frozenset(x) for x in arr]
    arr = set(arr) 

    arr = [list(x) for x in arr]
    arr = list(arr)

    for x in arr:
        if type(x[0]) is string:
            x[0], x[1] = x[1], x[0]

    return arr
    
def three_of_a_kind(arr):
    list = [x[0] for x in arr]
    mut_insertion_sort(list)

    #we iterate through all the numbers in the list
    for i in range((len(list) - 1), -1, -1):
        current_amt = 1
        target = list.pop()
        i -= 1

        #if the function hasnt returned true and the amt of items in the list is less than 3 it cant be true
        if len(list) < 3:
            return False

        #we can do this becuase the list is sorted im so sorry 
        #but look O(n) time excluding the sorting algorhtm
        if len(list) < 3:
            first_pop = list.pop()
            second_pop = list.pop()
            i -= 2
        else:
            first_pop = list.pop()
            second_pop = list.pop()
            third_pop = list.pop()
            i -= 3

        #for no index error
        if  len(list) > 3:
            if target == third_pop:
                return False
        elif target == second_pop:
            i += 1
            list.append(third_pop)
            return True
        elif target == first_pop:
            i += 2
            list.append(third_pop)
            list.append(second_pop)
        else:
            i += 3
            list.append(third_pop)
            list.append(second_pop)
            list.append(first_pop)
        
    return False 
    
def pairs_amt(arr):
    list = [x[0] for x in arr]
    mut_insertion_sort(list)

    #we iterate through all the numbers in the list
    for i in range((len(list) - 1), -1, -1):
        current_amt = 1
        target = list.pop()
        i -= 1

        #if the function hasnt returned true and the amt of items in the list is less than 3 it cant be true
        if len(list) < 3:
            return False

        #we can do this becuase the list is sorted im so sorry 
        #but look O(n) time excluding the sorting algorhtm
        if len(list) < 3:
            first_pop = list.pop()
            second_pop = list.pop()
            i -= 2
        else:
            first_pop = list.pop()
            second_pop = list.pop()
            third_pop = list.pop()
            i -= 3

        #for no index error
        if  len(list) > 3:
            if target == third_pop:
                pairs_amt += 2
        elif target == second_pop:
            i += 1
            list.append(third_pop)
        elif target == first_pop:
            i += 2
            pairs_amt += 1
            list.append(third_pop)
            list.append(second_pop)
        else:
            i += 3
            list.append(third_pop)
            list.append(second_pop)
            list.append(first_pop)
        
    return pairs_amt 

def highest_pair(arr):
    list = [x[0] for x in arr]
    mut_insertion_sort(list)

    #we iterate through all the numbers in the list
    for i in range((len(list) - 1), -1, -1):
        #if the function hasnt returned true and the amt of items in the list is less than 3 it cant be true
        if len(list) < 3:
            return False

        current_amt = 1
        target = list.pop()
        i -= 1

        #we can do this becuase the list is sorted
        if len(list) < 3:
            first_pop = list.pop()
            second_pop = list.pop()
            i -= 2
        else:
            first_pop = list.pop()
            second_pop = list.pop()
            third_pop = list.pop()
            i -= 3

        if  len(list) > 3 and target == third_pop:
            return [target, first_pop, second_pop, third_pop]
        elif target == second_pop:
            i += 1
            list.append(third_pop)
            return True
        elif target == first_pop:
            return [target, first_pop]
        else:
            i += 3
            list.append(third_pop)
            list.append(second_pop)
            list.append(first_pop)
        
        if current_amt % 2 == 0:
            paris_amt += 1
        
        i -= 1
        
    return pairs_amt 

def main():
    #create a list of all the card to choose from
    suits = ['♥', '♠', '♦', '♣']
    ranks = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
    cards = [[rank, suit] for rank in ranks for suit in suits]

    #create the hands
    MAX_HAND_SIZE = 13
    MIN_HAND_SIZE = 1
    hand_size = lambda a: a + random.randint(MIN_HAND_SIZE, MAX_HAND_SIZE)

    HANDS_AMT = 4
    hands = [make_hand(cards, hand_size(0)) for j in range(HANDS_AMT)]

    while True:
        try:
            hand_num = 0
            while hand_num == 0: 
                for i in range(HANDS_AMT):
                    print(f"Hand #{i + 1}:\n{hands[i]} \n")

                print("Which hand do you want to check, press 5 to remake them, or Ctrl C to exit")
                hand_num = int(input())
                
                if (hand_num > 5) or (hand_num < 1):
                    hand_num = 0
                    print("The value you've inputed is not one of the hands")
                if hand_num == 5:
                    hands = [make_hand(cards, hand_size(0)) for j in range(HANDS_AMT)]
                    hand_num = 0
                else:
                    hand_num -= 1
                    break


                
            for i in range(HANDS_AMT):
                rank_to_int(hands[i]) 

            while True:
                print("What operation do you want to do on the hand:")
                print("   1. Check if all cards are equal")
                print("   2. Shuffle the hand")
                print("   3. Check for three of a kind")
                print("   4. Count for pairs")
                print("   5. Find the highest Pair")
                print("   6. Go Back")
                operation = int(input())
                match operation:
                    case 1:
                        print(all_equal(hands[hand_num]))
                        break
                    case 2:
                        hands[hand_num] = shuffle(hands[hand_num])
                        print(shuffle(hands[hand_num]))
                        break
                    case 3:
                        print(three_of_a_kind(hands[hand_num]))
                        break
                    case 4:
                        print(pairs_amt(hands[hand_num]))
                        break
                    case 5:
                        print(highest_pair(hands[hand_num]))
                        break
                    case 6:
                        break
                    case _:
                        print("The number you've entered is not one of the options") 


            for i in range(HANDS_AMT):
                int_to_rank(hands[i]) 

        except KeyboardInterrupt:
            break

        except ValueError:
            print("The awnser you've typed is not a interger please try again")

if __name__ == "__main__":
    main()
