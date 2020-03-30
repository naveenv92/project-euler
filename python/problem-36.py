### Problem 36 - Double-Base Palindromes
###-------------------------------------------------------------------------------------------------
### The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
### Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
### (Please note that the palindromic number, in either base, may not include leading zeros.)

### Solution

# Function to convert to binary. n:int -> string
def convertToBinary(n):
	binary = []

	if n == 0:
		return [0]

	while n != 0:
		binary.append(n % 2)
		n //= 2
	
	binary = ''.join([str(i) for i in binary])
	return binary[::-1]

# Function to determine if palindrome. n:string -> boolean
def isPalindrome(n):
	if n == n[::-1]:
		return True
	else:
		return False

# Find sum of palindromes in base 2 and 10 below 1000000
sumOfPalindromes = 0
for i in range(1, 1000000):
	if isPalindrome(str(i)) and isPalindrome(convertToBinary(i)):
		sumOfPalindromes += i

print('The sum of palindromes in base 2 and 10 below 1,000,000 is: ' + str(sumOfPalindromes))