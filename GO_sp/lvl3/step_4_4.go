package main

func CountingSort(contacts []string) map[string]int {
	countsort := make(map[string]int)

	for _, phone := range contacts {
		countsort[phone]++
	}

	return countsort
}