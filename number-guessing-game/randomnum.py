import random

# Generate a random integer between 1 and 100
quit = False

while quit == False:
    trial = 5
    num = random.randint(1, 100)

    print("Welcome To CLI Number Guessing Game.")
    print("I'm thinking of a number, could you tell what number it is?")
    guessnum = ""
    while guessnum != num:

        guessnum = input()

        try:
            guessnum = int(guessnum)
        except ValueError:
            print("Input is not a valid number.")

        if trial == 0 and guessnum != num:
            print(f"You have used up your trial limits. Failed this round. Number is {num}")
            print("Choose options: 1. Try another number 2. Quit")
            ops = input()
            if ops == "1":
                break
            else:
                quit = True
                break
        if guessnum < num:
            print("Too low. Try again.")
            trial -= 1

        elif guessnum > num:
            print("Too high. Try again")
            trial -= 1

        elif guessnum == num:
            print("Correct! You guessed right.")
            print("1. Continue playing game 2. Quit")
            resp = input()
            if resp == "1":
                break
            else:
               quit = True 

