### Problem 15
###---------------------------------------------------------------------------------------------------------------------------------------------------------
### Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
### How many such routes are there through a 20×20 grid?

### Solution

import numpy as np

# Create grid to calculate lattice paths
grid = np.ones((21, 21))

for i in range(1, 21):
	for j in range(1, 21):
		grid[i][j] = grid[i-1][j] + grid[i][j-1]

print(grid[20][20])