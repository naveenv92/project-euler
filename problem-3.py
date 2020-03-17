### Problem 3
###-------------------------------------------------------------
### The prime factors of 13195 are 5, 7, 13 and 29.
### What is the largest prime factor of the number 600851475143?

### Solution

import numpy as np

# Function to determine if number is prime
def isPrime(n):
	
	if n == 2:
		return True

	for i in range(2, int(np.sqrt(n))):
		if n % i == 0:
			return False

	return True


largest_factor = 1
number = 600851475143

for i in range(2, int(np.sqrt(number))):
	if number % i == 0:
		if isPrime(i):
			largest_factor = i

print(largest_factor)