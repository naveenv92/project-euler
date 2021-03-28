package main

import (
	"fmt"
	"math"
)

func isPrime(n int) bool {
	if n < 2 {
		return false
	} else if n == 2 {
		return true
	} else {
		for i := 2; i*i <= n; i++ {
			if n%i == 0 {
				return false
			}
		}
	}
	return true
}

func main() {
	startValue := int(math.Floor(math.Sqrt(600851475143)))
	largestFactor := 0

	for startValue > 0 {
		if 600851475143%startValue == 0 && isPrime(startValue) {
			largestFactor = int(startValue)
			break
		}
		startValue -= 1
	}

	fmt.Printf("Largest prime factor of 600851475143 is %d\n", largestFactor)
}
