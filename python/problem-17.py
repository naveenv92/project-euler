### Problem 17
###------------------------------------------------------------------------------------------------------------------------------------------
### If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
### If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

### Solution
import math

letters = {'1': 3, '2': 3, '3': 5, '4': 4, '5': 4, '6': 3, '7': 5, '8': 5, '9': 4, '10': 3, '11': 6, '12': 6, '13': 8, '14': 8, '15': 7,
		   '16': 7, '17': 9, '18': 8, '19': 8, '20': 6, '30': 6, '40': 5, '50': 5, '60': 5, '70': 7, '80': 6, '90': 6, '100': 7, '1000': 8}

numOfLetters = 0

for i in range(1, 1001):
	currentNum = i
	if currentNum == 1000:
		numOfLetters += letters['1'] + letters['1000']
		currentNum -= 1000
	if math.floor(currentNum/100.0) > 0:
		numOfLetters += letters['100']
		numOfLetters += letters[str(math.floor(i/100.0))]
		currentNum -= math.floor(currentNum/100.0)*100
	if i > 100 and i % 100 != 0:
		numOfLetters += 3 # for 'and'
	if math.floor(currentNum/90.0) > 0:
		numOfLetters += letters['90']
		currentNum -= 90
	if math.floor(currentNum/80.0) > 0:
		numOfLetters += letters['80']
		currentNum -= 80
	if math.floor(currentNum/70.0) > 0:
		numOfLetters += letters['70']
		currentNum -= 70
	if math.floor(currentNum/60.0) > 0:
		numOfLetters += letters['60']
		currentNum -= 60
	if math.floor(currentNum/50.0) > 0:
		numOfLetters += letters['50']
		currentNum -= 50
	if math.floor(currentNum/40.0) > 0:
		numOfLetters += letters['40']
		currentNum -= 40
	if math.floor(currentNum/30.0) > 0:
		numOfLetters += letters['30']
		currentNum -= 30
	if math.floor(currentNum/20.0) > 0:
		numOfLetters += letters['20']
		currentNum -= 20
	if str(currentNum) in letters:
		numOfLetters += letters[str(currentNum)]

print("Number of letters in 1 to 1000: " + str(numOfLetters))