package main

import (
	"fmt"
	"math"
)

func main() {
	var num1, num2 float64

	fmt.Scanln(&num1)
	fmt.Scanln(&num2)
	
	maxNum := math.Max(num1, num2)
	roundMaxNum := math.Round(maxNum)

	fmt.Println(roundMaxNum)
}