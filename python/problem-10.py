"""
Problem 10 - Summation of Primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17

Find the sum of all the primes below two million
"""

def is_prime(n: int) -> bool:
    """
    Parameters
        n (int): number to check primality
    Returns
        boolean
    """

    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, round(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

def sum_of_primes(n: int) -> int:
    """
    Parameters
        n (int): upper value of primes to sum
    Returns
        sum_of_primes (int): sum of primes from [2, n)
    """

    sum_of_primes = 0

    for i in range(n):
        if is_prime(i):
            sum_of_primes += i
    return sum_of_primes

if __name__ == "__main__":
    print('The sum of all primes below 2,000,000 is: ' +
          str(sum_of_primes(2000000)))