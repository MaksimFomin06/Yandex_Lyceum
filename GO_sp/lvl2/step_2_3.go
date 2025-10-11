package main

import (
	"unicode"
)

func hasUpper(str string) bool {
	var isUpper bool = false

	for _, char := range str {
		if unicode.IsUpper(char) {
			isUpper = true
			break  
		}
	}

	return isUpper
}

func hasMinimumLength(str string, minLength int) bool {
	return len(str) >= minLength
} 

func checkPassword(str string) bool {
	return (hasUpper(str) && hasMinimumLength(str, 8))
}
