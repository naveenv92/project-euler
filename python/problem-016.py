"""
Problem 16 - Power Digit Sum

2^(15) = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26

What is the sum of the digits of the number 2^(1000)?
"""


def digit_sum(base: int, exponent: int) -> int:
    """
    Parameters
        base (int): base value
        exponent (int): exponent to raise base value to
    """
    num = base ** exponent
    return sum([int(i) for i in str(num)])


if __name__ == "__main__":
    print("The digit sum of 2^1000 is: " + str(digit_sum(2, 1000)))
