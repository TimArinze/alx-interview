#!/usr/bin/python3

"""Island Perimeter"""
from typing import List


def island_perimeter(grid: List[List]) -> int:
    """returns the parameter of the island described in the grid"""
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                if grid[i - 1][j] == 0:
                    perimeter += 1
                if grid[i + 1][j] == 0:
                    perimeter += 1
                if grid[i][j - 1] == 0:
                    perimeter += 1
                if grid[i][j - 1] == 0:
                    perimeter += 1
    return perimeter
