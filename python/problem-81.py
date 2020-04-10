### Problem 81 - Path Sum: Two Ways
###-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.
### Find the minimal path sum from the top left to the bottom right by only moving right and down in matrix.txt (right click and "Save Link/Target As..."), 
### a 31K text file containing an 80 by 80 matrix.

### Solution

import numpy as np

grid = np.loadtxt('../p081_matrix.txt', delimiter=',')

for i in range(len(grid) - 2, -1, -1):
	grid[len(grid) - 1, i] += grid[len(grid) - 1, i + 1]
	grid[i, len(grid) - 1] += grid[i + 1, len(grid) - 1]

for i in range(len(grid) - 2, -1, -1):
	for j in range(len(grid) - 2, -1, -1):
		grid[i][j] += min(grid[i + 1, j], grid[i, j + 1])

print('The minimal path sum is: ' + str(grid[0][0]))