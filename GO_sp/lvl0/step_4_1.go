package main

import (
	"math"
	"fmt"
)

func main() {
	var name1, name2, name3 int
	fmt.Scanln(&name1)
	fmt.Scanln(&name2)
	fmt.Scanln(&name3)

	min := math.Min(float64(name1), math.Min(float64(name2), float64(name3)))
	fmt.Println(min)
}