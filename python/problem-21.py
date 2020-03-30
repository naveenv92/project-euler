### Problem 21 - Amicable Numbers
###--------------------------------------------------------------------------------------------------------------------------
### Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
### If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
### For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
### The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
### Evaluate the sum of all the amicable numbers under 10000.

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

amicableSum = 0
for i in range(2, 10000):
	divisorSum = sumOfDivisors(i)
	if sumOfDivisors(divisorSum) == i and divisorSum != i:
		amicableSum += i

print("Sum of amicable numbers under 10000: " + str(amicableSum))