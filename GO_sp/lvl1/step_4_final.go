package main

import (
	"fmt"
)

func main() {
	var number int
	count := 0
	queue := make([]string, 5)
	
	for {
		var input string
		fmt.Scan(&input)

		if input == "очередь" {
				for i := 0; i < 5; i++ {
					if queue[i] != "" {
						fmt.Printf("%d. %s\n", i + 1, queue[i])
					} else {
						fmt.Printf("%d. -\n", i + 1)
					}
				}
				continue
		}
		if input == "количество" {
			freeSeets := 5 - count
			fmt.Printf("Осталось свободных мест: %d\n", freeSeets)
			fmt.Printf("Всего человек в очереди: %d\n", count)
			continue
		}

		if input == "конец" {
				for i := 0; i < 5; i++ {
					if queue[i] != "" {
						fmt.Printf("%d. %s\n", i + 1, queue[i])
					} else {
						fmt.Printf("%d. -\n", i + 1)
					}
				}
				return
		}
		
		fmt.Scan(&number)
		
		if number < 1 || number > 5 {
			fmt.Printf("Запись на место номер %d невозможна: некорректный ввод\n", number)
			continue
		} 
		
		if count == 5 {
			fmt.Printf("Запись на место номер %d невозможна: очередь переполнена\n", number)
			continue
		} 
		
		if queue[number-1] != "" {
			fmt.Printf("Запись на место номер %d невозможна: место уже занято\n", number)
			continue
		} 
		
		queue[number-1] = input
		count++
	}
}