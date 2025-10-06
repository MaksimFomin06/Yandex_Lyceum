package main

import "fmt"

func BuyFries(size string) {
	var rub int

	switch size {
	case "S":
		rub = 49
	case "M":
		rub = 89
	case "L":
		rub = 99
	default:
		rub = 0
	}

	var name string = "Картошка фри"

	printPrice(rub, name)
}

func BuyCola(size string) {
	var rub int

	switch size {
	case "S":
		rub = 99
	case "M":
		rub = 119
	case "L":
		rub = 139
	default:
		rub = 0
	}

	var name string = "Кола"

	printPrice(rub, name)
}

func printPrice(rub int, name string) {
	if rub == 0 {
		fmt.Println("Некорректный размер")
	} else {
		fmt.Printf("%s будет стоить %d рублей\n", name, rub)
	}
}
