### Problem 32 - Pandigital Products
###-------------------------------------------------------------------------------------------------------------------------------------------
### We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
### For example, the 5-digit number, 15234, is 1 through 5 pandigital.
### The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
### Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

### Solution

# Function to see if digits are pandigital. a:int, b:int, c:int -> boolean
def isPandigital(a, b, c):
    num_string = str(a) + str(b) + str(c)

    if len(num_string) != 9:
        return False
    else:
        if not "123456789".strip(num_string):
            return True
        else:
            return False


# Function to see if multiplicand and multiplier are unique. a:int, b:int -> boolean
def isUnique(a, b):
    for i in str(a):
        if i in str(b):
            return False
    return True


pandigital_nums = set()
for i in range(1, 3000):
    for j in range(i, 3000):
        if not isUnique(i, j):
            continue
        if isPandigital(i, j, i * j) and (i * j) not in pandigital_nums:
            pandigital_nums.add(i * j)

print("Sum of all 1-9 pandigital products is: " + str(sum(pandigital_nums)))
