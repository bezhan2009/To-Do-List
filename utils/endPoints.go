package utils

import (
	"awesomeProject2/controllers"
	"awesomeProject2/repository"
	"net/http"
)

func InitEndPoints() {
	fs := http.FileServer(http.Dir("static"))
	http.Handle("/static/", http.StripPrefix("/static/", fs))

	http.HandleFunc("/tasks", repository.TasksHandler)
	http.HandleFunc("/", controllers.IndexHandler)
	http.HandleFunc("/documentation", controllers.DocumentationHandler)
}
