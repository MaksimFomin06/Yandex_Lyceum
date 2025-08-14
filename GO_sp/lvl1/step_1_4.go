package main

import (
	"fmt"
	"math"
)

func main() {
	var num float64

	fmt.Scanln(&num)

	if num < -1{
		fmt.Println(-1)
		return
	}

	answer := math.Sqrt(num)
	fmt.Printf("%.3f", answer)
}