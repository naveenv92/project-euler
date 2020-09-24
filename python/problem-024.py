### Problem 24 - Lexicographic Permutations
###-------------------------------------------------------------------------------------------------------------------------------
### A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
### If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
### The lexicographic permutations of 0, 1 and 2 are:
### 012   021   102   120   201   210
### What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

### Solution

import numpy as np
import math

# Convert decimal base number to a factorial base
def convertToFac(n):
    number = ""
    counter = 0
    while True:
        counter += 1
        number = number + str(n % counter)
        if math.floor(n / counter) == 0:
            break
        n = math.floor(n / counter)

    return number[::-1]


# Get 1,000,000 in factorial base
million = list(convertToFac(999999))

# Convert to lexicographic permutation
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lexicographic = ""
for i in million:
    lexicographic = lexicographic + str(digits.pop(int(i)))

print("Millionth lexicographic permutation is: " + lexicographic)
