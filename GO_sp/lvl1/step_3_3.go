package main

import "fmt"

func main() {
	var count int
	var number, summa, sale float64

	fmt.Scanln(&count)
	fmt.Scanln(&sale)

	for i := 0; i < count; i++ {
		fmt.Scanln(&number)
		summa += number
	}

	result := summa * (100 - sale) / 100
	
	if result == float64(int(result)) {
		fmt.Printf("%d", int(result))
	} else {
		fmt.Printf("%.3f", result)
	}
}