package main

import (
	"strings"
	"fmt"
	"sort"
)

func getTopWords(wordMap map[string]int, n int) []string {
	type Pair struct {
		key string
		value int
	}

	pairs := make([]Pair, 0, len(wordMap))
	for k, v := range wordMap {
		pairs = append(pairs, pair[k, v])
	}

	sort.Slice(pairs, func(i, j int) bool) {
		return pairs[i].value > pairs[j].value
	}

	if len(pairs) > 5 {
		pairs = pairs[:5]
	}

	return pairs
}

func AnalyzeText(text string) {
	at_map := make(map[string]int)
	text = strings.ToLower(text)
	words := strings.Fields(text)
	word_count := len(words) // Количество слов в тексте
	unique_word_count := 0 // Количество уникальных слов
	max_count_in_text := 0
	max_count_in_text_key := 0 // Индекс самого частого слова

	for i := 0; i < word_count; i++ {
		idx := words[i]
		at_map[idx]++
	}

	for key := range at_map {
		if at_map[key] == 1 {
			unique_word_count++
		}
		if at_map[key] > max_count_in_text {
			max_count_in_text = at_map[key]
			max_count_in_text_key = key
		}
	}

	top_five_words := getTopWords(at_map, 5)

	fmt.Printf("Количество слов: %d\n", word_count)
	fmt.Printf("Количество уникальных слов: %d\n", unique_word_count)
	fmt.Printf("Самое часто встречающееся слово: %s (встречается %d раз)\n", at_map[max_count_in_text_key], unique_word_count)
	fmt.Println("Топ-5 самых часто встречающихся слов:")
	for key, value := range top_five_words {
		fmt.Printf("%s: %d раз\n", key, value)
	}
}

func main() {
	AnalyzeText("Самое часто встречающееся слово: *строка* (встречается *целое число* раз)")
}