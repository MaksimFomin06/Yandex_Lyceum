package main

import (
	"fmt"
	"net/http"
	"io"
)

func startServer(address string) {
	http.HandleFunc("/", getRequest)
	http.ListenAndServe(address, nil)
}

func sendRequest(url string) (string, error) {
	url = fmt.Sprintf("http://%s", url)
	resp, err := http.Get(url)
	if err != nil {
		return "", err
	}

	defer resp.Body.Close()

	body, err := io.ReadAll(resp.Body)
	if err != nil {
		return "", err
	}

	return string(body), nil
}

func getRequest(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello from server")
}
