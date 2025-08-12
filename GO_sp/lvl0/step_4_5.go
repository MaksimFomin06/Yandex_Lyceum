package main

import (
	"fmt"
	"time"
)

func main() {
	var firstDate, secondDate string

	fmt.Scanln(&firstDate)
	fmt.Scanln(&secondDate)

	firstDateParse, err := time.Parse("2006-01-02", firstDate)
	secondDateParse, err := time.Parse("2006-01-02", secondDate)
	if (err != nil) {
		return
	}

	firstYear := firstDateParse.Year()
	secondYear := secondDateParse.Year()

	diff := firstYear - secondYear

	answer := fmt.Sprintf("%d year ago", diff)

	fmt.Println(answer)
}