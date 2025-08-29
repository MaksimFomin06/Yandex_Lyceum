package main

import "fmt"

func main() {
	var word string

	fmt.Scanln(&word)

	for _, i := range word {
		if i == 'а' || i == 'о' {
			continue
		} else {
			fmt.Print(string(i))	
		}
	}
}