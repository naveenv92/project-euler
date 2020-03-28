### Problem 34 - Digit Factorials
###-----------------------------------------------------------------------------------------
### 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
### Find the sum of all numbers which are equal to the sum of the factorial of their digits.
### Note: as 1! = 1 and 2! = 2 are not sums they are not included.

### Solution

# 7*9! = 2540160 which is less than 9999999 so we will set this as the upper limit

factorials = {'0': 1, '1': 1, '2': 2, '3': 6, '4': 24, '5': 120, '6': 720, '7': 5040, '8': 40320, '9': 362880}
total_sum = 0

for i in range(3, 2540161):
	factorial_sum = 0
	for j in str(i):
		factorial_sum += factorials[j]
	if i == factorial_sum:
		total_sum += i

print('Total digit factorial sum: ' + str(total_sum))