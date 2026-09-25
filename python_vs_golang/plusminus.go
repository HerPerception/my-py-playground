package main

import "fmt"

func plusMinus(arr []int32) {
    // Write your code here
    pos := float64(0)
    neg := float64(0)
    zero := float64(0)
    for _, num := range arr {
        if num > 0 {
            pos++
        } else if num < 0 {
            neg++
        } else if num == 0 {
            zero++
        }
    }  
    div := float64(len(arr))
    fmt.Println(pos/div)
    fmt.Println(neg/div)
    fmt.Println(zero/div)
}
