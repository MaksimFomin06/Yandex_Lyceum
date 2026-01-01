package main

import "fmt"

func FindMaxKey(m map[int]int) int {
	var max_key int
	for key := range m {
		max_key = key
		break
	}
	for key := range m {
		if key > max_key {
			max_key = key
	 }
	}

	return max_key
}

func main() {
	m := map[int]int{
		19: 37,
		20: 38,
	}
	fmt.Println(FindMaxKey(m))
}