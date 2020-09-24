"""
Problem 57 - Square Root Convergents

It is possible to show that the square root of two can be expressed as an 
infinite continued fraction.

In the first one-thousand expansions, how many fractions contain a numerator 
with more digits than the denominator?
"""


def num_fracs(n: int) -> int:
    """
    Calculate number of fraction with more digits in numerator

    Parameters
        n (int): number of terms in series

    Returns
        (int): number of terms with more digits in the numerator
    """

    num = 3
    den = 2
    num_fracs = 0
    for _ in range(2, n + 1):
        num_temp = num + 2 * den
        den_temp = num + den
        if len(str(num_temp)) > len(str(den_temp)):
            num_fracs += 1
        num = num_temp
        den = den_temp
    return num_fracs


if __name__ == "__main__":
    print(
        "The number of expansions with more digits in the numerator:"
        + str(num_fracs(1000))
    )
