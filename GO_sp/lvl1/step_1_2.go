package main

import (
	"fmt"
)

func main() {
	var num1, num2 int

	fmt.Scan(&num1, &num2)

	if num1 == num2 {
		fmt.Println("Числа равны")
		return
	} else if num1 < num2 {
		fmt.Println("Второе число больше первого")
		return
	} else if num1 > num2 {
		fmt.Println("Первое число больше второго")
		return
	}	
}