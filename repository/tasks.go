package repository

import (
	"awesomeProject2/models"
	"encoding/json"
	"net/http"
)

type DefaultResponse struct {
	Message string `json:"message"`
}

var (
	tasks = []models.Task{
		{Title: "Complete Project Report", Description: "Prepare and finalize the project report for the annual review. Include data analysis, project milestones, and future recommendations.", Status: "новая"},
		{Title: "Fix Bug in Authentication Module", Description: "Resolve the issue in the authentication module that causes login failures for users with special characters in their passwords. Ensure compatibility with existing user data.", Status: "новая"},
		{Title: "Design New User Interface", Description: "Design a new user interface for the upcoming app release. Focus on improving usability and visual appeal, and incorporate feedback from the user experience testing.", Status: "новая"},
	}
)

func setHeaders(w http.ResponseWriter) {
	w.Header().Set("Content-Type", "application/json")
	w.Header().Set("Access-Control-Allow-Origin", "*")
	w.Header().Set("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
	w.Header().Set("Access-Control-Allow-Headers", "Content-Type")
}

func GetTasks(w http.ResponseWriter, r *http.Request) {
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

func AddTask(w http.ResponseWriter, r *http.Request) {
	setHeaders(w)
	if r.Method == http.MethodOptions {
		w.WriteHeader(http.StatusOK)
		return
	}

	if r.Method == http.MethodPost {
		var t models.Task

		err := json.NewDecoder(r.Body).Decode(&t)
		if err != nil {
			http.Error(w, err.Error(), http.StatusBadRequest)
			return
		}

		// Проверка на пустые поля
		if t.Description == "" || t.Title == "" {
			http.Error(w, "Invalid task content", http.StatusBadRequest)
			return // Завершаем выполнение функции, чтобы задача не добавлялась
		}

		tasks = append(tasks, t)
		var response DefaultResponse
		response.Message = "Successfully Added Operation"

		err = json.NewEncoder(w).Encode(response)
		if err != nil {
			http.Error(w, "Error encoding response", http.StatusInternalServerError)
			return // Завершаем выполнение функции при ошибке кодирования
		}
	} else {
		http.Error(w, "Invalid request method", http.StatusMethodNotAllowed)
	}
}

func TasksHandler(w http.ResponseWriter, r *http.Request) {
	switch r.Method {
	case http.MethodGet:
		GetTasks(w, r)
	case http.MethodPost:
		AddTask(w, r)
	default:
		http.Error(w, "Invalid request method", http.StatusMethodNotAllowed)
	}
}
