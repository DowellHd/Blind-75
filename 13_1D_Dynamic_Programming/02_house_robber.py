"""
198. House Robber
https://leetcode.com/problems/house-robber/
Difficulty: Medium

Given an array representing money in each house along a street, return the
maximum amount you can rob without robbing two adjacent houses.

Examples:
    Input: nums = [1,2,3,1]
    Output: 4  (rob house 1 and 3)

    Input: nums = [2,7,9,3,1]
    Output: 12  (rob house 1, 3, 5)

Constraints:
    - 1 <= nums.length <= 100
    - 0 <= nums[i] <= 400
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # Hint: dp[i] = max(dp[i-1], dp[i-2] + nums[i]).
        # At each house: skip it (take dp[i-1]) or rob it (dp[i-2] + nums[i]).
        # Only need two variables.
        pass
