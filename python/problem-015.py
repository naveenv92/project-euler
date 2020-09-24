"""
Problem 15 - Lattice Paths

Starting in the top left corner of a 2×2 grid, and only being able to move 
to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

import numpy as np


def lattice_paths(n: int) -> int:
    """
    Parameters
        n (int): size of grid (n x n)
    Returns
        paths (int): number of lattice paths
    """

    grid = np.ones((n + 1, n + 1))

    for i in range(1, 21):
        for j in range(1, 21):
            grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
    return int(grid[n][n])


if __name__ == "__main__":
    print(
        "The number of lattice paths in a 20x20 grid are: "
        + str(lattice_paths(20))
    )
