package delete_vowels

import "unicode"

func DeleteVowels(s string) string {
	vowels := map[rune]bool{
		'а': true, 'о': true, 'у': true, 'ы': true, 'э': true,
		'и': true, 'я': true, 'ё': true, 'ю': true, 'е': true,
	}

	var result []rune
	for _, r := range s {
		if !vowels[unicode.ToLower(r)] {
			result = append(result, r)
		}
	}
	return string(result)
}