package main

import (
	"fmt"
	"strings"
)

func main() {
	var count, summa int
	var word, text string

	fmt.Scanln(&count)
	fmt.Scanln(&word)

	for i := 0; i < count; i++ {
		fmt.Scan(&text)

		if strings.ToLower(word) == strings.ToLower(text) {
			summa += 1
		}
	}

	fmt.Println(summa)
}