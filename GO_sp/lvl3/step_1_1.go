package main

import (
	"fmt"
	"strings"
	"unicode/utf8"
)


func CountLengthAndBytes(first, second string) string {
	merge := strings.Join([]string{first, second}, "")
	byte_count := len(merge)
	symbol_count := utf8.RuneCountInString(merge)
	answer := fmt.Sprintf("Объединённая строка: %s. Количество байт: %d. Количество символов: %d.", merge, byte_count, symbol_count)

	return answer
}

func main() {
	fmt.Println(CountLengthAndBytes("Привет,", " мир!"))
	fmt.Println(CountLengthAndBytes("I love ", " Yandex!"))
	fmt.Println(CountLengthAndBytes("你好", "不好意思"))
}