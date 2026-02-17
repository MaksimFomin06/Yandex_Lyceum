package main

import (
	"fmt"
	"net/http"
	"io"
)

func loggingMiddleware(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		next.ServeHTTP(w, r)
	})
}

func authMiddleware(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		if _, err := r.Cookie("user_id"); err != nil {
			http.Redirect(w, r, "/login", http.StatusFound)
			return
		}
		next.ServeHTTP(w, r)
	})
}

func mainHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodGet {
		return
	}
	w.Write([]byte("Access granted"))
}

func loginHandler(w http.ResponseWriter, r *http.Request) {
	http.SetCookie(w, &http.Cookie{
		Name:  "user_id",
		Value: "123",
		Path:  "/",
	})
	w.Write([]byte("Please log in"))
}

func startServer(address string) {
	mux := http.NewServeMux()
	mux.HandleFunc("/login", loginHandler)

	protected := authMiddleware(http.HandlerFunc(mainHandler))
	mux.Handle("/", protected)

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