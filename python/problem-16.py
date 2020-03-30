### Problem 16 - Power Digit Sum
###-----------------------------------------------------------------
### 2^(15) = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
### What is the sum of the digits of the number 2^(1000)?

### Solution

num = 2**1000
digitSum = 0

for i in str(num):
	digitSum += int(i)

print('Digit sum: ' + str(digitSum))