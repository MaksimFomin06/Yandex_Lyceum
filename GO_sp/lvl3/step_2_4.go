package main

func SumOfArray(array [6]int) int {
	sum := 0

	for _, num := range array {
		sum += num
	}

	return sum
}