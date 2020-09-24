### Problem 40 - Champernowne's Constant
###----------------------------------------------------------------------------------------------------
### An irrational decimal fraction is created by concatenating the positive integers:
### 0.123456789101112131415161718192021...
### It can be seen that the 12th digit of the fractional part is 1.
### If d_n represents the nth digit of the fractional part, find the value of the following expression.
### d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000

### Solution

number = 1
decimal = ""

while len(decimal) <= 1000000:
    decimal = decimal + str(number)
    number += 1

product = (
    int(decimal[0])
    * int(decimal[9])
    * int(decimal[99])
    * int(decimal[999])
    * int(decimal[9999])
    * int(decimal[99999])
    * int(decimal[999999])
)

print("The product is: " + str(product))
