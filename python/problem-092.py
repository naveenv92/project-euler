### Problem 92 - Square Digit Chains
###------------------------------------------------------------------------------------------------------------------------------------------
### A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.
### For example,
### 44 → 32 → 13 → 10 → 1 → 1
### 85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89
### Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop.
### What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.
### How many starting numbers below ten million will arrive at 89?

### Solution

# Function to calculate chain
def chain_89(n: int) -> bool:
    number = n
    while True:
        squareDigits = 0
        for i in str(number):
            squareDigits += pow(int(i), 2)
        if squareDigits == 1:
            return False
        elif squareDigits == 89:
            return True
        else:
            number = squareDigits


num_of_89 = 0
for i in range(1, 10000000):
    if chain_89(i):
        num_of_89 += 1

print("The number of numbers that end at 89: " + str(num_of_89))
