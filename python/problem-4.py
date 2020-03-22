### Problem 4
###--------------------------------------------------------------------------------------------------------------------------------------
### A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
### Find the largest palindrome made from the product of two 3-digit numbers.

### Solution

# Function to determine palindrome
def isPalindrome(n):
	
	if str(n) == str(n)[::-1]:
		return True
	
	return False

# Calculate largest palindrome
largestPalindrome = 0

for i in range(100, 1000):
	for j in range(100, 1000):
		product = i*j
		if isPalindrome(product) and product > largestPalindrome:
			largestPalindrome = product

print(largestPalindrome)