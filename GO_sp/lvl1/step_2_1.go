package main

import (
	"fmt"
)

func main() {
	var num1, num2, num3 float64

	fmt.Scan(&num1, &num2, &num3)

	switch {
	case num1 == num2 && num2 == num3:
		fmt.Println("Максимальное равенство")
	default:
		fmt.Println("Не равны")
	}
}