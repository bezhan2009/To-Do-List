package main

import (
	"encoding/json"
	"html/template"
	"log"
	"net/http"
	"path/filepath"
)

type Task struct {
	Title   string `json:"title"`
	Content string `json:"content"`
}

type DefaultResponse struct {
	Message string `json:"message"`
}

var (
	tasks = []Task{
		{Title: "Complete Project Report", Content: "Prepare and finalize the project report for the annual review. Include data analysis, project milestones, and future recommendations."},
		{Title: "Fix Bug in Authentication Module", Content: "Resolve the issue in the authentication module that causes login failures for users with special characters in their passwords. Ensure compatibility with existing user data."},
		{Title: "Design New User Interface", Content: "Design a new user interface for the upcoming app release. Focus on improving usability and visual appeal, and incorporate feedback from the user experience testing."},
	}
)

func setHeaders(w http.ResponseWriter) {
	w.Header().Set("Content-Type", "application/json")
	w.Header().Set("Access-Control-Allow-Origin", "*")
	w.Header().Set("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
	w.Header().Set("Access-Control-Allow-Headers", "Content-Type")
}

func tasksHandler(w http.ResponseWriter, r *http.Request) {
	setHeaders(w)
	if r.Method == http.MethodOptions {
		w.WriteHeader(http.StatusOK)
		return
	}

	if r.Method == http.MethodGet {
		jsonTasks, err := json.Marshal(&tasks)
		if err != nil {
			http.Error(w, "Error marshaling tasks", http.StatusInternalServerError)
			return
		}
		w.Write(jsonTasks)
	} else {
		http.Error(w, "Invalid request method", http.StatusMethodNotAllowed)
	}
}

func addTask(w http.ResponseWriter, r *http.Request) {
	setHeaders(w)
	if r.Method == http.MethodOptions {
		w.WriteHeader(http.StatusOK)
		return
	}

	if r.Method == http.MethodPost {
		var t Task

		err := json.NewDecoder(r.Body).Decode(&t)
		if err != nil {
			http.Error(w, err.Error(), http.StatusBadRequest)
			return
		}

		tasks = append(tasks, t)
		var response DefaultResponse
		response.Message = "Successfully Added Operation"

		err = json.NewEncoder(w).Encode(response)
		if err != nil {
			http.Error(w, "Error encoding response", http.StatusInternalServerError)
		}
	} else {
		http.Error(w, "Invalid request method", http.StatusMethodNotAllowed)
	}
}

func indexHandler(w http.ResponseWriter, r *http.Request) {
	tmplPath := filepath.Join("template", "index.html")
	tmpl, err := template.ParseFiles(tmplPath)
	if err != nil {
		http.Error(w, "Error parsing template", http.StatusInternalServerError)
		return
	}
	tmpl.Execute(w, nil)
}

func documentationHandler(w http.ResponseWriter, r *http.Request) {
	tmplPath := filepath.Join("template", "documentation.html")
	tmpl, err := template.ParseFiles(tmplPath)
	if err != nil {
		http.Error(w, "Error parsing template", http.StatusInternalServerError)
		return
	}
	tmpl.Execute(w, nil)
}

func main() {
	// Обработка статических файлов
	fs := http.FileServer(http.Dir("static"))
	http.Handle("/static/", http.StripPrefix("/static/", fs))

	http.HandleFunc("/tasks", tasksHandler)
	http.HandleFunc("/tasks/create", addTask)
	http.HandleFunc("/", indexHandler)
	http.HandleFunc("/documentation", documentationHandler)

	log.Println("Server started on http://localhost:8080")
	log.Fatal(http.ListenAndServe(":8080", nil))
}
