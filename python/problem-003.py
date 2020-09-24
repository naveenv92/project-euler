"""
Problem 3 - Largest Prime Factor

The prime factors of 13195 are 5, 7, 13, and 29.

What is the largest prime factor of the number 600851475143?
"""

import numpy as np


def is_prime(n: int) -> bool:
    """
    Parameters
        n (int): number to test for primaility
    Returns
        boolean
    """

    if n == 2:
        return True
    for i in range(2, int(np.sqrt(n))):
        if n % i == 0:
            return False
    return True


def largest_prime_factor(n: int) -> int:
    """
    Parameters
        n (int): number to find factor for
    Returns
        largest_factor (int): largest prime factor of n
    """

    largest_factor = 1

    for i in range(2, int(np.sqrt(n))):
        if n % i == 0:
            if is_prime(i):
                largest_factor = i
    return largest_factor


if __name__ == "__main__":
    print(
        "The largest prime factor of 600851475143 is: "
        + str(largest_prime_factor(600851475143))
    )
