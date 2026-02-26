"""
213. House Robber II
https://leetcode.com/problems/house-robber-ii/
Difficulty: Medium

Same as House Robber, but the houses are arranged in a circle (first and
last houses are adjacent).

Examples:
    Input: nums = [2,3,2]
    Output: 3

    Input: nums = [1,2,3,1]
    Output: 4

Constraints:
    - 1 <= nums.length <= 100
    - 0 <= nums[i] <= 1000
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # Hint: Can't rob both first and last house. Run House Robber I
        # twice: once on nums[1:] and once on nums[:-1]. Return the max.
        pass
