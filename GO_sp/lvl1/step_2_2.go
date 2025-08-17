package main

import "fmt"

func main() {
	var num1, num2 string

	fmt.Scanln(&num1)
	fmt.Scanln(&num2)

	switch {
	case len(num1) >= 8 && len(num2) >= 8:
		fmt.Println("Оба пароля надёжные")
		return
	case len(num1) >= 8:
		fmt.Println("Только первый пароль надёжный")
	case len(num2) >= 8:
		fmt.Println("Только второй пароль надёжный")
	default:
		fmt.Println("Оба пароля ненадёжные")
	}
}