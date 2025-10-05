package main

import "fmt"

func GoOrNot(text string) {
	if text != "Go" {
		fmt.Println("Я знаю только Go!")
	} else {
		fmt.Println("Go!")
	}
}
