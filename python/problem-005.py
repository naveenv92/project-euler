"""
Problem 5 - Smallest Multiple

2520 is the smallest number that can be divided by each of the numbers 
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of 
the numbers from 1 to 20?
"""

from typing import Callable

def is_divisible(n: int) -> bool:
    """
    Parameters
        n (int): number to check if divisble by [1, 20]
    Returns
        boolean
    """

    for i in range(1, 21):
        if n % i != 0:
            return False
    return True

def smallest_number(func: Callable[[int], bool]) -> int:
    """
    Parameters
        func (Callable): callback function
    Returns
        n (int): smallest integer that satisfies func
    """

    n = 20
    while True:
        if func(n):
            break
        else:
            n += 20
    return n

if __name__ == '__main__':
    print('The smallest positive number divisible by 1-20 is: '
          + str(smallest_number(is_divisible)))