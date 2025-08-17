package main

import "fmt"

func main() {
	var sign string
	var degrees int

	fmt.Scan(&sign, &degrees)

	switch {
	case sign == "+" && degrees > 20:
		fmt.Println("Стоит надеть майку и шорты")
	case sign == "+" && 10 <= degrees && degrees <= 20:
		fmt.Println("Стоит надеть штаны и кофту")
	case (sign == "-" && -5 <= degrees * (-1)) || (sign == "+" && degrees <= 9), degrees == 0:
		fmt.Println("Стоит надеть куртку") 
	default:
		fmt.Println("Стоит надеть зимнюю куртку")
	}
}