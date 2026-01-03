package main

import (
	"fmt"
	"strings"
)

type Writer interface {
	Write(p []byte) int
}

type Reader interface {
	Read() []byte
}

type ReaderWriter interface {
	Writer
	Reader
}

type UpperReaderWriter struct {
	UpperString string
}

func (urw *UpperReaderWriter) Write(p []byte) int {
	urw.UpperString = strings.ToUpper(string(p))
	return len(p)
}

func (urw *UpperReaderWriter) Read() []byte {
	return []byte(urw.UpperString)
}

func main() {
	urw := &UpperReaderWriter{}

	testData := []byte("hello, world!")
	bytesWritten := urw.Write(testData)
	fmt.Printf("Записано %d байт: %s\n", bytesWritten, testData)

	readData := urw.Read()
	fmt.Printf("Прочитано: %s\n", readData)

	if urw.UpperString != strings.ToUpper(string(testData)) {
		fmt.Println("Ошибка: строка не преобразована в верхний регистр")
	}

	var _ Reader = urw
	var _ Writer = urw
	var _ ReaderWriter = urw
}