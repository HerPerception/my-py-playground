package main

import "fmt"
func Report_For_Duty(name string) string {
	return fmt.Sprintf("Recruit %s reporting for duty", name)
}

func main(){
	fmt.Println(Report_For_Duty("Dee"))
}