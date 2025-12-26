package main

import (
	"strings"
	"fmt"
)

func CheckLetters(text string) string {
	ans := strings.Contains(text, "е")
	sym_count := strings.Count(text, "е")

	ans_error := fmt.Sprintf("Количество возможных ошибок: %d, перепроверьте текст", sym_count)
	if ans {
		return ans_error
	} else {
		return "Текст готов к публикации!"
	}
}