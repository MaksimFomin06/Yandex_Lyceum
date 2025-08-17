package main

import "fmt"

func main() {
	var text1, text2 string

	fmt.Scanln(&text1)
	fmt.Scanln(&text2)

	switch {
	case text1 == text2:
		fmt.Println("Ничья")
		return
	case (text1 == "камень" && text2 == "ножницы") || (text1 == "ножницы" && text2 == "бумага") || (text1 == "бумага" && text2 == "камень"):
		fmt.Println("Первый игрок победил")
	default:
		fmt.Println("Второй игрок победил")
	}
}