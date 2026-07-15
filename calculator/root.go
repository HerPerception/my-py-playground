package main

import (
	"fmt"
	"math"
	"os"
	"strconv"
)

func Root() {
	numstr := os.Args[1]
	number, err := strconv.Atoi(numstr)
	if err != nil {
		fmt.Println(err)
		return
	}
	numberMap := make(map[int]int)
	i := 2
	for number > 1 {
		if number%i == 0 {
			if val, ok := numberMap[i]; ok {
				numberMap[i] = val + 1
			} else {
				numberMap[i] = 1
			}
			number /= i
		} else {
			i += 1
		}
	}

	fmt.Println(numberMap)
	root := 1
	for key, num := range numberMap {
		if num%2 == 0 {
			for num > 0 {
				root *= key
				num -= 2
			}
		} else {
			continue
		}
	}
	fmt.Println(root)
	fmt.Println(math.Sqrt(288))
}
