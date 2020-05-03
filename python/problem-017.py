"""
Problem 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out 
in words, how many letters would be used?
"""

import math

def num_of_letters(n: int) -> int:
    """
    Parameters
        n (int): upper range of numbers to add letters [1, n]
    Returns
        num_letters (int): number of letters in [1, n]
    """
    
    num_letters = 0
    lett = {'1': 3, '2': 3, '3': 5, '4': 4, '5': 4, '6': 3, '7': 5, '8': 5,
            '9': 4, '10': 3, '11': 6, '12': 6, '13': 8, '14': 8, '15': 7,
            '16': 7, '17': 9, '18': 8, '19': 8, '20': 6, '30': 6, '40': 5, 
            '50': 5, '60': 5, '70': 7, '80': 6, '90': 6, '100': 7, '1000': 8}

    for i in range(1, n+1):
        current_num = i
        if current_num == 1000:
            num_letters += lett['1'] + lett['1000']
            current_num -= 1000
        if math.floor(current_num/100.0) > 0:
            num_letters += lett['100']
            num_letters += lett[str(math.floor(i/100.0))]
            current_num -= math.floor(current_num/100.0)*100
        if i > 100 and i % 100 != 0:
            num_letters += 3 # for 'and'
        if math.floor(current_num/90.0) > 0:
            num_letters += lett['90']
            current_num -= 90
        if math.floor(current_num/80.0) > 0:
            num_letters += lett['80']
            current_num -= 80
        if math.floor(current_num/70.0) > 0:
            num_letters += lett['70']
            current_num -= 70
        if math.floor(current_num/60.0) > 0:
            num_letters += lett['60']
            current_num -= 60
        if math.floor(current_num/50.0) > 0:
            num_letters += lett['50']
            current_num -= 50
        if math.floor(current_num/40.0) > 0:
            num_letters += lett['40']
            current_num -= 40
        if math.floor(current_num/30.0) > 0:
            num_letters += lett['30']
            current_num -= 30
        if math.floor(current_num/20.0) > 0:
            num_letters += lett['20']
            current_num -= 20
        if str(current_num) in lett:
            num_letters += lett[str(current_num)]
    return num_letters

print("Number of letters in 1 to 1000: " + str(num_of_letters(1000)))