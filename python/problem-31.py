### Problem 48 - Coin Sums
###------------------------------------------------------------------------------------------------------------------------
### In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:
### 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
### It is possible to make £2 in the following way:
### 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
### How many different ways can £2 be made using any number of coins?

### Solution

import numpy as np

# Dictionary of values of coins
values = {0:1, 1:2, 2:5, 3:10, 4:20, 5:50, 6:100, 7:200}
coinSums = np.zeros((201, 8))

for i in range(1, 201):
	for j in range(8):
		if j == 0:
			coinSums[i][j] = 1
		else:
			coinSums[i][j] = coinSums[i][j-1]
			if i - values[j] >= 0:
				coinSums[i][j] += coinSums[i - values[j]][j]
			if i == values[j]:
				coinSums[i][j] += 1

print('Total ways to make £2: ' + str(int(coinSums[200][7])))