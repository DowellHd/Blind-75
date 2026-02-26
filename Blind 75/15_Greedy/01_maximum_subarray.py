"""
53. Maximum Subarray
https://leetcode.com/problems/maximum-subarray/
Difficulty: Medium

Given an integer array nums, find the subarray with the largest sum.

Examples:
    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6  ([4,-1,2,1])

    Input: nums = [1]
    Output: 1

Constraints:
    - 1 <= nums.length <= 10^5
    - -10^4 <= nums[i] <= 10^4
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Hint: Kadane's algorithm. Track current_sum. If it drops below 0,
        # reset to 0 (start fresh). Track the max_sum seen so far.
        # current_sum = max(num, current_sum + num)
        pass
