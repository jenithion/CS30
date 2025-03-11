mport random

#create a list of all the card to choose from
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
cards = [(suit, rank) for rank in ranks for suit in suits]

#create the hands
MAX_HAND_SIZE = 13
MIN_HAND_SIZE = 1
def hand_size():
    hand_size = random.randint(MIN_HAND_SIZE, MAX_HAND_SIZE)
    return hand_size

HANDS_AMT = 4
hands = [[random.choice(cards) for i in range(hand_size())] for j in range(HANDS_AMT)]

def main():
    while True:
        for i in range(HANDS_AMT):
            print(f"Hand #{i + 1}:\n{hands[i]} \n")

        print("which hand do you want to check")
        hand_num = int(input())

        print("What operation do you want to do on the hand:")
        print("   1. Check if all cards are equal")
        print("   2. Shuffle the hand")
        print("   3. Check for three of a kind")
        print("   4. Count for pairs")
        print("   5. Find the highest Pair")
        operation = input()
        match operation:
            case "1":
                all_equal()
            case "2":
                shuffle()
            case "3":
                three_of_a_kind()
            case "4":
                pairs_amt()
            case "5":
                highest_pair()
            case _:
                print("The character you've enterenterd is not one of the options") 

if __name__ == "__main__":
    main()
