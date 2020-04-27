"""
Problem 14 - Longest Collatz Sequence

The following iterative sequence is defined for the set of positive integers:
n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence: 
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 
10 terms. 

Although it has not been proved yet (Collatz Problem), it is thought that all 
starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
"""

from typing import Tuple

def collatz(n: int) -> int:
	"""
	Parameters
		n (int): starting number of sequence
	Returns
		length (int): length of sequence
	"""

	curr_n = n
	length = 0

	while curr_n != 1:
		if curr_n % 2 == 0:
			curr_n /= 2
		else:
			curr_n = 3*curr_n + 1
		length += 1
	length += 1 # Add 1 since look breaks at 1
	return length

def longest_chain(n: int) -> Tuple[int, int]:
	"""
	Parameters:
		n (int): top bound on values to search sequence
	Returns:
		longest_chain: length of longest chain below n
	"""

	longest = 0
	starting_n = 0

	for i in range(1, n):
		curr_length = collatz(i)
		if curr_length > longest:
			longest = curr_length
			starting_n = i
	return longest, starting_n

if __name__ == '__main__':
	longest, starting_n = longest_chain(1000000)
	print('Longest chain: ' + str(longest) + ' for starting number of ' +
		  str(starting_n))
