### Problem 82 - Path Sum: Three Ways
###-------------------------------------------------------------------------------------------------------------------------------------------
### The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column and finishing in any cell in the right column,
### and only moving up, down, and right, is indicated in red and bold; the sum is equal to 994.
### Find the minimal path sum from the left column to the right column in matrix.txt (right click and "Save Link/Target As..."),
### a 31K text file containing an 80 by 80 matrix.

### Solution

import numpy as np

# grid = np.loadtxt('../p082_matrix.txt', delimiter=',')

grid = np.array(
    [
        [131, 673, 234, 103, 18],
        [201, 96, 342, 965, 150],
        [630, 803, 746, 422, 111],
        [537, 699, 497, 121, 956],
        [805, 732, 524, 37, 331],
    ]
)

for i in range(len(grid)):
    grid[i, len(grid) - 2] += grid[i, len(grid) - 1]

newgrid = grid.copy()

for i in range(len(grid) - 2, -1, -1):
    for j in range(len(grid) - 3, 0, -1):
        if i == 0:
            newgrid[i, j] = grid[i, j] + min(grid[i + 1, j], grid[i, j + 1])
        elif i == len(grid) - 2:
            newgrid[i, j] += min(grid[i - 1, j], grid[i, j + 1])
        else:
            newgrid[i, j] += min(
                grid[i - 1, j], grid[i, j + 1], grid[i + 1, j]
            )

for i in range(len(grid)):
    newgrid[i, 0] += newgrid[i, 1]

print(newgrid)
