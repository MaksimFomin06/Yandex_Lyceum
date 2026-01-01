package main

import (
	"unicode/utf8"
)

func DeleteLongKeys(m map[string]int) map[string]int {
	for key := range m {
		if utf8.RuneCountInString(key) < 6 {
			delete(m, key)
		}
	}

	return m
}