### Problem 41 - Pandigital Prime
###---------------------------------------------------------------------------------------------------------
### We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. 
### For example, 2143 is a 4-digit pandigital and is also prime.
### What is the largest n-digit pandigital prime that exists?

### Solution

from itertools import permutations

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

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
largest_num = 0

for a in range(1, len(digits)):
	currDigits = digits[0:a]
	numbers = list(permutations(currDigits))
	nums = []

	for i in numbers:
		currNum = 0
		for j in range(len(i)):
			currNum += (10**(len(i) - (j + 1)))*i[j]
		nums.append(currNum)

	for i in nums:
		if isPrime(i):
			if i > largest_num:
				largest_num = i

print('The largest pandigital prime is: ' + str(largest_num))