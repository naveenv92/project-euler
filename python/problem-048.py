### Problem 48 - Self Powers
###----------------------------------------------------------------------
### The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
### Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000

### Solution

selfPowerSum = 0

for i in range(1, 1001):
    selfPowerSum += i ** i

print("The last ten digits are: " + str(selfPowerSum)[-10:])
