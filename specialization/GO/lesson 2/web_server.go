package main

import (
	"fmt"
	"net/http"
	"io"
	"log"
)

func loggingMiddleware(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		// log.Printf("Метод: %s, URL: %s", r.Method, r.URL.Path)
		next.ServeHTTP(w, r)
	})
}

func mainHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodGet {
		return
	}

	if _, err := r.Cookie("session_id"); err != nil {
		http.SetCookie(w, &http.Cookie{
			Name:  "session_id",
			Value: "abc123",
			Path:  "/",
		})
		w.Write([]byte("Welcome!"))
		return
	}

	w.Write([]byte("Welcome back!"))
}

func startServer(address string) {
	mux := http.NewServeMux()
	mux.HandleFunc("/", mainHandler)

	handler := loggingMiddleware(mux)

	http.ListenAndServe(address, handler)
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

func main() {
	startServer(":8080")
}