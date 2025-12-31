package main

import (
	"fmt"
	"strings"
)

var numbers = map[string]string{
	"0": "ноль",
	"1": "один",
	"2": "два",
	"3": "три",
	"4": "четыре",
	"5": "пять",
	"6": "шесть",
	"7": "семь",
	"8": "восемь",
	"9": "девять",
	"+": "плюс",
	"-": "минус",
	"*": "умножить на",
	"/": "разделить на",
}

func NumbersToLetters(input string) string {
	result := input

	for digit, word := range numbers {
		result = strings.ReplaceAll(result, digit, word)
	}

	return result
}


func main() {
	fmt.Println(NumbersToLetters("(1 + 2)"))
}