package main

import (
	"awesomeProject2/db"
	"awesomeProject2/utils"
	"log"
	"net/http"
)

func main() {
	errMigration := db.Migrate()
	if errMigration != nil {
		panic(errMigration)
	}

	utils.InitEndPoints()
	log.Println("Server started on http://localhost:8080")
	log.Fatal(http.ListenAndServe(":8080", nil))
}
