"""
Problem 22 - Names Score

Begin by sorting it into alphabetical order. Then working out the 
alphabetical value for each name, multiply this value by its alphabetical 
position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which 
is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN 
would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

import numpy as np
from os import path

def names_score(names: np.ndarray) -> int:

    letters = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8,
               'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 
               'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 
               'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
    names = sorted(names)
    total_score = 0

    for i in range(len(names)):
        multiplier = i + 1
        name_score = 0
        for j in names[i]:
            name_score += letters[j]
        name_score *= multiplier
        total_score += name_score
    return total_score

if __name__ == '__main__':
    directory = path.dirname(path.dirname(path.abspath(__file__)))
    file = '/p022_names.txt'
    names = np.genfromtxt(directory + file, delimiter=',', dtype=str)
    names = [name.strip('"') for name in names]
    print('The total name score is: %i' % names_score(names))
