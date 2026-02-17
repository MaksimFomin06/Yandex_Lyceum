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

func ipBlockerMiddleware(blockedIP string, next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		clientIP := r.Header.Get("X-Real-IP")
		if clientIP == "" {
			clientIP = r.RemoteAddr
		}
		if clientIP == blockedIP {
			http.Error(w, "403 Forbidden", http.StatusForbidden)
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

func startServer(address string) {
	mux := http.NewServeMux()
	mux.HandleFunc("/", mainHandler)

	handler := ipBlockerMiddleware("192.168.0.1", mux)
	handler = loggingMiddleware(handler)

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