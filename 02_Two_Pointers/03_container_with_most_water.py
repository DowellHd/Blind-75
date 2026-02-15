"""
11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/
Difficulty: Medium

Given n non-negative integers height[i], find two lines that together with
the x-axis form a container that holds the most water.

Examples:
    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49

    Input: height = [1,1]
    Output: 1

Constraints:
    - n == height.length
    - 2 <= n <= 10^5
    - 0 <= height[i] <= 10^4
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Hint: Two pointers at both ends. Area = min(h[l], h[r]) * (r - l).
        # Move the pointer with the shorter height inward, since moving
        # the taller one can never increase the area.
        pass
