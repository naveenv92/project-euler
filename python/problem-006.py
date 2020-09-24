"""
Problem 6 - Sum Square Difference

The sum of the squares of the first ten natural numbers is, 
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is, 
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten 
natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one 
hundred natural numbers and the square of the sum.
"""


def sum_square_diff(n: int) -> int:
    """
    Parameters
        n (int): range of [0, n) to calculate difference
    Returns
        sum square difference of [0, n)
    """

    sum_square = sum([i ** 2 for i in range(n)])
    square_sum = sum(range(n)) ** 2
    return square_sum - sum_square


if __name__ == "__main__":
    print(
        "The sum square difference of 1-100 is: " + str(sum_square_diff(101))
    )
