package main

import (
	"strings"
	"fmt"
	"sort"
	"unicode"
)

func getTopWords(wordMap map[string]int, n int) []string {
	keys := make([]string, 0, len(wordMap))
	for k := range wordMap {
		keys = append(keys, k)
	}

	sort.Slice(keys, func(i, j int) bool {
		return wordMap[keys[i]] > wordMap[keys[j]]
	})

	if len(keys) > n {
		keys = keys[:n]
	}

	return keys
}

func cleanWord(s string) string {
	return strings.Map(func(r rune) rune {
		if unicode.IsLetter(r) || unicode.IsNumber(r) {
			return r
		}
		return -1
	}, s)
}

func AnalyzeText(text string) {
	at_map := make(map[string]int)
	text = strings.ToLower(text)
	words := strings.Fields(text)

	cleanWords := make([]string, 0, len(words))
	for _, word := range words {
		clean := cleanWord(word)
		if clean != "" {
			cleanWords = append(cleanWords, clean)
		}
	}

	word_count := len(cleanWords)
	unique_word_count := 0
	max_count_in_text := 0
	max_count_in_text_key := ""

	for _, word := range cleanWords {
		at_map[word]++
	}

	for key, count := range at_map {
		if count > max_count_in_text {
			max_count_in_text = count
			max_count_in_text_key = key
		}

		unique_word_count++
	}

	top_five_words := getTopWords(at_map, 5)

	fmt.Printf("Количество слов: %d\n", word_count)
	fmt.Printf("Количество уникальных слов: %d\n", unique_word_count)
	fmt.Printf("Самое часто встречающееся слово: \"%s\" (встречается %d раз)\n", max_count_in_text_key, max_count_in_text)
	fmt.Println("Топ-5 самых часто встречающихся слов:")
	for _, word := range top_five_words {
		count := at_map[word]
		fmt.Printf("\"%s\": %d раз\n", word, count)
	}
}

func main() {
	AnalyzeText("one two two three three three four four four four five five five five five")
	AnalyzeText("Go очень очень очень ОЧЕНЬ ОчЕнь очень оЧЕНь классный классный! go просто, ну просто классный. GO Классный!")
	AnalyzeText("Я так люблю море. Я на море. Я так люблю. Море! Я море!!! ЛЮБЛЮ МОРЕ")
}