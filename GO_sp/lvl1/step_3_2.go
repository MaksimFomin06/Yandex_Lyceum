package main

import "fmt"

func main() {
	var count int
	var mark float64

	fmt.Scanln(&count)

	for i := 0; i < count; i++ {
		fmt.Scanln(&mark)

		if mark >= 90 && mark <= 100 {
			fmt.Println("5")
		} else if mark >= 75 && mark <= 89 {
			fmt.Println("4")
		} else if mark >= 50 && mark <= 74 {
			fmt.Println("3")
		} else if mark >= 0 && mark <= 49 {
			fmt.Println("2")
		} else {
			fmt.Println("Неверный балл")
		}
	}
}