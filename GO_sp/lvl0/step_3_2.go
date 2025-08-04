package main

import "fmt"

func main() {
	var text string

	fmt.Scanln(&text)

	result := fmt.Sprintf("А ещё я люблю %s!", text)

	fmt.Println(result)
}
