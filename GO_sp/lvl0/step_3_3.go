package main

import "fmt"

func main() {
	var name string
	var apartmentNumber int
	var secretPassword int
	var time float64

	fmt.Scanln(&name)
	fmt.Scanln(&apartmentNumber)
	fmt.Scanln(&secretPassword)
	fmt.Scanln(&time)

	answer := fmt.Sprintf("Привет, %s! Приглашаю тебя на соревнование по программированию, которое пройдёт, как всегда, в квартире %d. Оно будет длиться примерно %.1f часа. Не забудь секретный пароль для входа: %d.", name, apartmentNumber, time, secretPassword)
	fmt.Println(answer)
}
