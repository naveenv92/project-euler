### Problem 14
###--------------------------------------------------------------------------------------------------------------------------
### The following iterative sequence is defined for the set of positive integers:
### n → n/2 (n is even)
### n → 3n + 1 (n is odd)
### Using the rule above and starting with 13, we generate the following sequence: 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
### It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
### Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
### Which starting number, under one million, produces the longest chain?

### Solution

import numpy as np

# Function to calculate Collatz sequence
def collatz(n):
	currentNumber = n
	length = 0

	while currentNumber != 1:
		if currentNumber % 2 == 0:
			currentNumber = currentNumber/2
		else:
			currentNumber = 3*currentNumber + 1
		length += 1

	# Add extra term because loop breaks when the number is 1
	length += 1
	return length

longestChain = 0
startingNumber = 0
for i in range(1, 1000000):
	currentLength = collatz(i)
	if currentLength > longestChain:
		longestChain = currentLength
		startingNumber = i

print('Longest chain: ' + str(longestChain) + ' for starting number of ' + str(startingNumber))