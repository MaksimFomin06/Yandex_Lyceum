package main

import (
	"errors"
	"fmt"
)

var ZeroError = errors.New("Пустой слайс")
var NegativeNum = errors.New("Отрицательное число")


func UnderLimit(nums []int, limit int, n int) ([]int, error) {
	if nums == nil {
		return nil, ZeroError
	} else if n < 0 {
		return nil, NegativeNum
	}
	counter := 0
	var ans_arr []int
	for _, num := range nums {
		if counter == n {
			break
		}
		if num < limit {
			ans_arr = append(ans_arr, num)
			counter++
		}
	}

	return ans_arr, nil
}

func main() {
	fmt.Println(UnderLimit([]int{3, -5, 6}, 10, 3))
} 