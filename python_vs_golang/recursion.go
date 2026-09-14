/*============================================================================================
RECURSION is when a function calls itself. It should always have a base case or a stop condition
to avoid an infinite recursion.

The example is implememnted in Golang.
==============================================================================================*/

package main

import "fmt"

func main() {
	fmt.Println(tri_recursion(6))
}
func tri_recursion(k int) int {
	result := 0
	if k > 0 {
		result = k + tri_recursion(k-1)
		print(result)
	}
	return result
}
