def main():
    cost = 50
    amount_due = cost
    accepted_coins = [25, 10, 5]
    
    while amount_due > 0:
        print(f"Amount Due: {amount_due} cents")
        coin = int(input("Insert Coin: "))
        
        if coin in accepted_coins:
            amount_due -= coin
    
    change_owed = abs(amount_due)  # If amount_due is negative, it means change is due
    print(f"Change Owed: {change_owed} cents")

main()