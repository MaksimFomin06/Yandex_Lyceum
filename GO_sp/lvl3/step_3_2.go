package main

func Join(nums1, nums2 []int) []int {
	emkost := len(nums1) + len(nums2)
	join_arr := make([]int, emkost)

	copy(join_arr, nums1)
	copy(join_arr[len(nums1):], nums2)

	return join_arr
}