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

func hasLowerCase(str string) bool {
	var isLower bool = false

	for _, char := range str {
		if unicode.IsLower(char) {
			isLower = true
			break
		}
	}

	return isLower
}

func hasMinimumLength(str string, minLength int) bool {
	return len(str) >= minLength
} 

func ratePassword(str string) string {
	var count int = 0
	var ans string

	if hasLowerCase(str) {
        count += 1
    }
    if hasMinimumLength(str, 8) {
        count += 1
    }
    if hasUpper(str) {
        count += 1
    }

	switch count {
	case 1:
		ans = "Слабый пароль"
	case 2:
		ans = "Средний пароль"
	case 3:
		ans = "Сложный пароль"
	default:
		ans = "Пароль недостаточно безопасен, придумайте новый"
	}

	return ans
}