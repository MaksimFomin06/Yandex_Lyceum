package main

func SliceCopy(nums []int) []int {
	new_arr := make([]int, len(nums))
	copy(new_arr, nums)

	return new_arr
}