import sys
customer_balance = 150000
pin = 1245
def input_conversion(user_input):
    try:
        return int(user_input)
    except ValueError:
        print("Invalid input.")
        sys.exit()
    
def transfers(user_input):
    if user_input == 1:
        user_input = input("""
Enter Opay account number or select from past accounts:
""")
    elif user_input == 2:
        user_input = input("""
Enter Bank name or select from past accounts:
""")
        if len(user_input) != 10 and len(user_input) != 11:
            print("Invalid input.")
            sys.exit()
        else:
            user_input = input("""
Input or Choose Amount:
1. 500
2. 1000                               
3. 2000                               
4. 5000                               
5. 10000                               
""")
            user_input = input_conversion(user_input)
            while user_input > customer_balance:
                    user_input = input("Insuffient Amount.\n")
                    user_input = input_conversion(user_input)

            if user_input <= customer_balance:
                    user_input = input("Input Pin: \n")
                    user_input = input_conversion(user_input)
                    if user_input != pin:
                        print("Pin is invalid")
                    else:
                        print("Transaction Successful")
            
    

ussd_input = input("""====== Welcome To Opay USSD ==========
Select an option:
1. Transfer Money
2. Open Account
3. Buy Airtime/Data
4. Check Balance
5. Block Account
6. Exit
""")

ussd_input = input_conversion(ussd_input)

if ussd_input == 1:
    ussd_input = input("""
Select Option:
1. Send to Opay
2. Send to Other Banks
""")
    ussd_input = input_conversion(ussd_input)
    transfers(ussd_input)
    

