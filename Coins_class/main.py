from coin import Coin

def calculate_price(coin_list):
    total = 0
    for i in range(len(coin_list)):
        total += coin_list[i].value

    return total

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1

def test_calculate_price(ALL_COINS):
    assert calculate_price(ALL_COINS) == 41

def main():
    allcoins = []
    allcoins.append( Coin("quarter", 12, "Silver", 25) )
    allcoins.append( Coin("dime", 9, "Nickel", 10) )
    allcoins.append( Coin("nickel", 10.5, "Nickel", 5) )
    allcoins.append( Coin("penny", 9.5, "Copper", 1) )
    test_calculate_price(allcoins)

    for i in range(len(allcoins)):
        print(f"{allcoins[i]} \n")
    
    while True:
        target = input("Input the name of a Coin: ")
        if target == "exit":
            break

        target_index = linear_search([allcoins[i].coin_name for i in range(len(allcoins))], target)
        if target_index != -1:
            print(allcoins[target_index])
        else:
            print("Coin not Found")

if __name__ == "__main__":
    main()
