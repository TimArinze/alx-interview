#!/usr/bin/python3
"""
Rotate 2D matrix
"""
from typing import List


def rotate_2d_matrix(matrix: List[List]):
    """Given an mxn = nxn 2D matrix, rotate it 90 degrees clockwise"""
    n = len(matrix)
    # n is the length of the row and column of the nxn matrix
    for i in range(n):
        # i transversing the column
        for j in range(i, n):
            # j transversing the row
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            # first iteration column changes all the value for column to row
        # for the second row we start with second column since we have settle
        # first column and so on.
    for row in matrix:
        row.reverse()
