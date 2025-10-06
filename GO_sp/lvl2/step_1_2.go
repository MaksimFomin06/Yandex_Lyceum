package main

import "fmt"

func PrintFlightRow(flight_num string, city_start string, city_finish string, time float32, number_place int, geit int, is_finish bool) {
	if is_finish {
		fmt.Printf("| %s | %s—%s | регистрация закончилась, проходите к гейту: %d | длительность полёта %.1f часа |\n", flight_num, city_start, city_finish, geit, time)
	} else {
		fmt.Printf("| %s | %s—%s | %d регистрация продолжается |\n", flight_num, city_start, city_finish, number_place)
	}
}
