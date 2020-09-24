### Problem 37 - Truncatable Primes
###----------------------------------------------------------------------------------------------------------------------------------
### The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right,
### and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
### Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

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


# Function to determine if trunctable from left. n:int -> boolean
def trunctLeft(n):
    num_str = str(n)
    for i in range(len(num_str)):
        if not isPrime(int(num_str[i:])):
            return False
    return True


# Function to determine if trunctable from right. n:int -> boolean
def trunctRight(n):
    num_str = str(n)
    for i in range(len(num_str)):
        if not isPrime(int(num_str[0 : (len(num_str) - i)])):
            return False
    return True


primes = []
current_num = 8

while len(primes) < 11:
    if trunctLeft(current_num) and trunctRight(current_num):
        primes.append(current_num)
    current_num += 1

print("The sum of trunctable primes is: " + str(sum(primes)))
