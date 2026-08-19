package main

import "fmt"
type ledger struct{
	balance int
	status string
}
func Account_Ledger_Analyser(transactions []int) (ledger_instance ledger) {
	for _, i := range transactions {
		ledger_instance.balance += i
	}
	if ledger_instance.balance < 0 {
		ledger_instance.status = "DEBT"
	}
	if ledger_instance.balance == 0 {
		ledger_instance.status = "BALANCED"
	}
	if ledger_instance.balance > 0 {
		ledger_instance.status = "PROFIT"
	}
	return ledger_instance
}

func main(){
	value := Account_Ledger_Analyser([]int{10, 15, 20, -100})
	slice := []string{fmt.Sprintf("%d", value.balance), value.status}
	fmt.Println(slice)
}
