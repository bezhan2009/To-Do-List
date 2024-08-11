package models

import "gorm.io/gorm"

type Status string
type Priority string

const (
	StatusNew        Status = "новая"
	StatusIncomplete Status = "не выполненная"
	StatusComplete   Status = "выполненная"
)

const (
	PriorityLow    Priority = "Низкая"
	PriorityMedium Priority = "Средний"
	PriorityHigh   Priority = "Высокая"
)

type Task struct {
	gorm.Model
	ID          uint     `gorm:"primaryKey" json:"id"`
	Title       string   `gorm:"type:varchar(100)" json:"title"`
	Description string   `gorm:"type:text" json:"description"`
	Status      Status   `gorm:"type:varchar(100);not null;default:'новая'" json:"status"`
	Priority    Priority `gorm:"type:varchar(100)" json:"priority"`
}
