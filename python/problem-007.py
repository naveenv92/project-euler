"""
Problem 7 - 10001st Prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see 
that the 6th prime is 13.

What is the 10,001st prime number?
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
        for i in range(2, round(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True


def nth_prime(n: int) -> int:
    """
    Parameters
        n (int): prime number of interest
    Returns
        nth_prime (int): nth prime number
    """

    curr_n = 2
    count = 0

    while True:
        if is_prime(curr_n):
            count += 1
        if count == n:
            break
        curr_n += 1
    return curr_n


if __name__ == "__main__":
    print("The 10,001st prime number is: " + str(nth_prime(10001)))
