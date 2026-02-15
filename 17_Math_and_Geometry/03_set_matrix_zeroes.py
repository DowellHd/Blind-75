"""
73. Set Matrix Zeroes
https://leetcode.com/problems/set-matrix-zeroes/
Difficulty: Medium

Given an m x n integer matrix, if an element is 0, set its entire row and
column to 0's. Do it in place.

Examples:
    Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
    Output: [[1,0,1],[0,0,0],[1,0,1]]

    Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Constraints:
    - m == matrix.length, n == matrix[0].length
    - 1 <= m, n <= 200
"""

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # Hint: Use the first row and first column as markers.
        # First pass: mark which rows/cols should be zeroed.
        # Second pass: set cells to zero based on markers.
        # Handle first row/col separately with boolean flags.
        pass
