"""
48. Rotate Image
https://leetcode.com/problems/rotate-image/
Difficulty: Medium

Given an n x n 2D matrix representing an image, rotate it 90 degrees
clockwise in-place.

Examples:
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [[7,4,1],[8,5,2],[9,6,3]]

Constraints:
    - n == matrix.length == matrix[i].length
    - 1 <= n <= 20
    - -1000 <= matrix[i][j] <= 1000
"""

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Hint: Transpose the matrix (swap matrix[i][j] with matrix[j][i]),
        # then reverse each row. This gives 90-degree clockwise rotation.
        pass
