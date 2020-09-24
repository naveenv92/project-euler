### Problem 50 - Consecutive Prime Sum
###-----------------------------------------------------------------------------------------------------------------------
### The prime 41, can be written as the sum of six consecutive primes:
### 41 = 2 + 3 + 5 + 7 + 11 + 13
### This is the longest sum of consecutive primes that adds to a prime below one-hundred.
### The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
### Which prime, below one-million, can be written as the sum of the most consecutive primes?

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


# Generate prime sums
primes = []
for i in range(10001):
    if isPrime(i):
        if len(primes) > 0:
            primes.append(i + primes[-1])
        else:
            primes.append(i)

max_length = 0
max_val = 0
for i in range(-1, len(primes)):

    # Subtract off primes starting from the beginning
    if i == -1:
        tempprimes = primes
    else:
        diff = primes[i]
        tempprimes = [i - diff for i in primes]

    # Check if the number is prime starting from the end and determine the length of the sum
    for j in range(len(tempprimes) - 1, -1, -1):
        length = 0
        val = 0
        if tempprimes[j] > 1000000:
            continue
        elif isPrime(tempprimes[j]):
            length = j - i
            val = tempprimes[j]
            break
    if length > max_length:
        max_length = length
        max_val = val

print(
    "The longest consecutive prime sum sequence is "
    + str(max_length)
    + " for a value of "
    + str(max_val)
)
