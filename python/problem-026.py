### Problem 26 - Reciprocal Cycles
###-----------------------------------------------------------------------------------------------------------------------------------
### A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
### 1/2	= 0.5
### 1/3 = 0.(3)
### 1/4	= 0.25
### 1/5	= 0.2
### 1/6	= 0.1(6)
### 1/7	= 0.(142857)
### 1/8	= 0.125
### 1/9	= 0.(1)
### 1/10 = 0.1
### Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
### Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

### Solution

# Define function to determine repeating cycle length
def isRepeating(d):
	rem = []
	dividend = 1
	while True:
		
		while dividend < d:
			dividend *= 10
		
		dividend %= d
		if dividend == 0:
			return 0
		elif dividend not in rem:
			rem.append(dividend)
		else:
			start = rem.index(dividend)
			cycle_length = len(rem) - start
			break

	return cycle_length

max_d, max_cycle_length = 0, 0

for i in range(1, 1000):
	if isRepeating(i) > max_cycle_length:
		max_d, max_cycle_length = i, isRepeating(i)

print('The value with the longest recurring cycle is ' + str(max_d) + ' with a length of ' + str(max_cycle_length))
