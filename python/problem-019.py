"""
Problem 19 - Counting Sundays

You are given the following information, but you may prefer to do some 
research for yourself.

* 1 Jan 1900 was a Monday.
* Thirty days has September, April, June and November. All the rest have 
  thirty-one, saving February alone, which has twenty-eight, rain or shine.
  And on leap years, twenty-nine.
* A leap year occurs on any year evenly divisible by 4, but not on a century 
  unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

def num_sundays(end_year: int) -> int:
    """
    Parameters
        end_year (int): year to count until [1900, end_year)
    Returns
        num_sundays (int): number of Sundays in [1900, end_year)
    """

    months = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 
              6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 
              11:'November', 12:'December'}

    days_in_month = {'January': 31, 'February': 28, 'March': 31, 'April': 30,
                     'May': 31, 'June': 30, 'July': 31, 'August': 31, 
                     'September': 30, 'October': 31, 'November': 30, 
                     'December': 31}

    days_in_month_ly = {'January': 31, 'February': 29, 'March': 31, 
                        'April': 30, 'May': 31, 'June': 30, 'July': 31, 
                        'August': 31, 'September': 30, 'October': 31, 
                        'November': 30, 'December': 31}

    # Starting date
    day, month, year = 1, 1, 1900
    num_sundays = 0

    while year < end_year:
        # Check if it is a Sunday
        if day % 7 == 0 and year != 1900:
            num_sundays += 1
        # Advance days (check if leap year)
        if year % 4 == 0 and not year % 100 == 0:
            day += days_in_month_ly[months[month]]
        else:
            day += days_in_month[months[month]]
        # Advance month
        month += 1
        if month > 12:
            month = 1
            year += 1
    return num_sundays

if __name__ == '__main__':
    print('The number of Sundays on the 1st of the month in the' +
          ' 20th century: ' + str(num_sundays(2001)))
