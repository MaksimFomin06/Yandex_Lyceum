package main

import (
	"fmt"
)

func PrettyArrayOutput(array [9]string) {
	counter := 1
	for _, word := range array {
		if 1 <= counter && counter <= 7 {
			fmt.Printf("%d я уже сделал: %s\n", counter, word)
		} else {
			fmt.Printf("%d не успел сделать: %s\n", counter, word)
		}

		counter++
	}
}

func main() {
	input := [9]string{
		"проснуться",
		"позавтракать",
		"сходить в школу",
		"пообедать",
		"погулять с друзьями",
		"сделать домашнюю работу",
		"попрограммировать на Go",
		"поужинать",
		"лечь спать",
	}
	PrettyArrayOutput(input)
}