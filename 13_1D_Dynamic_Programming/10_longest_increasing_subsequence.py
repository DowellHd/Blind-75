"""
300. Longest Increasing Subsequence
https://leetcode.com/problems/longest-increasing-subsequence/
Difficulty: Medium

Given an integer array nums, return the length of the longest strictly
increasing subsequence.

Examples:
    Input: nums = [10,9,2,5,3,7,101,18]
    Output: 4  ([2,3,7,101])

    Input: nums = [0,1,0,3,2,3]
    Output: 4

Constraints:
    - 1 <= nums.length <= 2500
    - -10^4 <= nums[i] <= 10^4

Follow up: Can you solve in O(n log n)?
"""

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Hint: O(n^2): dp[i] = LIS length ending at i. For each j < i,
        # if nums[j] < nums[i]: dp[i] = max(dp[i], dp[j]+1).
        # O(n log n): maintain "tails" array, use bisect_left to find position.
        pass
