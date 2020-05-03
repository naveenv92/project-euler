"""
Problem 21 - Amicable Numbers

Let d(n) be defined as the sum of proper divisors of n (numbers less than n 
which divide evenly into n).

If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and 
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 
and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

def sum_of_divisors(n: int) -> int:
    """
    Parameters
        n (int): input integer
    Returns
        (int): sum of divisors of n
    """

    divisors = [1]

    for i in range(2, round(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if not i**2 == n:
                divisors.append(n/i)
    return sum(divisors)

def amicable_sum(n: int) -> int:
    """
    Parameters
        n (int): find amicable sum below n
    Return
        amicable_sum (int): sum of amicable numbers in [0, n)
    """

    amicable_sum = 0

    for i in range(2, n):
        divisor_sum = sum_of_divisors(i)
        if sum_of_divisors(divisor_sum) == i and divisor_sum != i:
            amicable_sum += i
    return amicable_sum

if __name__ == '__main__':
    print('Sum of amicable numbers under 10000: %i' % amicable_sum(10000))