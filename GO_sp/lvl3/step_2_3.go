package main

import (
	"fmt"
)

func FindMaxMinInArray(array [10]int) (int, int) {
	max_num := array[0]
	min_num := array[0]
	
	for _, num := range array {
		max_num = max(max_num, num)
		min_num = min(min_num, num)
	}

	return max_num, min_num
}

func main() {
	input := [10]int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	max, min := FindMaxMinInArray(input)

	fmt.Print(max, min)
}