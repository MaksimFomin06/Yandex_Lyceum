package main

import (
	"fmt"
	"time"
	"math"
)

func main() {
	var startWork, name, surname, patronymic string
	var num1, num2, num3 float64

	fmt.Scanln(&startWork)
	fmt.Scanln(&name)
	fmt.Scanln(&surname)
	fmt.Scanln(&patronymic)
	fmt.Scanln(&num1)
	fmt.Scanln(&num2)
	fmt.Scanln(&num3)

	startAgreementTime, err := time.Parse("02.01.2006", startWork)
	if err != nil {
		return
	}

	startAgreement := startAgreementTime.AddDate(0, 0, 15)
	summa := num1 + num2 + num3
	summaInKop := math.Round(summa * 100)
	summaRub := int(summaInKop) / 100
	kop := int(summaInKop) % 100

	answer := fmt.Sprintf("Уважаемый, %s %s %s, доводим до вашего сведения, что бухгалтерия сформировала документы по факту выполненной вами работы.\nДата подписания договора: %s. Просим вас подойти в офис в любое удобное для вас время в этот день.\nОбщая сумма выплат составит %d руб. %01d коп.\n\nС уважением,\nГл. бух. Иванов А.Е.", surname, name, patronymic, startAgreement.Format("02.01.2006"), summaRub, kop)
	fmt.Println(answer)
}