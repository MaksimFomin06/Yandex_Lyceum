package main

import (
	"fmt"
)

func main() {
	var num int

	fmt.Scan(&num)

	if num == 0 {
		fmt.Println("Число 0")
		return
	} else if num <= 9 && num >= -9{
		fmt.Println("Число однозначное")
		return
	} else if num % 2 == 0 {
		fmt.Println("Число чётное")
		return
	} else if num >= 0 {
		fmt.Println("Число положительное")
		return
	} else if num < -9 && num % 2 != 0 {
		fmt.Println("Число красивое")
		return
	}
}