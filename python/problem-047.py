### Problem 47 - Distinct Primes Factors
###------------------------------------------------------------------------------------------------------------------------
### The first two consecutive numbers to have two distinct prime factors are:
### 14 = 2 × 7
### 15 = 3 × 5
### The first three consecutive numbers to have three distinct prime factors are:
### 644 = 2² × 7 × 23
### 645 = 3 × 5 × 43
### 646 = 2 × 17 × 19.
### Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

### Solution

from typing import List, Set

# Function to determine if prime
def isPrime(n: int) -> bool:
	if n < 2:
		return False
	elif n == 2:
		return True
	else:
		i = 2
		while i**2 <= n:
			if n % i == 0:
				return False
			i += 1
		return True

# Function to do prime factorization
def primeFactorization(n: int, primes: List[int]) -> Set[int]:
	i = 0
	pf = set()
	while True:
		if i == len(primes):
			break
		if n == 1:
			break
		if n in primes:
			pf.add(n)
			break
		if n % primes[i] == 0:
			pf.add(primes[i])
			n /= primes[i]
		else:
			i += 1
	return pf

# Create list of primes
primes = [i for i in range(1001) if isPrime(i)]

# Iterate through starting numbers and final numbers (trial and error for this)
num = 100000
first_num = 0
while True:
	if num > 200000:
		break
	if len(primeFactorization(num, primes)) == 4:
		if len(primeFactorization(num + 1, primes)) == 4:
			if len(primeFactorization(num + 2, primes)) == 4:
				if len(primeFactorization(num + 3, primes)) == 4:
					first_num = num
					break
	num += 1

print('The first number in the four consecutive numbers is: ' + str(first_num))

