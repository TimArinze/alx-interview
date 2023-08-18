#!/usr/bin/python3
"""
Rotate 2D matrix
"""
from typing import List


def rotate_2d_matrix(matrix: List[List]):
    """Given an mxn = nxn 2D matrix, rotate it 90 degrees clockwise"""
    n = len(matrix)
    #n is the n of the matrix
    for i in range(n):
        #m is the i-max of the matrix
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
