package main

import "fmt"
func Age_Category(age int) string {
	if age < 0 {
		return "Invalid age"
	} else if age < 13 {
		return "Child"
	} else if age < 18 {
		return "Teenager"
	} else if age < 65 {
		return "Adult"
	}
	return "Senior"
}
func main() {
	fmt.Println(Age_Category(17))
}