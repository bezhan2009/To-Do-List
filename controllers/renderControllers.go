package controllers

import (
	"html/template"
	"net/http"
	"path/filepath"
)

func IndexHandler(w http.ResponseWriter, r *http.Request) {
	tmplPath := filepath.Join("template", "index.html")
	tmpl, err := template.ParseFiles(tmplPath)
	if err != nil {
		http.Error(w, "Error parsing template", http.StatusInternalServerError)
		return
	}
	tmpl.Execute(w, nil)
}

func DocumentationHandler(w http.ResponseWriter, r *http.Request) {
	tmplPath := filepath.Join("template", "documentation.html")
	tmpl, err := template.ParseFiles(tmplPath)
	if err != nil {
		http.Error(w, "Error parsing template", http.StatusInternalServerError)
		return
	}
	tmpl.Execute(w, nil)
}
