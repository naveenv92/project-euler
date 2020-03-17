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