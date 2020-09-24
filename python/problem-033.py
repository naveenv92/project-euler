### Problem 33 - Digit Cancelling Fractions
###----------------------------------------------------------------------------------------------------------------------------------------------------------
### The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8,
### which is correct, is obtained by cancelling the 9s.
### We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
### There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
### If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

### Solution

# Function to determine if fraction is digit cancelling. num:int, den:int -> boolean
def digitCancelling(num, den):
    num_string = str(num)
    den_string = str(den)

    if int(num_string[1]) == 0 and int(den_string[1]) == 0:
        return False
    elif num_string[0] == den_string[0] and int(den_string[1]) != 0:
        if float(num_string[1]) / float(den_string[1]) == num / den:
            return True
    elif num_string[0] == den_string[1] and int(den_string[0]) != 0:
        if float(num_string[1]) / float(den_string[0]) == num / den:
            return True
    elif num_string[1] == den_string[1] and int(den_string[0]) != 0:
        if float(num_string[0]) / float(den_string[0]) == num / den:
            return True
    elif num_string[1] == den_string[0] and int(den_string[1]) != 0:
        if float(num_string[0]) / float(den_string[1]) == num / den:
            return True
    else:
        return False


# Function to find the Euclidean GCD. a:int, b:int -> gcd:int
def euclideanGCD(a, b):
    while True:
        if a >= b:
            a %= b
            if a == 0:
                return b
        elif a < b:
            b %= a
            if b == 0:
                return a


# Find digit cancelling fractions
product_num = 1
product_den = 1
for i in range(10, 100):
    for j in range(10, 100):
        if i == j:
            continue
        if i > j:
            continue
        if digitCancelling(i, j):
            product_num *= i
            product_den *= j

fraction_gcd = euclideanGCD(product_num, product_den)
print(
    "The denominator of the product of digit cancelling fractions is: "
    + str(product_den / fraction_gcd)
)
