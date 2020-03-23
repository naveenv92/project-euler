### Problem 23
###-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
###For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
### A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
### As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. 
### By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
### However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
### Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

### Solution

import numpy as np

# Function to determine the sum of divisors
def sumOfDivisors(n):
	divisors = [1]
	for i in range(2, int(np.sqrt(n)) + 1):
		if n % i == 0:
			divisors.append(i)
			if not i**2 == n:
				divisors.append(n/i)
	return sum(divisors)

abundantNumbers = []

for i in range(2, 28124):
	if sumOfDivisors(i) > i:
		abundantNumbers.append(i)

nonAbundantSums = np.arange(1, 28124, 1)

for i in abundantNumbers:
	for j in abundantNumbers:
		if i + j <= 28123:
			nonAbundantSums[i+j-1] = 0

print("The sum of positive integers that cannot be written as the sum of two abundant numbers: " + str(sum(nonAbundantSums)))