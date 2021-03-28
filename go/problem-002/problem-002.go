package main

import "fmt"

func main() {
	curr := 1
	prev := 1
	sumValues := 0

	for curr <= 4000000 {
		if curr%2 == 0 {
			sumValues += curr
		}
		curr += prev
		prev = curr - prev
	}

	fmt.Printf("The sum of fibonacci numbers below 4,000,000 is %d\n", sumValues)
}
