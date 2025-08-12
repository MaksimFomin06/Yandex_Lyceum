package main

import (
	"fmt"
	"time"
)

func main() {
	var nowTime string

	fmt.Scanln(&nowTime)

	hourAndMinute, err := time.Parse("2006-01-02/15:04:05", nowTime)
	if err != nil {
		return
	}
	hour := hourAndMinute.Hour()
	minute := hourAndMinute.Minute()

	answer := fmt.Sprintf("Текущее время %d часов, %d минут. Ты точно не забыл про важные дела на сегодня?", hour, minute)

	fmt.Println(answer)
}