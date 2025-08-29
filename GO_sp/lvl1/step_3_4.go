package main

import "fmt"

func main() {
	var text string

	for {
		fmt.Scanln(&text)
		
		if text == "да" || text == "нет" || text == "чёрный" || text == "белый" {
			fmt.Println("Поражение")
			break
		} else {
			fmt.Println("Игра продолжается")
		}
	}
}