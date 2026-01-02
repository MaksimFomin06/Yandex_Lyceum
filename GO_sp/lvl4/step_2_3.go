package main

import "fmt"

type LogLevel string

const (
    Error LogLevel = "Error"
    Info  LogLevel = "Info"
)

type Logger interface {
    Log(message string)
}

type Log struct {
    Level LogLevel
}

func (l Log) Log(message string) {
    switch l.Level {
    case Error:
        fmt.Printf("ERROR: %s\n", message)
    case Info:
        fmt.Printf("INFO: %s\n", message)
    default:
        fmt.Printf("%s: %s\n", l.Level, message)
    }
}

func main() {
	errorLog := &Log{Level: Error}
	errorLog.Log("This is an error message")
}