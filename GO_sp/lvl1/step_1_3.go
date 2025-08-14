package main

import (
	"fmt"
)

func main() {
	var rub, kop, price float32

	fmt.Scan(&rub, &kop, &price)

	if kop >= 100 {
		rub += float32(int(kop) / 100)
		kop = float32(int(kop) % 100)
	}
	if rub >= price {
		fmt.Println("Сегодня будет вкусный кофе!")
		return
	}

	fmt.Println("Стоит подкопить")
}