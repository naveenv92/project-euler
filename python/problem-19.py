### Problem 19 - Counting Sundays
###------------------------------------------------------------------------------------------------------
### You are given the following information, but you may prefer to do some research for yourself.
### * 1 Jan 1900 was a Monday.
### * Thirty days has September,
###   April, June and November.
###   All the rest have thirty-one,
###   Saving February alone,
###   Which has twenty-eight, rain or shine.
###   And on leap years, twenty-nine.
### * A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
### How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

### Solution

# Dictionary matching month numbers to names
months = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}

# Dictionary for number of days in a month
daysInMonth = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 
			   'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}

# Dictionary for number of days in a month during leap year
daysInMonthLY = {'January': 31, 'February': 29, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 
			   'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}

# Starting date
year = 1900
month = 1
day = 1

numberOfSundays = 0

while year < 2001:

	# Check if it is a Sunday
	if day % 7 == 0 and year != 1900:
		numberOfSundays += 1

	# Advance days (check if leap year)
	if year % 4 == 0 and not year % 100 == 0:
		day += daysInMonthLY[months[month]]
	else:
		day += daysInMonth[months[month]]

	# Advance month
	month += 1
	if month > 12:
		month = 1
		year += 1

print('Sundays on the 1st of the month in the 20th century: ' + str(numberOfSundays))
