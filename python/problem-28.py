### Problem 28 - Number Spiral Diagonals
###--------------------------------------------------------------------------------------------------------------
### Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
###    21 22 23 24 25
###    20  7  8  9 10
###    19  6  1  2 11
###    18  5  4  3 12
###    17 16 15 14 13
### It can be verified that the sum of the numbers on the diagonals is 101.
### What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

### Solution

# Separation between numbers is 2*n in the nth layer
currNum = 1
totalSum = 1
layer = 1

while True:
	separation = 2*layer
	for i in range(1, 5):
		currNum += separation
		totalSum += currNum
	layer += 1

	if currNum >= 1001**2:
		break

print('Sum of diagonals for 1001 x 1001 spiral: ' + str(totalSum))