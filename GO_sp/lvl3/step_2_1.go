package main

import (
	"fmt"
)

func FiveSteps(array [5]int) [5]int {
	var new_arr [5]int

	for i := 0; i < len(array); i++ {
		new_arr[i] = array[len(array)-1-i]
	}

	return new_arr
}


func main() {
	fmt.Println(FiveSteps([5]int{1, 2, 3, 4, 5}))
}