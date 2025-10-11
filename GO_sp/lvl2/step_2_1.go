package main

import "fmt"

func myFunc() int {
    // Задаём переменную
    a := 1

	return a
}

func main() {
    // Вызываем переменную
    myFunc()
    
    // Пробуем вывести переменную из функции myFunc в консоль
    fmt.Println(myFunc())
}