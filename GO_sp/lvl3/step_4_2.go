package main

func SumOfValuesInMap(m map[int]int) int {
	summa := 0

	for _, value := range m {
		summa += value
	}

	return summa
}