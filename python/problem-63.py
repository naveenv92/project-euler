### Problem 63 - Powerful Digit Counts
###----------------------------------------------------------------------------------------------------------------------
### The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is a ninth power.
### How many n-digit positive integers exist which are also an nth power?

### Solution

numbers = []
number = 1

while True:
	if number > 11:
		break
	exp = 1
	while True:
		power = pow(number, exp)
		if len(str(power)) == exp:
			numbers.append(power)
		else:
			break
		exp += 1
	number += 1

print('The number of n-digit positive numbers that are an nth power is: ' + str(len(numbers)))