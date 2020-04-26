"""
Problem 4 - Largest Palindrome Product

A palindromic number reads the same both ways. The largest palindrome 
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrome(n: int) -> bool:
	"""
	Parameters
		n (int): number to test if palindrome
	Returns
		boolean
	"""

	if str(n) == str(n)[::-1]:
		return True
	return False

def largest_palindrome(low: int, high: int) -> int:
	"""
	Parameters
		low (int): low integer of range
		high (int): high integer of range
	Returns
		largest_palindrome (int): largest palindrome product of 
								  values in [low, high]
	"""

	largest_palindrome = 0

	for i in range(low, high):
		for j in range(low, high):
			if is_palindrome(i*j) and (i*j) > largest_palindrome:
				largest_palindrome = i*j
	return largest_palindrome

if __name__ == '__main__':
	print('The largest palindrome product of three-digit numbers is: ' 
	  	  + str(largest_palindrome(100, 1000)))