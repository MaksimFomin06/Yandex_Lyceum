package main

import (
	"fmt"
)

func PrintComplexNumber(z complex64) {
	d_ch := real(z)
	m_ch := imag(z)

	ans := fmt.Sprintf("Действительная часть: %.2f. Мнимая часть: %.2f", d_ch, m_ch)
	fmt.Println(ans)
}

func main() {
	PrintComplexNumber(complex(10, 15))
}