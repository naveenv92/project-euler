### Problem 20
###--------------------------------------------------------------------------------------------------------------------------------------
### n! means n × (n − 1) × ... × 3 × 2 × 1
### For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800, and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
### Find the sum of the digits in the number 100!

### Solution

# Function for factorial
def factorial(n):
	factorial = 1
	if n == 0:
		return 1
	else:
		for i in range(1, n+1):
			factorial *= i

	return factorial

largeNum = factorial(100)
digitSum = 0

for i in str(largeNum):
	digitSum += int(i)

print('Sum of digits in 100!: ' + str(digitSum))