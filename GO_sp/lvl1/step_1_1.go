package main

import (
	"fmt"
)

func main() {
	var text string

	fmt.Scanln(&text)

	if text != "Go" {
		fmt.Println("Я знаю только Go!")
		return
	}

	fmt.Println("Go!")
}