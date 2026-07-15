package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func main() {
	// STEP 1: Initialize a scanner to read user input from the terminal.
	scanner := bufio.NewScanner(os.Stdin)
	var input string
	fmt.Println("Welcome To CLI Calculator")

	// STEP 2: Start an infinite loop to keep the calculator running.
CalculatorLoop:
	for {
		// STEP 3: Prompt user to choose between running the calculator or viewing help guidelines.
		fmt.Println("Choose operation: (Calculator, Help)")
		scanner.Scan()
		input = scanner.Text()

		// STEP 4: If user types "Help", display the supported math operations and formats.
		if input == "Help" {
			fmt.Println("Addition: num1 + num2")
			fmt.Println("Subtraction: num1 - num2")
			fmt.Println("Multiplication: num1*num3")
			fmt.Println("Division: num1/num2")
			fmt.Println("Square: num1^num2")
			fmt.Println("Squareroot: number")
		}

		// STEP 5: If user types "Calculator", start the calculation process.
		if input == "Calculator" {
			fmt.Println("Enter values to perform operation:")
		CalculatorStart:
			scanner.Scan()
			newInput := scanner.Text()
			var newStr string

			// STEP 6: Remove all spaces from the user's input string.
			var builder strings.Builder
			for _, ch := range newInput {
				if ch == ' ' {
					continue
				} else {
					builder.WriteRune(ch)
				}
			}
			newStr = builder.String()

			// STEP 7: Find the mathematical operator (+, -, *, /) and its index position.
			split := 0
			operator := ""
			hasOperator := false
			for i := range newStr {
				// Looks for an operator, ensuring it is not the very first character (to allow negative numbers).
				if i > 0 && (newStr[i] == '+' || newStr[i] == '-' || newStr[i] == '*' || newStr[i] == '/' || newStr[i] == '^') {
					operator = string(newStr[i])
					split = i // Stores the index where the string will be split.
					hasOperator = true
					break
				}
			}

			if !hasOperator {
				rootNum, err := strconv.Atoi(newStr)
				if err != nil {
					fmt.Println("Wrong number of arguments. You must provide two numbers to multiply, add, divide or subtract, or provide a valid number to find square root. Type Help to see how.")
					goto CalculatorStart
				}
				fmt.Println(math.Sqrt(float64(rootNum)))
				goto CalculatorStart
			}

			// STEP 8: Validate that there are characters both before and after the operator.
			if len(newStr[:split]) == 0 || len(newStr[split+1:]) == 0 {
				fmt.Println("Wrong number of arguments. You must provide two numbers. Type Help to see how.")
				continue CalculatorLoop
			}

			// STEP 9: Initialize variables to hold the two converted integer numbers.
			firstNum := 0
			secondNum := 0

			// STEP 10: Convert the text before the operator into the first integer.
			first, err := strconv.Atoi(newStr[:split])
			if err != nil {
				fmt.Println("Error. Check input and try again. Type (Help) to see how the operation works.")
				continue CalculatorLoop
			} else {
				firstNum = first
			}

			// STEP 11: Convert the text after the operator into the second integer.
			second, err := strconv.Atoi(newStr[split+1:])
			if err != nil {
				fmt.Println("Error. Check input and try again. Type (Help) to see how the operation works.")
				continue CalculatorLoop
			} else {
				secondNum = second
			}

			// STEP 12: Perform the matching math calculation based on the detected operator.
			switch operator {
			case "+":
				fmt.Printf("%d + %d = %d\n", firstNum, secondNum, firstNum+secondNum)

			case "-":
				fmt.Printf("%d - %d = %d\n", firstNum, secondNum, firstNum-secondNum)

			case "*":
				fmt.Printf("%d * %d = %d\n", firstNum, secondNum, firstNum*secondNum)

			case "^":
				power := firstNum
				for range secondNum - 1 {
					power *= firstNum
				}
				fmt.Printf("%d ^ %d = %d\n", firstNum, secondNum, power)
			case "/":
				// STEP 12b: Prevent application crash by blocking division by zero.
				if secondNum == 0 {
					fmt.Println("No division by 0")
				} else {
					// If division results in a remainder, display it as a decimal (float).
					if firstNum%secondNum != 0 {
						fmt.Printf("%d / %d = %.3f\n", firstNum, secondNum, float64(firstNum)/float64(secondNum))
					} else {
						// If division is clean, display it as a whole integer.
						fmt.Printf("%d / %d = %d\n", firstNum, secondNum, firstNum/secondNum)
					}
				}
			}
		}

		// STEP 13: Ask the user whether to run another calculation or exit the program.
		fmt.Println("Choose option: (continue, exit)")
		scanner.Scan()
		if scanner.Err() != nil {
			fmt.Println("Error with input.")
		}
		option := scanner.Text()

		// STEP 14: Break the infinite loop if "exit" is selected; otherwise, restart from STEP 3.
		if option == "exit" {
			fmt.Println("Goodbye from CLI Calculator.")
			break
		} else {
			continue
		}
	}
}
