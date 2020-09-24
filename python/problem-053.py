### Problem 53 - Combinatoric Selections
###---------------------------------------------------------------------------------------------------
### There are exactly ten ways of selecting three from five, 12345:
### 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
### In combinatorics, we use the notation, (5 3)=10.
### In general, (n r)=n!/r!(n−r)!, where r≤n, n!=n×(n−1)×...×3×2×1, and 0!=1.
### It is not until n=23, that a value exceeds one-million: (23 10)=1144066.
### How many, not necessarily distinct, values of (n r) for 1 ≤ n ≤ 100, are greater than one-million?

### Solution

# Function to compute factorial
def factorial(n: int) -> int:
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact


num_above_million = 0
for n in range(1, 101):
    for r in range(1, n + 1):
        combos = factorial(n) / (factorial(n - r) * factorial(r))
        if combos > 1000000:
            num_above_million += 1

print(
    "The number of values of (n r) that are greater than 1,000,000: "
    + str(num_above_million)
)
