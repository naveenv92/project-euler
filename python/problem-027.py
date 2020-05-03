### Problem 27 - Quadratic Primes
###------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### Euler discovered the remarkable quadratic formula:
### n^2 + n + 41
### It turns out that the formula will produce 40 primes for the consecutive integer values 0 ≤ n ≤ 39 
### However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41
### The incredible formula n^2 − 79n + 1601 was discovered, which produces 80 primes for the consecutive values 0 ≤ n ≤ 79 
### The product of the coefficients, −79 and 1601, is −126479.
### Considering quadratics of the form:
### n^2 + an + b, where |a| < 1000 and |b| ≤ 1000
### where |n| is the modulus/absolute value of n
### e.g. |11| = 11 and |−4| = 4
### Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.

def isPrime(n):
	if n < 2:
		return False
	elif n == 2:
		return True
	else:
		i = 2
		while i**2 <= n:
			if n % i == 0:
				return False
			i += 1
		return True


def quadratic(a, b):
	n = 0
	while True:
		test = n**2 + a*n + b
		if isPrime(test):
			n += 1
		else: break
	return n

longestChain = 0
coeff_a = 0
coeff_b = 0

for a in range(-1000, 1000):
	for b in range(-1000, 1001):
		n = quadratic(a, b)
		if n > longestChain:
			longestChain = n
			coeff_a = a
			coeff_b = b

print('The product of the coefficients is: ' + str(coeff_a*coeff_b))