package main

type User struct {
	ID int
	Name string
	Email string
	Age int
}

type Report struct {
	User
	ReportID int
	Date string
}

func CreateReport(user User, reportDate string) Report {
	reportId := user.ID
	return Report{User: user, ReportID: reportId, Date: reportDate}
}

func GenerateUserReports(users []User, reportDate string) []Report {
	reports := make([]Report, 0, len(users))

	for _, user := range users {
		report := CreateReport(user, reportDate)
		reports = append(reports, report)
	}
	
	return reports
}