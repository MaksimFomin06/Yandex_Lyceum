package main

import (
	"fmt"
	"strings"
	"strconv"
)

func main() {
	count := 0
	queue := make([]string, 5)
	
	for {
		var input string
		fmt.Scanln(&input)

		parts := strings.Split(input, "")

		if len(parts) == 1 {
			switch parts[0] {
			case "очередь":
				for i := 0; i < 5; i++ {
					if queue[i] != "" {
						fmt.Printf("%d. %s\n", i + 1, queue[i])
					} else {
						fmt.Printf("%d. -\n", i + 1)
					}
				}
			case "конец":
				for i := 0; i < 5; i++ {
					if queue[i] != "" {
						fmt.Printf("%d. %s\n", i + 1, queue[i])
					} else {
						fmt.Printf("%d. -\n", i + 1)
					}
				}
				return
			}
		} else if len(parts) == 2 {
			name := parts[0]
			number, err := strconv.Atoi(parts[1])

			if err != nil {
				break
			}
			
			if number < 1 || number > 5 {
				fmt.Printf("Запись на место номер %.d невозможна: некорректный ввод\n", number)
				continue
			} 
			
			if count == 5 {
				fmt.Printf("Запись на место номер %.d невозможна: очередь переполнена\n", number)
				continue
			} 
			if queue[number - 1] != "" {
				fmt.Printf("Запись на место номер %.d невозможна: место уже занято\n", number)
				continue
			} 
			
			queue[number-1] = name
			count++
		}
	}
}