### Problem 46 - Goldbach's Other Conjecture
###-------------------------------------------------------------------------------------------------------------------------------
### It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
### 9 = 7 + 2 × 1^2
### 15 = 7 + 2 × 2^2
### 21 = 3 + 2 × 3^2
### 25 = 7 + 2 × 3^2
### 27 = 19 + 2 × 2^2
### 33 = 31 + 2 × 1^2
### It turns out that the conjecture was false.
### What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

### Solution

import math

# Function to determine if prime. n:int -> boolean
def isPrime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        i = 2
        while i ** 2 <= n:
            if n % i == 0:
                return False
            i += 1
        return True


number = 1
primes = []

while True:
    number += 1
    flag = False
    if isPrime(number):
        primes.append(number)
        continue
    elif number % 2 == 0:
        continue
    else:
        for i in primes:
            sq = ((number - i) / 2) ** 0.5
            if (sq - math.floor(sq)) == 0:
                flag = True
                break
        if flag == False:
            break

print(
    "The smallest odd number that cannot be written as the sum of a prime and twice a square is: "
    + str(number)
)
