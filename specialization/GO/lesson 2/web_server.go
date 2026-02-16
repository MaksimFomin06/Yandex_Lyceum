package main

import (
	"fmt"
	"net/http"
)

func getRequest(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello, World!")
}

func main() {
	http.HandleFunc("/", getRequest)

	port:= ":8080"

	http.ListenAndServe(port, nil)
}