package main

import (
	"fmt"
	"html/template"
	"log"
	"math/rand"
	"net/http"
	"strconv"
)

var tmpl = template.Must(template.ParseFiles("index.html"))
var num = rand.Intn(100) + 1

type Values struct {
	RandomNum int
	GuessNum  int
	Response  string
}

func homeHandler(w http.ResponseWriter, r *http.Request) {
	if r.URL.Path != "/" {
		http.Error(w, "Not Found", http.StatusNotFound)
		return
	}
	err := tmpl.Execute(w, nil)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
}
func guessHandler(w http.ResponseWriter, r *http.Request) {
	guess := r.FormValue("guessnum")
	guessNum, err := strconv.Atoi(guess)
	if err != nil {
		fmt.Fprintln(w, "Input is not a valid number.")
		return
	}
	data := Values{
		RandomNum: num,
		GuessNum:  guessNum,
	}
	var resp string
	switch {
	case data.GuessNum < data.RandomNum:
		resp = "Too Low"

	case data.GuessNum > data.RandomNum:
		resp = "Too High"

	case data.GuessNum == data.RandomNum:
		resp = "Correct! You got me."
		num = rand.Intn(100) + 1
		data.RandomNum = num
	}
	data.Response = resp
	err = tmpl.Execute(w, data)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

}

func main() {
	http.Handle("/static/", http.StripPrefix("/static", http.FileServer(http.Dir("static"))))
	http.HandleFunc("/", homeHandler)
	http.HandleFunc("/guess", guessHandler)
	log.Println("server started")
	log.Fatal(http.ListenAndServe(":8080", nil))
}
