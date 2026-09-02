import sys
print("Welcome to Sandies Fast Food. Below is the menu of food available today. \n 1. Fried rice and salad \n 2. Semo and Egusi \n 3. Yam and egg sauce \n 4. Akpu and Ofe-Onugbu")
food_menu = {1: "Fried rice and salad", 2: "Semo and Egusi", 3: "Yam and egg sauce", 4: "Akpu and Ofe-Onugbu"}
menu_input = (input("Input order to proceed: \n"))

try:
    menu_input = int(menu_input)
except ValueError:
    print("Sorry, this food is not available at this time. Only the food on the menu is available.")
    sys.exit()

if menu_input not in food_menu:
    print("Sorry, this food is not available at this time. Only the food on the menu is available")
else:
    print("Selection successful. You can now proceed too the payment section.")
