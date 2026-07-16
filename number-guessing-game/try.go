package main

import "fmt"

func main() {
	try := false
	for try != true {
		if try == true {
			break
		}
		for j := 0; j < 6; j++ {
			if j == 4 {
				try = true
				// break
			}
			fmt.Println(j)
		}
	}
}
