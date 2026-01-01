package main

import "fmt"

func SwapKeysAndValues(m map[string]string) map[string]string {
	new_map := make(map[string]string)
	for key, value := range m {
		new_map[value] = key
	}

	return new_map
}

func main() {
	m := map[string]string{
		"Яндекс":        "+74957397000",
		"Музей Яндекса": "+74991101133",
	}
	fmt.Println(SwapKeysAndValues(m))
}