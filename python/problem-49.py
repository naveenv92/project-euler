### Problem 49 - Prime Permutations
###------------------------------------------------------------------------------------------------------------------------------------------------------------
### The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: 
### (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
### There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.
### What 12-digit number do you form by concatenating the three terms in this sequence?

### Solution

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

# Function to determine if permutation
def isPerm(a: int, b: int) -> bool:
	digits = list()
	for i in str(a):
		digits.append(i)
	for j in str(b):
		if j in digits:
			digits.remove(j)
	return len(digits) == 0

# Generate list of 4-digit primes
primes = []
n = 1000
while True:
	if n > 9999:
		break
	if isPrime(n):
		primes.append(n)
	n += 1

# Generate list of permutations of 4-digit primes
perms = []
for i in range(len(primes)):
	currPerms = [primes[i]]
	for j in range(i, len(primes)):
		if primes[i] == primes[j]:
			continue
		elif isPerm(primes[i], primes[j]):
			currPerms.append(primes[j])
	if len(currPerms) > 2:
		perms.append(currPerms)

# Determine if there is a constant difference in sequence
sequences = []
for i in perms:
	diff = i[1] - i[0]
	const = True
	for j in range(1, len(i) - 1):
		if i[j+1] - i[j] != diff:
			const = False
			break
	if const == True:
		sequences.append(i)

finalNum = ''
for i in sequences:
	finalNum += str(i)

print('The 12-digit number from concatenating the number sequence is: ' + finalNum)
