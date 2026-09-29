package main

import "fmt"

func removeDuplicates(nums []int) int {
	//	newNums := []int{}
	uniqueMap := make(map[int]int)
	for i := 0; i < len(nums); i++ {
		num := nums[i]
		if val, exists := uniqueMap[num]; exists {
			uniqueMap[num] = val + 1
			nums = append(nums[:i], nums[i+1:]...)
			i--
		} else {
			uniqueMap[num] = 1
		}
	}
	fmt.Println(nums)
	return len(nums)

}

func call() {
	// 1. Define input and expected output slices
	nums := []int{1, 1, 2}      // Input array
	expectedNums := []int{1, 2} // The expected answer with correct length

	// 2. Call your implementation
	k := removeDuplicates(nums)

	// 3. Assert k matches the length of the expected slice
	if k != len(expectedNums) {
		panic(fmt.Sprintf("Assertion failed: k (%d) != expectedNums length (%d)", k, len(expectedNums)))
	}

	// 4. Assert elements match up to index k
	for i := 0; i < k; i++ {
		if nums[i] != expectedNums[i] {
			panic(fmt.Sprintf("Assertion failed: nums[%d] (%d) != expectedNums[%d] (%d)", i, nums[i], i, expectedNums[i]))
		}
	}

	fmt.Println("All assertions passed successfully!")

	fmt.Println(removeDuplicates([]int{0, 0, 1, 1, 1, 2, 2, 3, 3, 4}))
}
