### Problem 10 - Summation of Primes
###------------------------------------------------------
### The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
### Find the sum of all the primes below two million.

### Solution

import numpy as np

# Function to determine prime
def isPrime(n):
	if n == 1:
		return False
	if n == 2:
		return True
	for i in range(2, int(np.sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True

sumOfPrimes = 0

for i in range(2000000):
	if isPrime(i):
		sumOfPrimes += i

print(sumOfPrimes)