### Problem 7 - 10001st Prime
###-----------------------------------------------------------------------------------------------------
### By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
### What is the 10,001st prime number?

### Solution

import numpy as np

# Function to determine if number is prime
def isPrime(n):
	
	if n == 2:
		return True

	for i in range(2, int(np.sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True

# Find 10,001st prime number
number = 2
counter = 0

while True:
	if isPrime(number):
		counter += 1
	if counter == 10001:
		break
	number += 1

print(number)