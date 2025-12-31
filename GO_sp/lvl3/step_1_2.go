package main

import (
	"unicode"
)

func CheckOnlyASCII(s string) bool {
	answer := true
	
	for _, symbol := range s {
		if symbol > unicode.MaxASCII {
			answer = false
			return answer
		}
	}

	return answer
}