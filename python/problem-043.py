### Problem 43 - Sub-String Divisibility
###------------------------------------------------------------------------------------------------------------------------
### The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, 
### but it also has a rather interesting sub-string divisibility property.
### Let d_1 be the 1st digit, d_2 be the 2nd digit, and so on. In this way, we note the following:
### d_2d_3d_4=406 is divisible by 2
### d_3d_4d_5=063 is divisible by 3
### d_4d_5d_6=635 is divisible by 5
### d_5d_6d_7=357 is divisible by 7
### d_6d_7d_8=572 is divisible by 11
### d_7d_8d_9=728 is divisible by 13
### d_8d_9d_10=289 is divisible by 17
### Find the sum of all 0 to 9 pandigital numbers with this property.

### Solution

from itertools import permutations

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers = list(permutations(digits))
nums = []

for i in numbers:
	if i[0] == 0:
		continue
	currNum = ''
	for j in range(len(i)):
		currNum += str(i[j])
	nums.append(currNum)

pan_div = []

for i in nums:
	if int(i[1:4]) % 2 == 0:
		if int(i[2:5]) % 3 == 0:
			if int(i[3:6]) % 5 == 0:
				if int(i[4:7]) % 7 == 0:
					if int(i[5:8]) % 11 == 0:
						if int(i[6:9]) % 13 == 0:
							if int(i[7:10]) % 17 == 0:
								pan_div.append(int(i))

print('The sum of all 0 to 9 pandigital numbers with this property is: ' + str(sum(pan_div)))
