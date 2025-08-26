package main

import "fmt"

func main() {
	var text string

	for i := 0; i < 5; i++ {
		fmt.Scanln(&text)
		if text == "Go" {
			fmt.Println("Go!")
		} else {
			fmt.Println("Я знаю только Go!")
		}
	}
}