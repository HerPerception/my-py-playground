package main

import "fmt"

func main() {
	staircase(6)
}
func staircase(n int32) {
	// Write your code here
	for i := 1; i <= int(n); i++ {
		text := ""
		j := int(n)
		num := i
		for j > 0 {
			if j <= num {//Once j becomes equal or smaller than the number i is holding, begin to add #
				text += "#"
			} else {
				text += " "
			}
			j--
		}
		fmt.Println(text)
	}
}
