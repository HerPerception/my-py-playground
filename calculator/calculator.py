while True:
    userInput = input("Input number and operator. ")
    if userInput == "exit":
        break

    parts = userInput.split()
    if len(parts) != 3:
        print("Error: Please use spaces between numbers and operators (e.g., 23 / 5),or 'exit' to quit.")
        continue
    a, op, b = parts
    try:
        if op == "+":
            print(f"{a}+{b}={float(a)+float(b)}")
        elif op == "-":
            print(float(a)-float(b))
        elif op == "*":
            print(float(a)*float(b))
        elif op == "/":
            if b == "0":
                print("No division by 0")
            else:
                print(float(a)/float(b))
    except ValueError:
        print("Error, Input must be two valid numbers with an operator between and seperated by spaces. (eg. 23 * 6)")
        # askToContinue = input( "Type 'exit' to quit, or press Enter to continue: " )
        