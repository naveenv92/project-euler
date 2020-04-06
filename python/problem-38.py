### Problem 38 - Pandigital Multiples
###---------------------------------------------------------------------------------------------------------------------------------------------------
### Take the number 192 and multiply it by each of 1, 2, and 3:
### 192 × 1 = 192
### 192 × 2 = 384
### 192 × 3 = 576
### By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
### The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, 
### which is the concatenated product of 9 and (1,2,3,4,5).
### What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

### Solution

# Function to determine if pandigital
def isPandigital(n: int) -> bool:
	digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	digit_set = set()

	for i in range(len(str(n))):
		digit_set.add(digits[i])

	for i in str(n):
		if int(i) in digit_set:
			digit_set.remove(int(i))

	return len(digit_set) == 0

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pan_nums = []

for i in range(2, len(digits) + 1):
	num = 2
	curr_digits = digits[0:i]
	while True:
		concat_number = ''
		for j in curr_digits:
			concat_number += str(num*j)
		if len(concat_number) > 9:
			break
		elif isPandigital(int(concat_number)):
			pan_nums.append(int(concat_number))
		num += 1

print('The largest pandigital 1 to 9 number is: ' + str(max(pan_nums)))


