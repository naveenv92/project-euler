"""
Problem 1 - Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6, and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def sum_of_multiples(n: int) -> int:
    """
    Parameters
        n (int): maximum value to use for sum
    Returns
        total (int): sum of multiples of 3 and 5
    """

    total = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

if __name__ == '__main__':
    print('The sum of multiples of 3 or 5 below 1000 is: ' +
          str(sum_of_multiples(1000)))