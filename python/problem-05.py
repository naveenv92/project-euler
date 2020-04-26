"""
Problem 5 - Smallest Multiple

2520 is the smallest number that can be divided by each of the numbers 
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of 
the numbers from 1 to 20?
"""

# Check if evenly divisible
def isDivisible(n):
	for i in range(1, 21):
		if n % i != 0:
			return False

	return True

# Calculate smallest divisible integer
number = 20

while True:
	if isDivisible(number):
		break
	else:
		number += 20

print('The smallest number divisible by 1-20 is: ' + str(number))