### Problem 52 - Permuted Multiples
###---------------------------------------------------------------------------------------------------------------------------
### It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
### Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

### Solution

# Function to determine if digits are the same
def sameDigits(n: int, m: int) -> bool:
	
	if len(str(n)) != len(str(m)):
		return False

	digits = set()
	
	for i in str(n):
		digits.add(int(i))

	for i in str(m):
		if int(i) in digits:
			digits.remove(int(i))

	return len(digits) == 0

n = 1
while True:
	if sameDigits(n, 2*n):
		if sameDigits(n, 3*n):
			if sameDigits(n, 4*n):
				if sameDigits(n, 5*n):
					if sameDigits(n, 6*n):
						break
	n += 1

print('The smallest integer x is: ' + str(n))
