import random

def all_equal(arr):
    list = [x[1] for x in arr]
    print(list)
    return True

def shuffle(arr):
    return True
    
def three_of_a_kind(arr):
    return True
    
def pairs_amt(arr):
    return True

def highest_pair(arr):
    return True

def main():
    #create a list of all the card to choose from
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    cards = [(suit, rank) for rank in ranks for suit in suits]

    #create the hands
    MAX_HAND_SIZE = 13
    MIN_HAND_SIZE = 1
    hand_size = lambda a: a + random.randint(MIN_HAND_SIZE, MAX_HAND_SIZE)

    HANDS_AMT = 4
    hands = [[random.choice(cards) for i in range(hand_size(0))] for j in range(HANDS_AMT)]

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
                    all_equal(hands[hand_num])
                    break
                case "2":
                    shuffle(hands[hand_num])
                    break
                case "3":
                    three_of_a_kind(hands[hand_num])
                    break
                case "4":
                    pairs_amt(hands[hand_num])
                    break
                case "5":
                    highest_pair(hands[hand_num])
                    break
                case _:
                    print("The character you've enterenterd is not one of the options") 

if __name__ == "__main__":
    main()
