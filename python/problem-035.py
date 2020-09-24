### Problem 35 - Circular Primes
###--------------------------------------------------------------------------------------------------------------------------
### The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
### There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
### How many circular primes are there below one million?

### Solution

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


# Function to see if all circulations are prime. n:int -> boolean
def isCircular(n):

    if not isPrime(n):
        return False

    num_string = list(str(n))
    for i in range(len(num_string) - 1):
        temp_index = num_string[0]

        for j in range(len(num_string) - 1):
            num_string[j] = num_string[j + 1]
        num_string[-1] = temp_index

        if not isPrime(int("".join(num_string))):
            return False
    return True


total_primes = 0
for i in range(1, 1000000):
    if isCircular(i):
        total_primes += 1

print("The total circular primes below 1,000,000 is: " + str(total_primes))
