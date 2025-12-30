package main

import (
	"time"
	"errors"
	"strings"
	"unicode/utf8"
)

var TimeNow = func() time.Time {
	return time.Now()
}

var GoSleep = errors.New("исправь свой ответ, а лучше ложись поспать")

var rusWeekdays = map[time.Weekday]string{
	time.Sunday:    "Воскресенье",
	time.Monday:    "Понедельник",
	time.Tuesday:   "Вторник",
	time.Wednesday: "Среда",
	time.Thursday:  "Четверг",
	time.Friday:    "Пятница",
	time.Saturday:  "Суббота",
}

func currentDayOfTheWeek() string {
	return rusWeekdays[TimeNow().Weekday()]
}

func dayOrNight() string {
	hour := TimeNow().Hour()
	if hour >= 10 && hour <= 22 {
		return "День"
	}
	return "Ночь"
}

func nextFriday() int {
	now := TimeNow()
	return (5 - int(now.Weekday()) + 7) % 7
}

func CheckCurrentDayOfTheWeek(answer string) bool {
	expected := rusWeekdays[TimeNow().Weekday()]
	return strings.EqualFold(expected, answer)
}

func CheckNowDayOrNight(answer string) (bool, error) {
	if utf8.RuneCountInString(answer) != 4 {
		return false, GoSleep
	}
	expected := dayOrNight()
	return strings.EqualFold(expected, answer), nil
}
