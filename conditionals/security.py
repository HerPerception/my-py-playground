has_keycard = False
clearance_level = 0
while True:
    command = input("Enter command: ")

    if command == "swipe":
        has_keycard = True
        print("Keycard registered.")
    elif command == "authenticate":
        resp = input("Enter clearance number: ")
        clearance_level = int(resp)
    elif command == "enter":
        if has_keycard == True and clearance_level >= 5:
            print("Access Granted.")
        else:
            print("Access denied. Try again.")
    elif command == "quit":
        break
    else:
        print("Enter a valid command. (enter, swipe, authenticate, quit)")

