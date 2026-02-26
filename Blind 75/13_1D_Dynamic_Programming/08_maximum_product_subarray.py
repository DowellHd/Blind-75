"""
152. Maximum Product Subarray
https://leetcode.com/problems/maximum-product-subarray/
Difficulty: Medium

Given an integer array nums, find the subarray with the largest product.

Examples:
    Input: nums = [2,3,-2,4]
    Output: 6  ([2,3])

    Input: nums = [-2,0,-1]
    Output: 0

Constraints:
    - 1 <= nums.length <= 2 * 10^4
    - -10 <= nums[i] <= 10
"""

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Hint: Track both current max and current min product (negatives
        # can flip min to max). At each element:
        # cur_max = max(num, cur_max*num, cur_min*num)
        # cur_min = min(num, cur_max*num, cur_min*num)
        pass
