balance = 100
while True:
    print("Options: 1. Check Balance, 2. Deposit, or 3. Exit")
    ops = int(input("Input option number here: "))
    if ops == 1:
        print(f"Balance: {balance}.")
    elif ops == 2:
        amount = int(input("Enter amount: "))
        balance += amount
        print(f"Deposit successful. Balance: {balance}")
    elif ops == 3:
        print("Shutting down... Goodbye... ")
        break