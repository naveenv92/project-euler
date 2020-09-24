"""
Problem 20 - Factorial Digit Sum

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800, and the sum of the 
digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""


def factorial(n: int) -> int:
    """
    Parameters
        n (int): calculate factorial of n
    Returns
        factorial (int): n!
    """

    factorial = 1
    if n == 0:
        return 1
    else:
        for i in range(1, n + 1):
            factorial *= i
    return factorial


def digit_sum(n: int) -> int:
    """
    Parameters
        n (int): calculate digit sum of n
    Returns
        digit_sum (int): sum of digits of n
    """

    digit_sum = 0
    for i in str(n):
        digit_sum += int(i)
    return digit_sum


if __name__ == "__main__":
    print("Sum of digits in 100!: %i" % digit_sum(factorial(100)))
