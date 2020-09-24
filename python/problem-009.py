"""
Problem 9 - Special Pythagorean Triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for 
which, a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.

Find the product abc.
"""


def pythagorean_triplet(n: int) -> int:
    """
    Parameters
        n (int): the sum of a + b + c
    Returns
        prod (int): product a*b*c
    """

    prod = 0
    for a in range(1, n + 1):
        for b in range(a, n + 1):
            c = n - a - b
            if (a ** 2 + b ** 2 == c ** 2) and (a + b + c == 1000):
                prod = a * b * c
                break
    return prod


if __name__ == "__main__":
    print(
        "The Pythagorean triplet for which a + b + c = 1000 is: "
        + str(pythagorean_triplet(1000))
    )
