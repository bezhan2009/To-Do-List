package db

import (
	"awesomeProject2/models"
	"errors"
	"log"
)

func Migrate() error {
	errConn := ConnectToDB()
	if errConn != nil {
		panic(errConn)
	}
	if dbConn == nil {
		return errors.New("database connection is not initialized")
	}

	err := dbConn.AutoMigrate(&models.Task{})
	if err != nil {
		return errors.New("failed to migrate database schema: " + err.Error())
	}

	log.Println("Database migration completed successfully")
	return nil
}
