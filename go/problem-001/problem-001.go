package main

import (
	"fmt"
)

func main() {
	var sumValues int

	for i := 0; i < 1000; i++ {
		if i % 3 == 0 || i % 5 == 0 {
			sumValues += i
		}
	}

	fmt.Printf("The sum is %d\n", sumValues)
}
